from chunk import *
from wowfile import *

class MHDR(WChunk):
	def __init__(self):
		self.flags = 0
		self.ofsMCIN = 0
		self.ofsMTEX = 0
		self.ofsMMDX = 0
		self.ofsMMID = 0
		self.ofsMWMO = 0
		self.ofsMWID = 0
		self.ofsMDDF = 0
		self.ofsMODF = 0
		self.ofsMFBO = 0
		self.ofsMH2O = 0
		self.ofsMTFX = 0
		self.pad1 = 0
		self.pad2 = 0
		self.pad3 = 0
		self.pad4 = 0
		
	def unpackData(self,f):	
		self.flags, = struct.unpack("i",f.read(4))
		self.ofsMCIN, = struct.unpack("i",f.read(4))
		self.ofsMTEX, = struct.unpack("i",f.read(4))
		self.ofsMMDX, = struct.unpack("i",f.read(4))
		self.ofsMMID, = struct.unpack("i",f.read(4))
		self.ofsMWMO, = struct.unpack("i",f.read(4))
		self.ofsMWID, = struct.unpack("i",f.read(4))
		self.ofsMDDF, = struct.unpack("i",f.read(4))
		self.ofsMODF, = struct.unpack("i",f.read(4))
		self.ofsMFBO, = struct.unpack("i",f.read(4))
		self.ofsMH2O, = struct.unpack("i",f.read(4))
		self.ofsMTFX, = struct.unpack("i",f.read(4))
		self.pad1, = struct.unpack("i",f.read(4))
		self.pad2, = struct.unpack("i",f.read(4))
		self.pad3, = struct.unpack("i",f.read(4))
		self.pad4, = struct.unpack("i",f.read(4))
		
	def packData(self):
		ret = struct.pack("i", self.flags)
		ret += struct.pack("i", self.ofsMCIN)
		ret += struct.pack("i", self.ofsMTEX)
		ret += struct.pack("i", self.ofsMMDX)
		ret += struct.pack("i", self.ofsMMID)
		ret += struct.pack("i", self.ofsMWMO)
		ret += struct.pack("i", self.ofsMWID)
		ret += struct.pack("i", self.ofsMDDF)
		ret += struct.pack("i", self.ofsMODF)
		ret += struct.pack("i", self.ofsMFBO)
		ret += struct.pack("i", self.ofsMH2O)
		ret += struct.pack("i", self.ofsMTFX)
		ret += struct.pack("i", self.pad1)
		ret += struct.pack("i", self.pad2)
		ret += struct.pack("i", self.pad3)
		ret += struct.pack("i", self.pad4)
		return ret
		
		
class MCINEntry:
	entrySize = 16
	def __init__(self):
		self.ofsMCNK = 0
		self.sizeMCNK = 0
		self.flags = 0
		self.aId = 0
	def unpack(self,f):
		self.ofsMCNK, = struct.unpack("i", f.read(4))
		self.sizeMCNK, = struct.unpack("i", f.read(4))
		self.flags, = struct.unpack("i", f.read(4))
		self.aId, = struct.unpack("i", f.read(4))
		return self
		
	def pack(self):
		ret = struct.pack("i", self.ofsMCNK)
		ret += struct.pack("i", self.sizeMCNK)
		ret += struct.pack("i", self.flags)
		ret += struct.pack("i", self.aId)
		return ret