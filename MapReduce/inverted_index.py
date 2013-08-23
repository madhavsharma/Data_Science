import MapReduce
import sys
import json
"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    doc_id = record[0]
    content = record[1]
    #print doc_id,content
    word_list = []
    words = content.split()
    for w in words:
		if w not in word_list:
			word_list.append(w)
			mr.emit_intermediate(w,doc_id)
		else:
			continue

def reducer(key, list_of_values):
    inverted_index = []
    for v in list_of_values:
      inverted_index.append(v)
    mr.emit((key,inverted_index))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
