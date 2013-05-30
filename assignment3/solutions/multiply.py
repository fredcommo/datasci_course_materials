import MapReduce
import sys

"""
Compute matrix multiplication
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  K = range(5)
  i = 0
  # key: (i,k) if A, (j, k) otherwise
  # value: A[i,j] or B[j,k]
  if record[0] == 'a':
    for k in K:
      mr.emit_intermediate((record[1], k), [record[0], record[2], record[3]])
  else:
    for k in K:
      mr.emit_intermediate((k, record[2]), [record[0], record[1], record[3]])


def reducer(key, value):
#  print 'key', key
#  print 'value', value
  aValues = [v for v in value if v[0]=='a']
  bValues = [v for v in value if v[0]=='b']
  total = 0
  for v1 in aValues:
    for v2 in bValues:
      if v1[1]==v2[1]:
        total += v1[2]*v2[2]
  mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
