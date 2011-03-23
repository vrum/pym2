from chunk import *
from wowfile import *

MCNK_HAS_SHADOWS = 0x1
MCNK_IMPASSABLE = 0x2
MCNK_RIVER = 0x4
MCNK_OCEAN = 0x8
MCNK_MAGMA = 0x10
MCNK_SLIME = 0x20
MCNK_HAS_VERTEX_COLORS = 0x40
MCNK_TBC = 0x8000

bitmap = [0x1, 0x2 ,0x4 ,0x8 ,0x10 ,0x20 ,0x40 ,0x80]

class MHDR(WChunk):
	def __init__(self):
		self.magic = 0
		self.size = 0
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
		
class MODFEntry:
	entrySize = 64
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
		
	def getFlags(self):
		return self.flags
		
	def setUnique(self, uId):
		self.unique = uId
		
	def getUnique(self):
		return self.unique
			
	def setIndex(self,ind):
		self.index = ind
		
	def getIndex(self):
		return self.index
			
	def setDoodadSet(self,dds):
		self.doodadset = dds
		
	def getDoodadSet(self):
		return self.doodadset
			
	def setNameSet(self,nms):
		self.nameset = nms
		
	def getNameSet(self):
		return self.nameset
		
class MDDFEntry:
	entrySize = 36
	def __init__(self):
		self.index = 0
		self.unique = 0
		self.position = Vec3()
		self.rotation = Vec3()
		self.scale = 0
		self.flags = 0
			
	def unpack(self,f):
		self.index, = struct.unpack("i",f.read(4))
		self.unique, = struct.unpack("i",f.read(4))
		self.position.unpack(f)
		self.rotation.unpack(f)
		self.scale, = struct.unpack("h",f.read(2))
		self.flags, = struct.unpack("h",f.read(2))
		return self
		
	def pack(self):
		ret = struct.pack("i",self.index)
		ret += struct.pack("i",self.unique)
		ret += self.position.pack()
		ret += self.rotation.pack()
		ret += struct.pack("h",self.scale)
		ret += struct.pack("h",self.flags)
		return ret
		
	def setPosition(self,pos):
		self.position = pos
			
	def setRotation(self,rot):
		self.rotation = rot
			
	def getPosition(self):
		return self.position
			
	def getRotation(self):
		return self.rotation
			
	def setFlags(self,flags):
		self.flags = flags
		
	def getFlags(self):
		return self.flags
		
	def setUnique(self, uId):
		self.unique = uId
		
	def getUnique(self):
		return self.unique
			
	def setIndex(self,ind):
		self.index = ind
		
	def getIndex(self):
		return self.index
		
	def setScale(self, scale):
		self.scale = scale
	
	def getScale(self):
		return self.scale
		
		
