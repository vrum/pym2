from chunk import *
from wmo_root import *


class WMOFile(WoWFile):
	def __init__(self,root = True):
		self.root = root
		self.mver = MVER()
		if(root):
			self.mohd = MOHD()
			self.motx = FilenameChunk(1297044568)
			self.momt = EntryChunk(1297042772,MOMTEntry)
			self.mogn = FilenameChunk(1297041230)
			self.mogi = EntryChunk(1297041225, MOGIEntry)
			self.mosb = WChunk()
			self.mopv = WChunk()
			self.mopt = WChunk()
			self.mopr = WChunk()
			self.movv = WChunk()
			self.movb = WChunk()
			self.molt = WChunk()
			self.mods = WChunk()
			self.modn = FilenameChunk(1297040462)
			self.modd = WChunk()
			self.mfog = WChunk()
		else:
			pass
			
	
		
	def readData(self,f):
		self.mver.unpack(f)
		if(self.root):
			self.mohd.unpack(f)
			self.motx.unpack(f)
			self.momt.unpack(f)
			self.mogn.unpack(f)
			self.mogi.unpack(f)
			self.mosb.unpack(f)
			self.mopv.unpack(f)
			self.mopt.unpack(f)
			self.mopr.unpack(f)
			self.movv.unpack(f)
			self.movb.unpack(f)
			self.molt.unpack(f)
			self.mods.unpack(f)
			self.modn.unpack(f)
			self.modd.unpack(f)
			self.mfog.unpack(f)
		else:
			pass
			
		
	def writeData(self,f):
		f.write(self.mver.pack())
		if(self.root):
			f.write(self.mohd.pack())
			f.write(self.motx.pack())
			f.write(self.momt.pack())
			f.write(self.mogn.pack())
			f.write(self.mogi.pack())
			f.write(self.mosb.pack())
			f.write(self.mopv.pack())
			f.write(self.mopt.pack())
			f.write(self.mopr.pack())
			f.write(self.movv.pack())
			f.write(self.movb.pack())
			f.write(self.molt.pack())
			f.write(self.mods.pack())
			f.write(self.modn.pack())
			f.write(self.modd.pack())
			f.write(self.mfog.pack())
		else:
			pass
			
		return f
			
			
r = WMOFile()
r.read("D:\\temp\\wowdaten\\World\\wmo\\cameron.wmo")
r.write("Blah.wmo")
			