'''

@Author : Madhav

@Summary: Removes last 10 characters from string of nucleoatides and remove any duplicates if any.

'''




import MapReduce
import sys
import json
from collections import Counter


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	key = record[0].encode('utf-8')
	value = record[1].encode('utf-8')[:-10]
	#print "emit 1",key,value
	mr.emit_intermediate(value,key)
	#print "emit 2",value,key
	#mr.emit_intermediate(value,key)
	#print "calling reducer for ",key,value

def reducer(key, list_of_values):
	#print "received", key,list_of_values
	mr.emit((key))

		
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