class MCNK(WChunk):
	def __init__(self):
		self.magic = 0
		self.size = 0
		self.flags = 0
		self.indexX = 0
		self.indexY = 0
		self.nLayers = 0
		self.nDoodadRefs = 0
		self.ofsMCVT = 0
		self.ofsMCNR = 0
		self.ofsMCLY = 0
		self.ofsMCRF = 0
		self.ofsMCAL = 0
		self.sizeMCAL = 0
		self.ofsMCSH = 0
		self.sizeMCSH = 0
		self.areaId = 0
		self.nMapObjRefs = 0
		self.holes = 0
		self.lowQualTexMap = [0,0,0,0,0,0]
		self.predTex = 0
		self.noEffect = 0
		self.ofsMCSE = 0
		self.sizeMCSE = 0
		self.ofsMCLQ = 0
		self.sizeMCLQ = 0
		self.pos = Vec3()
		self.ofsMCCV = 0
		self.pad1 = 0
		self.pad2 = 0
		self.mcvt = EntryChunk(1296258644, HeightValue)
		self.mccv = EntryChunk(1296253782, Color)
		self.mcnr = EntryChunk(1296256594, ADTNormal)
		self.pad3 = 0
		self.pad4 = 0
		self.pad5 = 0
		self.pad6 = 0
		self.mcly = EntryChunk(1296256089, MCLYEntry)
		self.mcrf = EntryChunk(1296257606, Reference)
		self.mcsh = MCSH()
		self.mcal = WChunk()
		self.mclq = WChunk()
		self.mcse = WChunk()
		
		
		
	def unpackData(self,f):
		self.flags, = struct.unpack("i", f.read(4))
		self.indexX, = struct.unpack("i", f.read(4))
		self.indexY, = struct.unpack("i", f.read(4))
		self.nLayers, = struct.unpack("i", f.read(4))
		self.nDoodadRefs, = struct.unpack("i", f.read(4))
		self.ofsMCVT, = struct.unpack("i", f.read(4))
		self.ofsMCNR, = struct.unpack("i", f.read(4))
		self.ofsMCLY, = struct.unpack("i", f.read(4))
		self.ofsMCRF, = struct.unpack("i", f.read(4))
		self.ofsMCAL, = struct.unpack("i", f.read(4))
		self.sizeMCAL, = struct.unpack("i", f.read(4))
		self.ofsMCSH, = struct.unpack("i", f.read(4))
		self.sizeMCSH, = struct.unpack("i", f.read(4))
		self.areaId, = struct.unpack("i", f.read(4))
		self.nMapObjRefs, = struct.unpack("i", f.read(4))
		self.holes, = struct.unpack("i", f.read(4))
		self.lowQualTexMap = struct.unpack("6i", f.read(24))
		self.ofsMCSE, = struct.unpack("i", f.read(4))
		self.sizeMCSE, = struct.unpack("i", f.read(4))
		self.ofsMCLQ, = struct.unpack("i", f.read(4))
		self.sizeMCLQ, = struct.unpack("i", f.read(4))
		self.pos.unpack(f)
		self.ofsMCCV, = struct.unpack("i", f.read(4))
		self.pad1, = struct.unpack("i", f.read(4))
		self.pad2, = struct.unpack("i", f.read(4))
		self.mcvt.unpack(f)
		if (self.flags & MCNK_HAS_VERTEX_COLORS):
			#print "MCCV"
			self.mccv.unpack(f)
		self.mcnr.unpack(f)
		self.pad3, = struct.unpack("b", f.read(1))
		self.pad4, = struct.unpack("i", f.read(4))
		self.pad5, = struct.unpack("i", f.read(4))
		self.pad6, = struct.unpack("i", f.read(4))
		self.mcly.unpack(f)
		self.mcrf.unpack(f)
		if (self.flags & MCNK_HAS_SHADOWS):
			#print "MCSH"
			self.mcsh.unpack(f)
		self.mcal.unpack(f)
		if (self.ofsMCLQ != 0):
			#print "MCLQ"
			self.mclq.unpack(f)
		if (self.ofsMCSE != 0):
			#print "MCSE"
			self.mcse.unpack(f)
		
	def packData(self):
		self.ofsMCVT = 0x88 
		ret1 = self.mcvt.pack()
		if (self.flags & MCNK_HAS_VERTEX_COLORS):
			self.ofsMCCV = 0x88 + len(ret1)
			ret1 += self.mccv.pack()
		self.ofsMCNR = 0x88  + len(ret1)
		ret1 += self.mcnr.pack()
		ret1 += struct.pack("b", self.pad3)
		ret1 += struct.pack("i", self.pad4)
		ret1 += struct.pack("i", self.pad5)
		ret1 += struct.pack("i", self.pad6)
		self.ofsMCLY = 0x88  + len(ret1)
		ret1 += self.mcly.pack()
		self.ofsMCRF = 0x88  + len(ret1)
		ret1 += self.mcrf.pack()
		if (self.flags & MCNK_HAS_SHADOWS):
			self.ofsMCSH = 0x88  + len(ret1)
			ret1 += self.mcsh.pack()
		self.ofsMCAL = 0x88  + len(ret1)
		ret1 += self.mcal.pack()
		if (self.ofsMCLQ != 0):
			self.ofsMCLQ = 0x88  + len(ret1)
			ret1 += self.mclq.pack()
		if (self.ofsMCSE != 0):
			self.ofsMCSE = 0x88  + len(ret1)
			ret1 += self.mcse.pack()
		
		ret = struct.pack("i", self.flags)
		ret += struct.pack("i", self.indexX)
		ret += struct.pack("i", self.indexY)
		ret += struct.pack("i", self.nLayers)
		ret += struct.pack("i", self.nDoodadRefs)
		ret += struct.pack("i", self.ofsMCVT)
		ret += struct.pack("i", self.ofsMCNR)
		ret += struct.pack("i", self.ofsMCLY)
		ret += struct.pack("i", self.ofsMCRF)
		ret += struct.pack("i", self.ofsMCAL)
		ret += struct.pack("i", self.sizeMCAL)
		ret += struct.pack("i", self.ofsMCSH)
		ret += struct.pack("i", self.sizeMCSH)
		ret += struct.pack("i", self.areaId)
		ret += struct.pack("i", self.nMapObjRefs)
		ret += struct.pack("i", self.holes)
		ret += struct.pack("6i", self.lowQualTexMap[0], self.lowQualTexMap[1], self.lowQualTexMap[2], self.lowQualTexMap[3], self.lowQualTexMap[4], self.lowQualTexMap[5])
		ret += struct.pack("i", self.ofsMCSE)
		ret += struct.pack("i", self.sizeMCSE)
		ret += struct.pack("i", self.ofsMCLQ)
		ret += struct.pack("i", self.sizeMCLQ)
		ret += self.pos.pack()
		ret += struct.pack("i", self.ofsMCCV)
		ret += struct.pack("i", self.pad1)
		ret += struct.pack("i", self.pad2)
		ret += ret1
		return ret
		
		
