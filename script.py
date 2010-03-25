
from m2 import *


filename = "Wisp.m2"
m2 = M2File(filename )
for i in m2.particle_emitters:
	for j in i.color.Keys:
		j.x = 0 #red
		j.y = 255 #green
		j.z = 0 # blue
m2.write(filename)

	


	
