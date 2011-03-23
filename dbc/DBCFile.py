import struct
import array

range = xrange

class DBCLoc:
	def __init__(self):
		self.Languages = []
		for i in range(16):
			self.Languages.append("\0")
		self.LocMask = 0
	def unpack(self,f,sDict):
		self.Languages = []
		for i in range(16):
			t, = ReadInt(f)
			print i
			print sDict[t]
			self.Languages.append(sDict[t])
		self.LocMask, = ReadInt(f)
		return self
	def pack(self,rDict):
		ret = ''
		for i in self.Languages:
			ret += PackInt(rDict[i])
		ret += PackInt(self.LocMask)
		return ret
		


def CreateStringDictionary(f,sOffset,szStrings):
	ret_ofs = {}
	ret_str = {}
	oldpos = f.tell()
	f.seek(sOffset)
	while (f.tell() < szStrings+sOffset):
		ofs = f.tell() - sOffset
		t = ""
		Name = ""
		while t != "\0":
			t = f.read(1)
			Name += t
		ret_ofs.update({ofs : Name})
		ret_str.update({Name : ofs})
	f.seek(oldpos)
	return (ret_ofs,ret_str)

	
def ReadString(f,sOffset,offset):
	oldpos = f.tell()
	f.seek(sOffset + offset)
	t = ""
	Name = ""
	while t != "\0":
		t = f.read(1)
		Name += t
	f.seek(oldpos)
	return Name
	
def PackString(s,sBlock):
	ret = len(sBlock)
	sBlock += s
	ret = PackInt(ret)
	return (ret,sBlock)
	
def ReadLoc(f,sDict):
	ret = []
	for i in range(16):
		t, = struct.unpack("i",f.read(4))
		if(t!=0):
			if(t in sDict):
				ret.append(sDict[t])
			else:
				s = "Not found: " +str(t)
				ret.append(s)
	#bitmask at end
	t = struct.unpack("i",f.read(4))
	return ret
	
def ReadInt(f):
	return struct.unpack("i",f.read(4))
	
def PackInt(i):
	return struct.pack("i",i)
	
def ReadFloat(f):
	return struct.unpack("f",f.read(4))
	
def PackFloat(f):
	return struct.pack("f",f)
	
def ReadChar(f):
	return struct.unpack("B",f.read(1))
	
def PackChar(f):
	return struct.pack("B",f)
	
def ReadLong(f):
	return struct.unpack("q",f.read(8))
	
def PackLong(f):
	return struct.pack("q",f)
	
class DBCEntry:
	def __init__(self):
		pass
	def __module__(self):
		pass
	def __doc__(self):
		pass
	def unpack(self,f,sDict):
		pass
	def pack(self,rDict):
		memberList = [member for member in dir(self) if not callable(getattr(self, member))]
		ret = ''
		for i in memberList:
			if type(getattr(self, i)) == type(''):
				ret += PackInt(rDict[getattr(self, i)])
			elif type(getattr(self, i)) == type(1):
				ret += PackInt(getattr(self, i))
			elif type(getattr(self, i)) == type(1L):
				ret += PackLong(getattr(self, i))
			elif type(getattr(self, i)) == type(1.0):
				ret += PackFloat(getattr(self, i))
			elif type(getattr(self, i)) == type(DBCLoc()):
				ret += getattr(self, i).pack(rDict)
			else:#Yet unknown
				pass
		return ret
class DBCHeader:
	def __init__(self):
		pass
	def unpack(self,f):
		self.signature, = ReadInt(f)
		self.nRecords,	= ReadInt(f)
		self.nFields,	= ReadInt(f)
		self.szRecords,	= ReadInt(f)
		self.szFields 	= self.szRecords / self.nFields
		self.szStrings,	= ReadInt(f)
		return self
		
	def pack(self):
		ret = PackInt(self.signature)
		ret += PackInt(self.nRecords)
		ret += PackInt(self.nFields)
		ret += PackInt(self.szRecords)
		ret += PackInt(self.szStrings)
		return ret
		
class DBC:
	def __init__(self,filename,entryclass):
		f = open(filename,"r+b")
		self.hdr = DBCHeader().unpack(f)
		self.StringOffset = f.tell() + self.hdr.nRecords * self.hdr.szRecords
		self.entries = []
		(self.sDict,self.rDict) = CreateStringDictionary(f,self.StringOffset,self.hdr.szStrings)
		for i in range(self.hdr.nRecords):
			temp = entryclass().unpack(f,self.sDict)
			self.entries.append(temp)
		
	def AddEntry(self,entrie):
		self.entries.append(entrie)
		
		memberList = [member for member in dir(entrie) if not callable(getattr(entrie, member))]
		for i in memberList:
			if type(getattr(entrie, i)) == type(''):
				n = getattr(entrie, i)
				#check if last byte is NULL
				if n[-1] != "\0":
					n += "\0"
					setattr(entrie, i,n)
				#if the string is not yet in the dbc, add it
				if not self.rDict.has_key(n):
					self.rDict.update({n:self.hdr.szStrings})
					self.sDict.update({self.hdr.szStrings:n})
					self.hdr.szStrings += len(n)

		self.hdr.nRecords += 1
		
	def write(self,filename):
		f = open(filename,"w+b")
		f.write(self.hdr.pack())
		self.StringOffset = f.tell() + self.hdr.nRecords * self.hdr.szRecords	
		
		for i in self.entries:
			t = i.pack(self.rDict)
			f.write(t)
			
		sBlock = ""
		for i in range(len(self.sDict)):
			sBlock += self.sDict[len(sBlock)]
		self.hdr.szStrings = len(sBlock)
		f.write(sBlock)
		f.seek(0,0)
		f.write(self.hdr.pack())
		f.close()
		