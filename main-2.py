#file => a document that contains data, store

#file handling => storing, organizing data, manipulating,

# __MODE__

#reading (r) => reading the contents of a file

#write (w) => replaces everything in the doc

#append(a) => adds more

#create(x) => creates a new file

# file = open("example.py", "r")

file = open("zain.txt", "r")


with open("zain.txt","r"):
  lines= file.readlines()
  for line in lines:
     word =line.split()
     print(word)
 

with open("zain.txt", "a" ) as f:
 f.write(" \n  i wold never hate learning ")