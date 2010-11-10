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
		self.ambCol = Color()
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
		self.ambCol.unpack(f)
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
		ret += self.ambCol.pack()
		ret += struct.pack("i",self.wmoId)
		ret += self.bb1.pack()
		ret += self.bb2.pack()
		ret += struct.pack("i",self.liquid)
		return ret


		

			
class MOMTEntry:
	entrySize = 64
	def __init__(self):
		self.flags1 = 0
		self.specMode = 0
		self.blendMode = 0
		self.texture1 = 0
		self.color1 = Color()
		self.texflags1 = 0
		self.texture2 = 0
		self.color2 = Color()
		self.texflags2 = 0
		self.color3 = Color()
		self.unk = [0,0,0,0]
		self.texobj1 = 0
		self.texobj2 = 0
			
	def unpack(self,f):
		self.flags1, = struct.unpack("i",f.read(4))
		self.specMode, = struct.unpack("i",f.read(4))
		self.blendMode, = struct.unpack("i",f.read(4))
		self.texture1, = struct.unpack("i",f.read(4))
		self.color1.unpack(f)
		self.texflags1, = struct.unpack("i",f.read(4))
		self.texture2, = struct.unpack("i",f.read(4))
		self.color2.unpack(f)		
		self.texflags2, = struct.unpack("i",f.read(4))
		self.color3.unpack(f)
		self.unk[0], = struct.unpack("i",f.read(4))
		self.unk[1], = struct.unpack("i",f.read(4))
		self.unk[2], = struct.unpack("i",f.read(4))
		self.unk[3], = struct.unpack("i",f.read(4))
		self.texobj1, = struct.unpack("i",f.read(4))
		self.texobj2, = struct.unpack("i",f.read(4))
		return self
		
	def pack(self):
		ret = struct.pack("i",self.flags1)
		ret += struct.pack("i",self.specMode)
		ret += struct.pack("i",self.blendMode)
		ret += struct.pack("i",self.texture1)
		ret += self.color1.pack()
		ret += struct.pack("i",self.texflags1)
		ret += struct.pack("i",self.texture2)
		ret += self.color2.pack()
		ret += struct.pack("i",self.texflags2)
		ret += self.color3.pack()
		ret += struct.pack("4i",self.unk[0],self.unk[1],self.unk[2],self.unk[3])
		ret += struct.pack("i",self.texobj1)
		ret += struct.pack("i",self.texobj2)
		return ret
		

	
class MOGIEntry:
	entrySize = 32
	def __init__(self):
		self.flags = 0
		self.minExtends = Vec3()
		self.maxExtends = Vec3()
		self.name = 0
		
	def unpack(self,f):
		self.flags, = struct.unpack("i",f.read(4))
		self.minExtends.unpack(f)
		self.maxExtends.unpack(f)
		self.name, = struct.unpack("i",f.read(4))
		return self
		
	def pack(self):
		ret = struct.pack("i",self.flags)
		ret += self.minExtends.pack()
		ret += self.maxExtends.pack()
		ret += struct.pack("i",self.name)
		return ret