class MCLYEntry:
	entrySize = 16
	def __init__(self):
		self.textureId = 0
		self.flags = 0
		self.ofsMCAL = 0
		self.effectId = 0
		self.pad = 0
	def unpack(self,f):
		self.textureId, = struct.unpack("i", f.read(4))
		self.flags, = struct.unpack("i", f.read(4))
		self.ofsMCAL, = struct.unpack("i", f.read(4))
		self.effectId, = struct.unpack("h", f.read(2))
		self.pad, = struct.unpack("h", f.read(2))
		return self
	def pack(self):
		ret = struct.pack("i", self.textureId)
		ret += struct.pack("i", self.flags)
		ret += struct.pack("i", self.ofsMCAL)
		ret += struct.pack("h", self.effectId)
		ret += struct.pack("h", self.pad)
		return ret
		
class MCSH(WChunk):
	def __init__(self):			
		self.magic = 0
		self.size = 0
		self.data = []
		
	def unpackData(self,f):
		for i in range(64):
			tb = []
			for j in xrange(8):
				shb, = struct.unpack("B", f.read(1))
				for n in xrange(8):
					tb.append( (shb & bitmap[n]) == bitmap[n])
			self.data.append(tb)
			
			
	def packData(self):
		ret = ""
		for i in self.data:
			tb = 0
			c = 0
			for j in i:
				if (j == True):
					tb |= bitmap[c]
				c += 1
				if( c == 8):
					ret += struct.pack("B", tb)
					tb = 0
					c = 0
		return ret
		

		
		
		
class MH2O(WChunk):
	def __init__(self):
		self.magic = 0
		self.size = 0
		self.info = []
	def unpackData(self,f):
		start = f.tell()
		hdr = []
		for i in xrange(256):
			hdr.append(MH2OHeader().unpack(f))
			self.info.append(MH2OChunk())
		for i in xrange(256):
			if(hdr[i].nLayers > 0):
				self.info[i].nLayers = hdr[i].nLayers
				f.seek(start+hdr[i].ofsInfo)
				for n in range(hdr[i].nLayers):
					self.info[i].info.append(MH2OInfo().unpack(f))
				f.seek(start+hdr[i].ofsMask)
				for n in range(hdr[i].nLayers):
					self.info[i].render.append(MH2ORender().unpack(f))					
				for n in range(hdr[i].nLayers):
					inf = self.info[i].info[n]
					f.seek(start+inf.ofsHeightmap)
					sz = inf.width*inf.height
					self.info[i].height.append(MH2OHeight().unpack(f,sz))
		
		s = open("test.txt","wb")
		for i in xrange(256):
			s.write("Chunk: "+str(i)+"\n")
			s.write(str(self.info[i]))
		s.close()
		f.seek(start+self.size)
	def packData(self):
		return ""
		
