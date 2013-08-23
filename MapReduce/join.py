'''

@Author : Madhav

@Summary: Relational join as MapReduce query.

'''


import MapReduce
import sys
import json


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    table = record[0]
    record_id = record[1]
    mr.emit_intermediate(record_id,record)
def reducer(key, list_of_values):
    orderlist = []
    finallist = []
    order_len = len(orderlist)
    #linelist_len = len(lineitemlist)
    for item in list_of_values:
		orderlist.append(item)
    for i in range(len(orderlist)-1):
		for j in range(i,len(orderlist)):
			if(orderlist[i][0]<>orderlist[j][0] and orderlist[i][1]==orderlist[j][1]):
				mr.emit(orderlist[i]+orderlist[j])
				
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
