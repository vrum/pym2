from DBCFile import *

class FactionEntry(DBCEntry):
	def __init__(self):
		self.Id = 0
		self.GainId = 0
		self.AtWar = 0
		self.Allied = 0
		self.Unk1 = 0
		self.Unk2 = 0
		self.Unk3 = 0
		self.Unk4 = 0
		self.Unk5 = 0
		self.Unk6 = 0
		self.BasRep = 0
		self.Mod1 = 0
		self.Mod2 = 0
		self.Mod3 = 0
		self.Con1 = 0
		self.Con2 = 0
		self.Con3 = 0
		self.Con4 = 0
		self.Parent = 0
		self.Name = DBCLoc()
		self.Description = DBCLoc()
	def __module__(self):
		pass
	def __doc__(self):
		pass
	def unpack(self,f,sDict):
		self.Id,		= ReadInt(f)
		self.GainId,		= ReadInt(f)
		self.AtWar,		= ReadInt(f)
		self.Allied,		= ReadInt(f)
		self.Unk1,		= ReadInt(f)
		self.Unk2,		= ReadInt(f)
		self.Unk3,		= ReadInt(f)
		self.Unk4,		= ReadInt(f)
		self.Unk5,		= ReadInt(f)
		self.Unk6,		= ReadInt(f)
		self.BasRep,		= ReadInt(f)
		self.Mod1,		= ReadInt(f)
		self.Mod2,		= ReadInt(f)
		self.Mod3,		= ReadInt(f)
		self.Con1,		= ReadInt(f)
		self.Con2,		= ReadInt(f)
		self.Con3,		= ReadInt(f)
		self.Con4,		= ReadInt(f)
		self.Parent,		= ReadInt(f)
		self.Name		= DBCLoc().unpack(f,sDict)
		self.Description	= DBCLoc().unpack(f,sDict)
		return self

		
factiondbc = DBC("Faction.dbc",FactionEntry)
factiondbc.write("Blah.dbc")
print factiondbc.entries[20].Name.Languages[3]
