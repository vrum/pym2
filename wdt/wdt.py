from chunk import *
from wowfile import *

class MWMO(WChunk):
	def unpackData(self,f):
		self.filename = f.read(self.size)
	def packData(self):	
		#make sure last character is \0!
		if len(self.filename) == 0:
			self.filename = "\0"
		if self.filename[len(self.filename)-1] != "\0":
				self.filename += "\0"
		return self.filename
		
class MODF(WChunk):
	def unpackData(self,f):
		self.index, = struct.unpack("i",f.read(4))
		self.unique, = struct.unpack("i",f.read(4))
		self.position = Vec3().unpack(f)
		self.orientation = Vec3().unpack(f)
		self.minExtends = Vec3().unpack(f)
		self.maxExtends = Vec3().unpack(f)
		self.flags, = struct.unpack("h",f.read(2))
		self.doodadset, = struct.unpack("h",f.read(2))
		self.nameset, = struct.unpack("h",f.read(2))
		self.pad, = struct.unpack("h",f.read(2))
	def packData(self):
		ret = struct.pack("i",self.index)
		ret += struct.pack("i",self.unique)
		ret += self.position.pack()
		ret += self.orientation.pack()
		ret += self.minExtends.pack()
		ret += self.maxExtends.pack()
		ret += struct.pack("h",self.flags)
		ret += struct.pack("h",self.doodadset)
		ret += struct.pack("h",self.nameset)
		ret += struct.pack("h",self.pad)
		return ret

class MPHD(WChunk):
	def unpackData(self,f):
		self.flags, = struct.unpack("i",f.read(4))
		self.data, = struct.unpack("i",f.read(4))
		self.unused = struct.unpack("6i",f.read(6*4))
		
	def packData(self):
		ret = struct.pack("i",self.flags)
		ret += struct.pack("i",self.data)
		for i in range(6):
			ret += struct.pack("i",self.unused[i])
		return ret
		
	def hasTerrain(self):
		if self.flags & 1:
			return False
		else:
			return True
		
	
class MAIN(WChunk):
	class MapEntry:
		def __init__(self):
			self.flags = 0
			self.asyncobject = 0
		def unpack(self,f):
			self.flags, = struct.unpack("i",f.read(4))
			self.asyncobject, = struct.unpack("i",f.read(4))
			return self
		def pack(self):
			ret = struct.pack("i",self.flags)
			ret += struct.pack("i",self.asyncobject)
			return ret
		def isSet(self):
			if self.flags & 1:
				return True
			else:
				return False
		def check(self):
			self.flags &= 1
		def uncheck(self):
			self.flags |= 1
			
	def uncheckTile(self,x,y):
		self.maptiles[x + y*64].uncheck()
	def checkTile(self,x,y):
		self.maptiles[x + y*64].check()
	def hasADT(self,x,y):
		self.maptiles[x + y*64].isSet()
		
	def unpackData(self,f):
		self.maptiles = []
		for i in xrange(4096):
			temp = self.MapEntry().unpack(f)
			self.maptiles.append(temp)
		return self
		
	def packData(self):
		ret = ""
		for i in xrange(4096):
			ret += self.maptiles[i].pack()
		return ret
			


class WDTFile(WoWFile):
		
	def readData(self,f):
		self.mver = MVER().unpack(f)
		self.mphd = MPHD().unpack(f)
		self.main = MAIN().unpack(f)
		if not self.mphd.hasTerrain():
			self.mwmo = MWMO().unpack(f)
			self.modf = MODF().unpack(f)
		print self.mver.version
			
		
	def writeData(self,f):
		f.write(self.mver.pack())
		f.write(self.mphd.pack())
		f.write(self.main.pack())
		if not self.mphd.hasTerrain():
			f.write(self.mwmo.pack())
			f.write(self.modf.pack())
		return f
		
		

wdt = WDTFile().read("AlliancePVPBarracks.wdt")
wdt.write("blah.wdt")