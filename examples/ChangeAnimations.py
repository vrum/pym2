from m2 import *

inName = "NightElfFemale.m2"
outName = "HumanFemale.m2"

im2 = M2File(inName)
om2 = M2File(outName)


def ChangeAnims(i, j):
	for k in om2.animations:
		for n in im2.animations:
			if (k.animId == n.animId) & (k.subId == n.subId):
				if (i.translation.interpolation != 0) & (j.translation.interpolation != 0) & (i.translation.nTimes > k.index) & ( j.translation.nTimes > n.index):
					i.translation.TimeSubs[k.index] = j.translation.TimeSubs[n.index]
					i.translation.KeySubs[k.index] = j.translation.KeySubs[n.index]

				if (i.rotation.interpolation != 0) & (j.rotation.interpolation != 0)& (i.rotation.nTimes > k.index) & ( j.rotation.nTimes > n.index):
					i.rotation.TimeSubs[k.index] = j.rotation.TimeSubs[n.index]
					i.rotation.KeySubs[k.index] = j.rotation.KeySubs[n.index]
				if (i.scaling.interpolation != 0) & (j.scaling.interpolation != 0)& (i.scaling.nTimes > k.index) & ( j.scaling.nTimes > n.index):
					i.scaling.TimeSubs[k.index] = j.scaling.TimeSubs[n.index]
					i.scaling.KeySubs[k.index] = j.scaling.KeySubs[n.index]


def Depth(bone,file):
	ret = 0
	
	while (bone.parent != -1):
		ret += 1
		bone = file.bones[bone.parent]
		
	return ret
	
def Dependent(bone,file,id):
	while (bone.parent != -1):
		if (bone.parent == id):
			return True
		bone = file.bones[bone.parent]
	return False
					

for i in om2.bones:
	for j in im2.bones:
		#if (i.unk == j.unk):
		#	ChangeAnims(i,j)
		#	break
		#r shoulder
		if (Dependent(i,om2,22) & Dependent(j,im2,22)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			break
		#l shoulder
		if (Dependent(i,om2,21) & Dependent(j,im2,21)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			break
		#r kneee
		if (Dependent(i,om2,5) & Dependent(j,im2,8)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			break
		#l knee
		if (Dependent(i,om2,6) & Dependent(j,im2,7)) & (Depth(i,om2) == Depth(j,im2)):
			ChangeAnims(i,j)
			break
		

			
om2.write(outName)
			