#!/usr/bin/python
#Example:
# > python checkno.py test.txt

import sys

filename = sys.argv[1]
with open(filename, 'r') as myfile:
        data = myfile.read()

data2 = data.split("\n\n")

for i in data2:
       count += 1
       for x in numbers:
               if x == str(count):
                       print "\n"
                       print i
