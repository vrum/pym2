from chunk import *
from wmo_root import *


class WMOFile(WoWFile):
	def __init__(self,root = True):
		self.root = root
		self.mver = MVER()
		if(root):
			self.mohd = MOHD()
			self.motx = FilenameChunk(1297044568)
		else:
			pass
			
	
		
	def readData(self,f):
		self.mver.unpack(f)
		if(self.root):
			self.mohd.unpack(f)
			self.motx.unpack(f)
		else:
			pass
			
		
	def writeData(self,f):
		f.write(self.mver.pack())
		if(self.root):
			f.write(self.mohd.pack())
			f.write(self.motx.pack())
		else:
			pass
			
		return f
			
			
r = WMOFile()
r.read("D:\\temp\\wowdaten\\World\\wmo\\cameron.wmo")
r.write("Blah.wmo")
			