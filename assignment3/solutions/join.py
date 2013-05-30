import MapReduce
import sys

"""
Return a list of orders and corresponding items, one output per item.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id in record[1]
    # value: the entire record
    mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    # key: order_id
    # value: order record + item record
    order = list_of_values[0]
    for item in list_of_values[1:]:
      mr.emit(order+item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
