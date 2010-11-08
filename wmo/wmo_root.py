from chunk import *
from wowfile import *

class MOHD(WChunk):
	def __init__(self):
		self.magic = 1297041476
		self.size = 0
		self.nTextures = 0
		self.nGroups = 0
		self.nPortals = 0
		self.nLights = 0
		self.nModels = 0
		self.nDoodads = 0
		self.nSets = 0
		self.ambCol = 0
		self.wmoId = 0
		self.bb1 = Vec3()
		self.bb2 = Vec3()
		self.liquid = 0
	
	def unpackData(self,f):
		self.nTextures, = struct.unpack("i",f.read(4))
		self.nGroups, = struct.unpack("i",f.read(4))
		self.nPortals, = struct.unpack("i",f.read(4))
		self.nLights, = struct.unpack("i",f.read(4))
		self.nModels, = struct.unpack("i",f.read(4))
		self.nDoodads, = struct.unpack("i",f.read(4))
		self.nSets, = struct.unpack("i",f.read(4))
		self.ambCol, = struct.unpack("i",f.read(4))
		self.wmoId, = struct.unpack("i",f.read(4))
		self.bb1.unpack(f)
		self.bb2.unpack(f)
		self.liquid, = struct.unpack("i",f.read(4))
	
	def packData(self):
		ret = struct.pack("i",self.nTextures)
		ret += struct.pack("i",self.nGroups)
		ret += struct.pack("i",self.nPortals)
		ret += struct.pack("i",self.nLights)
		ret += struct.pack("i",self.nModels)
		ret += struct.pack("i",self.nDoodads)
		ret += struct.pack("i",self.nSets)
		ret += struct.pack("i",self.ambCol)
		ret += struct.pack("i",self.wmoId)
		ret += self.bb1.pack()
		ret += self.bb2.pack()
		ret += struct.pack("i",self.liquid)
		return ret


		

			
		