import MapReduce
import sys
import json
from collections import Counter
"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	key = record[0].encode('utf-8')
	value = record[1].encode('utf-8')
	#print "emit 1",key,value
	mr.emit_intermediate(key,value)
	#print "emit 2",value,key
	mr.emit_intermediate(value,key)
	#print "calling reducer for ",key,value

def reducer(key, list_of_values):
	#print "received", key,list_of_values
	friend_list = Counter(list_of_values)
	for values in (friend_list.keys()):
		if (friend_list[values] == 1):
			mr.emit((key,values))

		
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
