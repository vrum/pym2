#! /usr/bin/python
from m2 import *

print "Please insert Modelname:"
filename = raw_input() #get input
m2 = M2File(filename) #open m2
print "Insert Tilting ( 0 = no tilt, 1 = x-tilt, 2 = y-tilt, 3 = xy-tilt)"
tilt = int(raw_input())
m2.hdr.modeltype |= tilt #non-exclusive or: 001010 | 010001 = 011011
m2.write(filename)