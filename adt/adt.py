from chunk import *
from adt_chunks import *


class ADTFile(WoWFile):
	def __init__(self):
		self.mver = MVER()
		self.mhdr = MHDR()
		self.mcin = EntryChunk(1296255310, MCINEntry)
		self.mtex = FilenameChunk(1297368408)
		self.mmdx = FilenameChunk(1296909400)
		self.mmid = EntryChunk(1296910660, Reference)
		self.mwmo = FilenameChunk(1297567055)
		self.mwid = EntryChunk(1297566020, Reference)
		self.mddf = EntryChunk(1296319558, MDDFEntry)
		self.modf = EntryChunk(1297040454, MODFEntry)
		self.mh2o = WChunk()
		self.mcnk = []
		self.mfbo = WChunk()
		self.mtfx = EntryChunk(1297368664, Reference)
		
	def readData(self,f):
		self.mver.unpack(f)
		self.mhdr.unpack(f)
		self.mcin.unpack(f)
		self.mtex.unpack(f)
		self.mmdx.unpack(f)
		self.mmid.unpack(f)
		self.mwmo.unpack(f)
		self.mwid.unpack(f)
		self.mddf.unpack(f)
		self.modf.unpack(f)
		if(self.mhdr.ofsMH2O != 0):
			self.mh2o.unpack(f)
		for i in range(256):
			self.mcnk.append(MCNK().unpack(f))
		if(self.mhdr.ofsMFBO != 0):
			self.mfbo.unpack(f)
		if(self.mhdr.ofsMTFX != 0):
			self.mtfx.unpack(f)
		
		
	def writeData(self,f): #0x14 = MVER,0x40 = MHDR,  0x1008 = MCIN
		ret1 = self.mver.pack()
		ret = ""
		self.mhdr.ofsMCIN = 0x40 + len(ret)
		self.mhdr.ofsMTEX = 0x40 + 0x1008 + len(ret)
		ret += self.mtex.pack()
		self.mhdr.ofsMMDX = 0x40 + 0x1008 + len(ret)
		ret += self.mmdx.pack()
		self.mhdr.ofsMMID = 0x40 + 0x1008 + len(ret)
		ret += self.mmid.pack()
		self.mhdr.ofsMWMO = 0x40 + 0x1008 + len(ret)
		ret += self.mwmo.pack()
		self.mhdr.ofsMWID = 0x40 + 0x1008 + len(ret)
		ret += self.mwid.pack()
		self.mhdr.ofsMDDF = 0x40 + 0x1008 + len(ret)
		ret += self.mddf.pack()
		self.mhdr.ofsMODF = 0x40 + 0x1008 + len(ret)
		ret += self.modf.pack()
		if(self.mhdr.ofsMH2O != 0):
			self.mhdr.ofsMH2O = 0x40 + 0x1008 + len(ret)
			ret += self.mh2o.pack()
		for i in range(256):
			self.mcin.entries[i].ofsMCNK = 0x14 + 0x40 + 0x1008 + len(ret)
			ret += self.mcnk[i].pack()
			self.mcin.entries[i].sizeMCNK = len(ret) - self.mcin.entries[i].ofsMCNK
		ret = self.mcin.pack() + ret
		if(self.mhdr.ofsMFBO != 0):
			self.mhdr.ofsMFBO = 0x40  + len(ret)
			ret += self.mfbo.pack()
		if(self.mhdr.ofsMTFX != 0):
			self.mhdr.ofsMTFX = 0x40  + len(ret)
			ret += self.mtfx.pack()	
		ret1 += self.mhdr.pack()			
		f.write(ret1)
		f.write(ret)
		return f
		
adt = ADTFile()
adt.read("Kalimdor_1_1..adt")
for i in adt.mcnk:
	for j in i.mcly.entries:
		j.flags |= 0x4
		j.flags |= 0x20
		j.flags |= 0x40
		j.flags |= 0x80
		j.flags |= 0x400
adt.write("Kalimdor_1_1.adt")
