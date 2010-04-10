from m2 import *
from RaceInfo import *


input = SkeletonMale
output = Murloc

inName = input.filename
outName = output.filename

im2 = M2File(inName)
om2 = M2File(outName)



#some bones might be ported also
#but not the bones depending on it	
changeBones = (0,1,2,3)#,4)
#change the anims of the bones :P
def ChangeAnims(i, j):
	diffVec = j.pivot - i.pivot # c = b - a, c is the vector from the bone getting the animations to the bone containg them
	for k in om2.animations:
		for n in im2.animations:
			if (k.animId == n.animId) & (k.subId == n.subId):#if it's the same animation, change the values
			
				if (i.translation.nTimes > k.index) & ( j.translation.nTimes > n.index):
					i.translation.interpolation = j.translation.interpolation#change interpolation values
					i.translation.TimeSubs[k.index] = j.translation.TimeSubs[n.index] #change timestamps
					i.translation.KeySubs[k.index] = j.translation.KeySubs[n.index] #change values
					for v in i.translation.KeySubs[k.index].values:
						v = v - diffVec #translation values should be changed to fit the other bone
						#so it what we do here is: v = v - c 
						#the value gets a new position, relative to the new bone 
				
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
			ChangeAnims(i,j) #change model
			break # no need to check the other bones anymore
		#l shoulder
		if (Dependent(i,om2,output.lshoulder,ic) & Dependent(j,im2,input.lshoulder,jc)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			break
		#r leg
		if (Dependent(i,om2,output.rknee,ic) & Dependent(j,im2,input.rknee,jc)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			break
		#l leg
		if (Dependent(i,om2,output.lknee,ic) & Dependent(j,im2,input.lknee,jc)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			break
			
		#head 
		if (Dependent(i,om2,output.head,ic) & Dependent(j,im2,input.head,jc)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			break
		
		#the other bones

		if (ic== jc) & (ic in changeBones):
			ChangeAnims(i,j)
			#break

		jc += 1
			
	

	ic += 1	

#change also some animations	
for k in om2.animations:
		for n in im2.animations:
			if (k.animId == n.animId) & (k.subId == n.subId):
			#change only the values, which are not model dependent and affect the animation
				k.len = n.len
				k.moveSpeed = n.moveSpeed
				k.flags = n.flags
				k.prob = n.prob
				k.pad = n.pad
				k.unk = n.unk
				k.playSpeed = n.playSpeed

outName = "D:\\makempq\\Character\\Human\\Female\\HumanFemale.m2"			
om2.write(outName)
			