from m2 import *
from animdbc import *
from RaceInfo import *


input = SkeletonMale
output = Murloc

changeBones_I = (0,1,2,3)#,4)
changeBones = { 0: 0,1:1,2:2,3:9}

inName = input.filename
outName = output.filename

im2 = M2File(inName)
om2 = M2File(outName)

canim = int(raw_input("Please insert anim to add: "))
print "Your choice was: " + giveAnimName(canim)

canimId = []
cId = 0

def CheckAnimFile(anim,animfile):
	print animfile
	a_name = output.filename[0:len(output.filename)-3]
	first = str(anim.animId)
	while len(first) < 4:
		first = "0" +first
	scnd  = str(anim.subId)
	while len(scnd) < 2:
		scnd = "0" +scnd
	fname = a_name + first + "-" + scnd + ".anim"
	print (animfile[0],fname)
	return (animfile[0],fname)

def getAnim(canim,sId):
	n = 0
	for i in im2.animations:
		if (i.animId == canim) & (i.subId == sId):
			canimId.append(i.index)
			om2.animations.append(i)
			om2.hdr.animations.count += 1
			pos = len(om2.animations)-1
			om2.animations[pos].index = pos
			apos = len(om2.anim_files)-1
			om2.anim_files.append(CheckAnimFile(i,im2.anim_files[n]))
			if i.next != -1:
				sId += 1
				om2.animations[pos].next = getAnim(canim,sId)
				
			while om2.hdr.anim_lookup.count <= canim:
				om2.hdr.anim_lookup.count +=1
				t = Lookup()
				t.Id = -1
				om2.anim_lookup.append(t)
			t = Lookup()
			t.Id = om2.animations[pos].index
			om2.anim_lookup[canim] = t
			
			return om2.animations[pos].index
			break
		n += 1
		



def AddAnim(i,j):
	diffVec = j.pivot - i.pivot # c = b - a, c is the vector from the bone getting the animations to the bone containg them
	for n in canimId:
		if ( j.translation.nTimes > n):
			i.translation.interpolation = j.translation.interpolation#change interpolation values
			i.translation.nTimes += 1
			i.translation.nKeys += 1
			i.translation.TimeSubs.append(j.translation.TimeSubs[n]) #change timestamps
			i.translation.KeySubs.append(j.translation.KeySubs[n]) #change values
			for v in i.translation.KeySubs[len(i.translation.KeySubs)-1].values:
				v = v - diffVec #translation values should be changed to fit the other bone
			#so it what we do here is: v = v - c 
			#the value gets a new position, relative to the new bone 
		if ( j.rotation.nTimes > n):		
			i.rotation.interpolation = j.rotation.interpolation
			i.rotation.nTimes += 1
			i.rotation.nKeys += 1
			i.rotation.TimeSubs.append(j.rotation.TimeSubs[n])
			i.rotation.KeySubs.append(j.rotation.KeySubs[n])
	
		if ( j.scaling.nTimes > n):			
			i.scaling.interpolation = j.scaling.interpolation
			i.scaling.nTimes += 1
			i.scaling.nKeys += 1
			i.scaling.TimeSubs.append(j.scaling.TimeSubs[n])
			i.scaling.KeySubs.append(j.scaling.KeySubs[n])


#get the depth of a bone
def Depth(bone,file):
	ret = 0
	
	while (bone.parent != -1):
		ret += 1
		bone = file.bones[bone.parent]
		
	return ret
#check if it "hangs" on that bone, or is it	
def Dependent(bone,file,id,ego):
	if ego == id:
		return True
	while (bone.parent != -1):
		if (bone.parent == id):
			return True
		bone = file.bones[bone.parent]
	return False
	
getAnim(canim,0)	
print canimId
ic = 0
for i in om2.bones:

	jc = 0
	for j in im2.bones:
		##########################################################
		#the 5 following blocks define the porting of different  #
		#parts of the anim-skeleton                              #
		##########################################################
		#r shoulder
		if (Dependent(i,om2,output.rshoulder,ic) & Dependent(j,im2,input.rshoulder,jc)) & (Depth(i,om2) == Depth(j,im2)):#check if bone is at the same position on each model
			AddAnim(i,j) #change model
			break # no need to check the other bones anymore
		#l shoulder
		if (Dependent(i,om2,output.lshoulder,ic) & Dependent(j,im2,input.lshoulder,jc)) & (Depth(i,om2) == Depth(j,im2)):
			AddAnim(i,j)
			break
		#r leg
		if (Dependent(i,om2,output.rknee,ic) & Dependent(j,im2,input.rknee,jc)) & (Depth(i,om2) == Depth(j,im2)):
			AddAnim(i,j)
			break
		#l leg
		if (Dependent(i,om2,output.lknee,ic) & Dependent(j,im2,input.lknee,jc)) & (Depth(i,om2) == Depth(j,im2)):
			AddAnim(i,j)
			break
			
		#head 
		if (Dependent(i,om2,output.head,ic) & Dependent(j,im2,input.head,jc)) & (Depth(i,om2) == Depth(j,im2)):
			AddAnim(i,j)
			break
		
		#the other bones
		if (ic in changeBones_I):
			if(changeBones[ic]== jc) :
				AddAnim(i,j)
				break

		jc += 1
			
	

	ic += 1	
	

	
	
outName = "D:\\makempq\\Character\\Human\\Female\\HumanFemale.m2"			
om2.write(outName)