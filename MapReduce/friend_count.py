'''

@Author : Madhav

@Summary: Calculates the number of friends.

'''


import MapReduce
import sys
import json


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	key = record[0]
	value = record[1]
	mr.emit_intermediate(key,1)

def reducer(key, list_of_values):
	total = 0
	for value in list_of_values:
		total+= value
	mr.emit((key,total))
	


		
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
