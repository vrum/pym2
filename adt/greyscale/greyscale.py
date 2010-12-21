from adt import *
import pngcanvas

def floatToColor(val):
	'''temp = (val * 0xFFFFFFFF - 0xFFFFFFFF if(val > 0)  else val * 0xFFFFFFFF + 0xFFFFFFFF)
	temp = int(temp/0xFFFFFFFF)
	color = []
	color.append(temp << 24)
	color.append(temp << 16)	
	color.append(temp << 8)	
	color.append(temp)'''
	temp = (val * 255 - 255 if(val > 0)  else val * 255 + 255)
	temp = int(temp/255)
	color = []
	color.append(0)	
	color.append(0)		
	color.append(0)	
	color.append(temp)
	return 	color

adt = ADTFile()
filename = raw_input("Please insert filename:\n")
adt.read(filename)
	

p = pngcanvas.PNGCanvas(144,144)
p.color = [0,0,0,0xff]
offsx = 0
offsy = 0
for i in range(16):
	for j in range(16):
		offsx = 9*j
		offsy = 9*i
		aposz = adt.mcnk[j*16+i].pos.z
		for x in range(9):
			for z in range(9):
				p.filledRectangle(offsx,offsy,offsx,offsy,floatToColor(adt.mcnk[j*16+i].mcvt.entries[x+9*z+8*z].value+aposz))
				offsx += 1
			offsy += 1
			offsx = 9*j

print offsx
print offsy
f = open(filename+".png", "wb")
f.write(p.dump())
f.close()
