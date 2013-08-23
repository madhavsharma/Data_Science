'''

@Author : Madhav

@Summary: Matrix Multiplication implemented using MapReduce.

'''



import MapReduce
import sys



mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	table = record[0].encode('utf-8')
	row = record[1]
	col = record[2]
	val = record[3]
	
	if table == 'a':
		for k in range(0,5):
			#pass
			mr.emit_intermediate((row,k),record)
	else:
		for l in range(0,5):
			#pass
			mr.emit_intermediate((l,col),record)

def reducer(key, list_of_values):
	#print  list_of_values
	a = {}
	b = {}
	for val in list_of_values:
		if val[0] == 'a':
			key_a = str(val[1]) + str(val[2])
			a[key_a] = val[3]
		else:
			key_b = str(val[1]) + str(val[2])
			b[key_b] = val[3]
	result = 0
	
	for res in range (0,5):
		a_key = str(key[0])+str(res)
		b_key = str(res)+str(key[1])
		if a_key in a.keys() and b_key in b.keys():
			result += (a[a_key] * b[b_key])
	if result <> 0:
		mr.emit((key[0],key[1],result))
	
	
		
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
