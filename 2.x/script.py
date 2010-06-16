#! /usr/bin/python

from m2 import *


m2 = M2File("Bear.m2")
for i in m2.animations:
	print ("Start: "+str(i.start))
	print ("End: "+str(i.end))
