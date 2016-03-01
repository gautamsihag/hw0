"""
Columbia W4111 Intro to databases
Homework 2
"""

import sys
from collections import *

def load_data(file_path):
  """
  This method reads the dataset, and returns a list of rows.
  Each row is a list containing the values in each column.
  """
  import csv
  with file(file_path) as f:
    dialect = csv.Sniffer().sniff(f.read(2048))
    f.seek(0)
    reader = csv.reader(f, dialect)
    return [l for l in reader]


def q1(data):
  a = set()
  for i in data[1:]:
    a.add(i[15])
  return len(a)
  """
  @param data the output of load_data()
  @return the number of  distinct types of items (by `description` attribute) in this dataset
  """
  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
  #return -1

def q2(data):
  d = set()
  for i in data[1:]:
    d.add(i[13])
  return len(d)

  """
  @param data the output of load_data()
  @return the number of  distinct `vendor`s (by exact string comparison) in this dataset
  """
  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
  #return -1

def q3(data):
  c = {}
  for i in data[1:]:
    store = i[2]
    if store not in c:
      c[store]=int(i[20])
    else:
      c[store]=int(c[store])+int(i[20])
#if bottle_qty < i[20]:
 #       bottle_qty = i[20]
  #      zipcode = i[6]
  return max(c,key=c.get)
  #i = max(c,key=c.get)
  #print c[i]
  """
  @param data the output of load_data()
  @return the value of the `store` attribute (the id) of the store that had the most sales (as defined by bottle qty)
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
  #return -1

def q4(data):
  c = {}
  e = {}
  for i in data[1:]:
    #desc = i[15]
    store = i[2]
    if store not in c:
      c[store]=int(i[20])
      #e[desc] = int(i[20])
    else:
      #if desc in e:  
      c[store]=int(c[store])+int(i[20])
  out = sorted(c,key=c.get,reverse=True)
  for x in data[1:]:
    if x[2]==out[0]:
      if x[15] in e:
        e[x[15]]= int(e[x[15]])+int(x[20])
      else:
        e[x[15]]=int(x[20]) 
#if bottle_qty < i[20]:
 #       bottle_qty = i[20]
  #      zipcode = i[6]
  return max(e,key=e.get)

  """
  @param data the output of load_data()
  @return The value of the `description` attribute of the most sold item from the store from q3()
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
  return ''

def q5(data):
  b = {}
  #bottle_qty = 0
  #zipcode = '00000'
  for i in data:
    if i[11] == 'TEQUILA':
      zipcode = i[6]
      if zipcode not in b:
        b[zipcode]=int(i[20])
      else:
        b[zipcode]=int(b[zipcode])+int(i[20])
  
#if bottle_qty < i[20]:
 #       bottle_qty = i[20]
  #      zipcode = i[6]
  return max(b,key=b.get)
  #i = max(b,key=b.get)
  #print b[i]
  """
  Finds the `zipcode` that has the greatest total `bottle_qty` for `category_name` "TEQUILA"
  @param data the output of load_data()
  @return The value of the `zipcode` attribute with the most sales in "TEQUILA" category
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html

  #return -1

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.stderr.write("Usage: python hw2.py (path to input csv)\n")
    sys.exit(1)
  file_path = sys.argv[1]

  data = load_data(file_path)
  print q1(data)
  print q2(data)
  print q3(data)
  print q4(data)
  print q5(data)
