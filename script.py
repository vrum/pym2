
from m2 import *
from skin import *

m2 = M2File("D:\\makempq\\Creature\\Worgen\\Worgen.m2")

for i in range(770, 1629):
	m2.vertices[i].pos.x -= 0.1
	m2.vertices[i].pos.z -= 0.2
	

m2.write("D:\\makempq\\Creature\\Worgen\\Worgen.m2")

