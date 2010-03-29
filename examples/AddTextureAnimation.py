#! /usr/bin/python
from m2 import *
from skin import *

#get the filename and open the files
print "Please insert Filename:"
filename = raw_input()
sname = filename[0:len(filename) -3] + "00.skin"
m2 = M2File(filename)
skin = SkinFile(sname)

#add a global sequence which will be used for the uvanimation
gs = GlobalSequence()
gs.Timestamp = 6667 
m2.gSequ.append(gs)
gsequ = m2.hdr.global_sequences.count #save which global sequence this is for later use
m2.hdr.global_sequences.count += 1

#add renderflags
rf = Renderflags()
rf.flags = 16 #	Disable z-buffer
rf.blend = 4 #	 Combiners_Mod2x 
m2.renderflags.append(rf)
reflag = m2.hdr.render_flags.count#save for later use
m2.hdr.render_flags.count += 1

#add texunit
tu = Lookup()
tu.Id = 1
m2.tex_units.append(tu)
texunit = m2.hdr.tex_units.count#save for later use
m2.hdr.tex_units.count += 1

#add texure
tex = Texture()
tex.flags = 3 #wrap x and y
tex.len_name = 42 # length of the name is 41 + string terminating zero
tex.name = "ITEM\OBJECTCOMPONENTS\WEAPON\HELLFIRE.BLP"
m2.textures.append(tex)
texid = m2.hdr.textures.count#save for lookup
m2.hdr.textures.count += 1
tl = Lookup()
tl.Id = texid
m2.tex_lookup.append(tl)
texlid = m2.hdr.tex_lookup.count#save for later use
m2.hdr.tex_lookup.count += 1


#add uvtranslation
uvanim = UVAnimation()
#create the translation
uvanim.translation.gsequ = gsequ #the texture animation is used globally 
uvanim.translation.interpolation = INTER_LINEAR#interpolate between the values linear

timesub = AnimSub()
timesub.type = DATA_INT
timesub.nEntries = 2
timesub.values.append(0)
timesub.values.append(6667)
uvanim.translation.nTimes = 1
uvanim.translation.TimeSubs.append(timesub)

keysub = AnimSub()
keysub.type = DATA_VEC3
keysub.nEntries = 2
first = Vec3()#start = 0 , 0 , 0
keysub.values.append(first)
second = Vec3()
second.x = -1.0 #end = -1 , 0 , 0 so it's floating xdown
keysub.values.append(second)
uvanim.translation.nKeys = 1
uvanim.translation.KeySubs.append(keysub)

#######
#Note:
#Translation = Vec3()
#Rotation = Quat() (and wow uses Short-Quaternions)
#Scaling = Vec3()
#######

uvlook = Lookup()
uvlook.Id = m2.hdr.uv_anim.count

m2.hdr.uv_anim.count +=1
m2.uv_anim.append(uvanim)
uvan = m2.hdr.uv_anim_lookup.count
m2.hdr.uv_anim_lookup.count += 1
m2.uv_anim_lookup.append(uvlook)


#add new layer to skin, which will contain the texture animation
#and is layed above a existing one
print "To which Submesh shall the UV-Animation be attached?"
subId = int(raw_input())
layer = Material()
layer.submesh = subId
layer.submesh2= subId
layer.mode = 1 # mode 0 appears black, so set it to 1
#here use the saved values
layer.animation = uvan
layer.renderflag = reflag
layer.texunit = texunit
layer.texunit2 = texunit
layer.texture = texlid

skin.texunit.append(layer)
skin.header.TextureUnits.count += 1

#write files
m2.write(filename)
skin.write(sname)
