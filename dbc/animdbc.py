
from DBCFile import *
		
class AnimEntry:
	def __init__(self):
		pass
	def unpack(self,f,stringoffset):
		self.Id,	= ReadInt(f)
		self.ofsName,	= ReadInt(f)
		self.Name = ReadString(f,stringoffset,self.ofsName)
		self.WeaponSt,	= ReadInt(f)
		self.Flags,	= ReadInt(f)
		self.Unk,	= ReadInt(f)
		self.Preceding,	= ReadInt(f)
		self.RealId,	= ReadInt(f)
		self.Group,	= ReadInt(f)
		return self

filename = "AnimationData.dbc"
animdbc = DBC(filename,AnimEntry)

def giveAnimName(id):
	for i in animdbc.entries:
		if i.Id == id:
			return i.Name
	return "Not Found oO"