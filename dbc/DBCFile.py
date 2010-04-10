import struct
import array


	
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
	
def ReadInt(f):
	return struct.unpack("i",f.read(4))
	
def ReadFloat(f):
	return struct.unpack("f",f.read(4))
	
	
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
		
class DBC:
	def __init__(self,filename,entryclass):
		f = open(filename,"r+b")
		f.seek(0,2)
		eof = f.tell()
		f.seek(0,0)
		self.hdr = DBCHeader().unpack(f)
		self.StringOffset = f.tell() + self.hdr.nRecords * 32
		self.entries = []
		for i in xrange(self.hdr.nRecords):
			temp = entryclass().unpack(f,self.StringOffset)
			self.entries.append(temp)
		
		