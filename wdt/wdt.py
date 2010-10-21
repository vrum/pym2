from chunk import *
from wowfile import *

class MWMO(WChunk):
	def __init__(self):
		self.magic = 1297567055
		self.size = 0
		self.filename = "\0"
	def unpackData(self,f):
		self.filename = f.read(self.size)
	def packData(self):	
		#make sure last character is \0!
		if len(self.filename) == 0:
			self.filename = "\0"
		if self.filename[len(self.filename)-1] != "\0":
				self.filename += "\0"
		return self.filename
	def setFilename(self,name):
		self.filename = name
	def getFilename(self):
		return self.filename
		
class MODF(WChunk):
	class WmoEntry:
		def __init__(self):
			self.index = 0
			self.unique = 0
			self.position = Vec3()
			self.orientation = Vec3()
			self.minExtends = Vec3()
			self.maxExtends = Vec3()
			self.flags = 0
			self.doodadset = 0
			self.nameset = 0
			self.pad = 0
			
		def unpack(self,f):
			self.index, = struct.unpack("i",f.read(4))
			self.unique, = struct.unpack("i",f.read(4))
			self.position.unpack(f)
			self.orientation.unpack(f)
			self.minExtends.unpack(f)
			self.maxExtends.unpack(f)
			self.flags, = struct.unpack("h",f.read(2))
			self.doodadset, = struct.unpack("h",f.read(2))
			self.nameset, = struct.unpack("h",f.read(2))
			self.pad, = struct.unpack("h",f.read(2))
			return self
			
		def pack(self):
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
			
		def setPosition(self,pos):
			self.position = pos
			
		def setOrientation(self,ori):
			self.orientation = ori
			
		def getPosition(self):
			return self.position
			
		def getOrientation(self):
			return self.orientation
			
		def setFlags(self,flags):
			self.flags = flags
			
		def setDoodadSet(self,dds):
			self.doodadset = dds
			
		def setNameSet(self,nms):
			self.nameset = nms
			
		def setIndex(self,ind):
			self.index = ind
		
	def __init__(self):
		self.magic = 1297040454
		self.size = 0
		self.nEntries = 0
		self.entries = []
		
	def unpackData(self,f):
		self.nEntries = self.size / 64
		for i in xrange(self.nEntries):
			self.entries.append(self.WmoEntry().unpack(f))
			
	def packData(self):
		ret = ""
		for i in xrange(self.nEntries):
			ret += self.entries[i].pack()
		return ret
	def addEntry(self):
		self.nEntries += 1
		self.entries.append(self.WmoEntry())
		
	def setEntryPosition(self,entry,pos):
		try:
			self.entries[entry].setPosition(pos)
		except:
			print "Entry not found"
			
	def getEntryPosition(self,entry):
		try:
			return self.entries[entry].getPosition()
		except:
			print "Entry not found"
			
	def setEntryOrientation(self,entry,ori):
		try:
			self.entries[entry].setOrientation(ori)
		except:
			print "Entry not found"
	def getEntryOrientation(self,entry):
		try:
			return self.entries[entry].getOrientation()
		except:
			print "Entry not found"

class MPHD(WChunk):
	def __init__(self):
		self.magic = 1297107012
		self.size = 0
		self.flags = 0
		self.data = 0
		self.unused = [0,0,0,0,0,0]
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
	def setTerrain(self):
		self.flags &= 14		
	def unsetTerrain(self):
		self.flags |= 1
		
	def hasBigAlpha(self):
		if self.flags & 4:
			return True
		else:
			return False
	def setBigAlpha(self):
		self.flags |= 4
	def unsetBigAlpha(self):
		self.flags &= 11
		
	def hasVertexShading(self):
		if self.flags & 2:
			return True
		else:
			return False
	def setVertexShading(self):
		self.flags |= 2
	def unsetVertexShading(self):
		self.flags &= 13
	
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
			self.flags |= 1
		def uncheck(self):
			self.flags = 0
		
	def __init__(self):
		self.magic = 1296124238
		self.size = 0
		self.maptiles = []		
		for i in xrange(4096):
			temp = self.MapEntry()
			self.maptiles.append(temp)
			
	def uncheckTile(self,x,y):
		self.maptiles[x + y*64].uncheck()
		
	def checkTile(self,x,y):
		self.maptiles[x + y*64].check()
		
	def hasADT(self,x,y):
		return self.maptiles[x + y*64].isSet()
		
	def unpackData(self,f):
		for i in xrange(4096):
			self.maptiles[i].unpack(f)
		return self
		
	def packData(self):
		ret = ""
		for i in xrange(4096):
			ret += self.maptiles[i].pack()
		return ret
			


class WDTFile(WoWFile):
	def __init__(self):
		self.mver = MVER()
		self.mphd = MPHD()
		self.main = MAIN()
		self.mwmo = MWMO()
		self.modf = MODF()
		
	def readData(self,f):
		self.mver.unpack(f)
		self.mphd.unpack(f)
		self.main.unpack(f)
		if not self.mphd.hasTerrain():
			self.mwmo.unpack(f)
			self.modf.unpack(f)
		print self.mver.version
			
		
	def writeData(self,f):
		f.write(self.mver.pack())
		f.write(self.mphd.pack())
		f.write(self.main.pack())
		if not self.mphd.hasTerrain():
			f.write(self.mwmo.pack())
			f.write(self.modf.pack())
		return f
		
	def checkTile(self,x,y):
		self.main.checkTile(x,y)
		
	def uncheckTile(self,x,y):
		self.main.uncheckTile(x,y)
		
	def setTerrain(self):
		self.mphd.setTerrain()
		
	def unsetTerrain(self):
		self.mphd.unsetTerrain()
		
	def setBigAlpha(self):
		self.mphd.setBigAlpha()
		
	def unsetBigAlpha(self):
		self.mphd.unsetBigAlpha()
		
	def setVertexShading(self):
		self.mphd.setVertexShading()
		
	def unsetVertexShading(self):
		self.mphd.unsetVertexShading()
		
	def setWMOName(self,name):
		self.mwmo.setFilename(name)
	def getWMOName(self):
		if not self.mphd.hasTerrain():
			return self.mwmo.getFilename()
		else:
			return ""
		
	def getWMOPosition(self):
		if not self.mphd.hasTerrain():
			return self.modf.getEntryPosition(0)
		else:
			return Vec3()
		
	def setWMOPosition(self,pos):
		pass
		
	def getWMOOrientation(self):
		if not self.mphd.hasTerrain():
			return self.modf.getEntryPosition(0)
		else:
			return Vec3()
		
	def setWMOOrientation(self,ori):
		pass
		
'''
wdt = WDTFile()#.read("AlliancePVPBarracks.wdt")
wdt.mphd.unsetTerrain()
wdt.mphd.setTerrain()
wdt.checkTile(0,0)
wdt.write("blah.wdt")
'''