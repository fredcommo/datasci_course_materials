import MapReduce
import sys

"""
Return asymmetric friends
if ['personA', 'personB'] so personB is a friend of personA,
but if not ['personB', 'personA'] personA is not a friend of personB.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: personA
    # value: (personA, personB)
    mr.emit_intermediate(str(sorted(record)), sorted(record))

def reducer(key, value):
  # key: personA
  # value: numbrer of friends
  if len(value) == 1:
    for v in value:
      mr.emit((v[0], v[1]))
      mr.emit((v[1], v[0]))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
