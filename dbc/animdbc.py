
from DBCFile import *
		
class AnimEntry(DBCEntry):
	def __init__(self):
		self.Id		= 0
		self.Name	= ''
		self.WeaponSt	= 0
		self.Flags	= 0
		self.Unk	= 0
		self.Preceding	= 0
		self.RealId	= 0
		self.Group	= 0
		
	def __module__(self):
		pass
	def __doc__(self):
		pass
	def unpack(self,f,sDict):
		self.Id,	= ReadInt(f)
		ofsName,	= ReadInt(f)
		self.Name	= sDict[ofsName]
		self.WeaponSt,	= ReadInt(f)
		self.Flags,	= ReadInt(f)
		self.Unk,	= ReadInt(f)
		self.Preceding,	= ReadInt(f)
		self.RealId,	= ReadInt(f)
		self.Group,	= ReadInt(f)
		return self

filename = "AnimationData.dbc"
animdbc = DBC(filename,AnimEntry)
print animdbc.entries[0].Name
a = AnimEntry()
a.Id = 512
a.Name = "Lolling"
a.WeaponSt = 123
a.RealId = 512
a.Group = 2
animdbc.AddEntry(a)

animdbc.write("Blah.dbc")

def giveAnimName(id):
	for i in animdbc.entries:
		if i.Id == id:
			return i.Name
	return "Not Found oO"
	



	