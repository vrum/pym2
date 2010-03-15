#example script
from m2 import *

f = open("HumanMale.m2","r+b")
hdr = M2Header(f)

tex = []
f.seek(hdr.textures.offset,SEEK_SET)
for i in range(hdr.textures.count):
	temp = Texture(f)
	print temp.name
	tex.append(temp)
	

anims = []
f.seek(hdr.animations.offset,SEEK_SET)
for i in range(hdr.animations.count):
	temp = Sequ(f)
	anims.append(temp)

look = []	
f.seek(hdr.anim_lookup.offset,SEEK_SET)
for i in range(hdr.anim_lookup.count):
	temp = struct.unpack("h",f.read(2))
	look.append(temp)
	
#fix animindices
c = 0	
for i in anims:
	i.index = c;
	c+=1;

c = 0
for i in look:
	i = -1
	for a in anims:
		if (a.animId == c):
			i = c
	c+=1;
	
f.seek(0,SEEK_END)
FillLine(f)
ofs = f.tell()
hdr.animations.offset = ofs
for i in anims:
	t = i.pack()
	f.write(t)
	
f.seek(0,SEEK_END)
FillLine(f)
ofs = f.tell()
hdr.anim_lookup.offset = ofs
for i in look:
	t = struct.pack("h",i[0])
	f.write(t)	
	
f.seek(0,SEEK_SET)
t = hdr.pack()
f.write(t)
	