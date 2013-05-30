import MapReduce
import sys

"""
Remove the 10 last nucleotides and returns the sequence without duplicates.
To suppress duplics, simply returns the sequences as keys.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: Id
    # value: nucleotides
    key = record[0]
    value = record[1]
    n = len(value)
    mr.emit_intermediate(value[:n-10], 1)

def reducer(key, value):
  # key: personA
  # value: numbrer of friends
  mr.emit(str(key))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