class MH2OChunk:
	def __init__(self):
		self.nLayers = 0
		self.info = []
		self.render = []
		self.mask = []
		self.height = []
		
	def __str__(self):
		ret = ""
		for i in range(self.nLayers):
			ret += "Layer: "+str(i)+"\n"
			ret += "LiquidType: "+str(self.info[i].liquidType)
			ret += "Flags: "+str(self.info[i].flags)
			ret += "\t highHeight: "+str(self.info[i].highHeight)
			ret += "\t lowHeight: "+str(self.info[i].lowHeight)+"\n"
			ret += "xOffset: "+ str(self.info[i].xOffset) 
			ret += "\t yOffset"+ str(self.info[i].yOffset) 
			ret += "\t Width: " + str(self.info[i].width)   
			ret += "\t Height: "+str(self.info[i].height)  + "\n"
			ret += "Rendermask:\n"
			ret += str(self.render[i])
		return ret
		
class MH2OHeader:
	def __init__(self):
		self.ofsInfo = 0
		self.nLayers = 0
		self.ofsMask = 0
	def unpack(self,f):
		self.ofsInfo, = struct.unpack("i", f.read(4))
		self.nLayers, = struct.unpack("i", f.read(4))
		self.ofsMask, = struct.unpack("i", f.read(4))
		return self
		
	def pack(self):
		ret = struct.pack("i", self.ofsInfo)
		ret += struct.pack("i", self.nLayers)
		ret += struct.pack("i", self.ofsMask)
		return ret
		
class MH2OInfo:
	def __init__(self):
		self.liquidType = 0
		self.flags = 0
		self.highHeight = 0
		self.lowHeight = 0
		self.xOffset = 0
		self.yOffset = 0
		self.width = 0
		self.height = 0
		self.ofsRender = 0
		self.ofsHeightmap = 0
	def unpack(self,f):
		self.liquidType, = struct.unpack("h", f.read(2))
		self.flags, = struct.unpack("h", f.read(2))
		self.highHeight, = struct.unpack("f", f.read(4))
		self.lowHeight, = struct.unpack("f", f.read(4))
		self.xOffset, = struct.unpack("b", f.read(1))
		self.yOffset, = struct.unpack("b", f.read(1))
		self.width, = struct.unpack("b", f.read(1))
		self.height, = struct.unpack("b", f.read(1))
		self.ofsRender, = struct.unpack("i", f.read(4))
		self.ofsHeightmap, = struct.unpack("i", f.read(4))
		return self
		
	def pack(self):
		ret = struct.pack("h", self.liquidType)
		ret += struct.pack("h", self.flags)
		ret += struct.pack("f", self.highHeight)
		ret += struct.pack("f", self.lowHeight)
		ret += struct.pack("b", self.xOffset)
		ret += struct.pack("b", self.yOffset)
		ret += struct.pack("b", self.width)
		ret += struct.pack("b", self.height)
		ret += struct.pack("i", self.ofsRender)
		ret += struct.pack("i", self.ofsHeightmap)
		return ret
		
class MH2OHeight:
	def __init__(self):
		self.heightMap = []
		self.transparency = []
	def unpack(self,f,size):
		for i in range(size):
			tmp = struct.unpack("f", f.read(4))
			self.heightMap.append(tmp)
		for i in range(size):
			tmp = struct.unpack("b", f.read(1))
			self.transparency.append(tmp)
		return self
		
	def pack(self):
		ret = ""
		for i in self.heightMap:
			ret += struct.pack("f", i)
		for i in self.transparency:
			ret += struct.pack("b", i)
		return ret
		
class MH2ORender:
	def __init__(self):
		self.render = []
		
	def __str__(self):
		ret = ""
		for i in xrange(8):
			for j in xrange(8):
				ret +=  "1" if(self.render[i*8+j]) else "0"
				ret += "  "
			ret += "\n"
		return ret
	def unpack(self,f):
		for i in xrange(8):
			tmp, = struct.unpack("B", f.read(1))
			for j in xrange(8):
				self.render.append( (tmp & bitmap[j]) == bitmap[j])
				
		return self
	def pack(self):
		ret = ""
		tb = 0
		for i in self.render:	
			if (i == True):
				tb |= bitmap[c]
				c += 1
			if( c == 8):
				ret += struct.pack("B", tb)
				tb = 0
				c = 0	
		return ret
		
	
		