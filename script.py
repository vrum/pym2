#example script
from m2 import *
from skin import *

m2 = M2File("Wisp.m2")#open m2
for i in m2.textures:#iterate through textures
	print i.name#print each texture name
	
m2.write("Wisp.m2")
	


f = open("HumanMale.m2","r+b")#open HumanMale.m2 with binary read and write support
hdr = M2Header(f)#read header


anims = []
f.seek(hdr.animations.offset,SEEK_SET)
for i in range(hdr.animations.count):
	temp = Sequ(f)
	anims.append(temp)

look = []	
f.seek(hdr.anim_lookup.offset,SEEK_SET)#lookuptable
for i in range(hdr.anim_lookup.count):
	temp = struct.unpack("h",f.read(2))#read int16
	look.append(temp)
	
#fix animindices
c = 0	
for i in anims:#iterate through animations
	i.index = c;#give the index the position
	c+=1;

c = 0
for i in look:#iterate through the lookup table
	i = -1#if no animation has that index set to -1
	for a in anims:#check all animations
		if (a.animId == c):#if one has the correct animId
			i = c#assign it to that lookup
	c+=1;
	
f.seek(0,SEEK_END)#go to the end of the file
FillLine(f)#pad to 16
ofs = f.tell()#get the new offset
hdr.animations.offset = ofs#set the header offset
for i in anims:
	t = i.pack()#pack the data
	f.write(t)#write to file
	
f.seek(0,SEEK_END)
FillLine(f)
ofs = f.tell()
hdr.anim_lookup.offset = ofs
for i in look:
	t = struct.pack("h",i[0])
	f.write(t)	
	
f.seek(0,SEEK_SET)#go to the start of the file
t = hdr.pack()#pack the header
f.write(t)#rewrite the header
	