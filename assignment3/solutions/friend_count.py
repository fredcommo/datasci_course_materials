import MapReduce
import sys

"""
Count friends
If personA is linked to personB: personB is a friend of personA,
but personA can be not a friend of personB.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: personA
    # value: 1 is as a friend
    mr.emit_intermediate(record[0], 1)

def reducer(key, value):
    # key: personA
    # value: numbrer of friends
    total = 0
    for v in value:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
