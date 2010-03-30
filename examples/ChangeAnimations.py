from m2 import *

inName = "SkeletonMale.m2"
outName = "HumanFemale.m2"

im2 = M2File(inName)
om2 = M2File(outName)


def ChangeAnims(i, j):
	diffVec = j.pivot - i.pivot
	for k in om2.animations:
		for n in im2.animations:
			if (k.animId == n.animId) & (k.subId == n.subId):
				if (i.translation.nTimes > k.index) & ( j.translation.nTimes > n.index):
					i.translation.interpolation = j.translation.interpolation
					i.translation.TimeSubs[k.index] = j.translation.TimeSubs[n.index]
					i.translation.KeySubs[k.index] = j.translation.KeySubs[n.index]
					for v in i.translation.KeySubs[k.index].values:
						v = v - diffVec
				
				if (i.rotation.nTimes > k.index) & ( j.rotation.nTimes > n.index):
					i.rotation.interpolation = j.rotation.interpolation
					i.rotation.TimeSubs[k.index] = j.rotation.TimeSubs[n.index]
					i.rotation.KeySubs[k.index] = j.rotation.KeySubs[n.index]
				
				if (i.scaling.nTimes > k.index) & ( j.scaling.nTimes > n.index):
					i.scaling.interpolation = j.scaling.interpolation
					i.scaling.TimeSubs[k.index] = j.scaling.TimeSubs[n.index]
					i.scaling.KeySubs[k.index] = j.scaling.KeySubs[n.index]
				

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

#some bones might be ported also	
changeBones = (0,1,2,3,4)
					
ic = 0
for i in om2.bones:
	hasChanged = False	
	jc = 0
	for j in im2.bones:

		#r shoulder
		if (Dependent(i,om2,17,ic) & Dependent(j,im2,11,jc)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			hasChanged = True
			break
		#l shoulder
		if (Dependent(i,om2,16,ic) & Dependent(j,im2,10,jc)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			hasChanged = True
			break
		#r kneee
		if (Dependent(i,om2,5,ic) & Dependent(j,im2,5,jc)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			hasChanged = True
			break
		#l knee
		if (Dependent(i,om2,6,ic) & Dependent(j,im2,6,jc)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			hasChanged = True
			break
			
		#head 
		if (Dependent(i,om2,10,ic) & Dependent(j,im2,9,jc)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			hasChanged = True
			break
		
		#the other bones
		if (ic== jc) & (ic in changeBones):
			print ic
			ChangeAnims(i,j)
			hasChanged = True
			break

		jc += 1
			
	

	ic += 1	

#change also some animations	
for k in om2.animations:
		for n in im2.animations:
			if (k.animId == n.animId) & (k.subId == n.subId):
				k.len = n.len
				k.moveSpeed = n.moveSpeed
				k.flags = n.flags
				k.prob = n.prob
				k.pad = n.pad
				k.unk = n.unk
				k.playSpeed = n.playSpeed

outName = "D:\\makempq\\Character\\Human\\Female\\" + outName			
om2.write(outName)
			