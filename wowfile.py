#This file contains some helpers for the files
import struct

SEEK_SET	= 0
SEEK_CUR	= 1
SEEK_END	= 2

def FillLine(f):
	i = f.tell()
	n = (16 - ((i) % 16))#Calculate the bytes needed to fill up the 0x10 ( == 16)
	for i in range(n):		
		f.write("\0")#write 0-Byte
		
	return f
	

class Chunk:
	def __init__(self,f):
		self.count,     = struct.unpack("i",f.read(4))
		self.offset,    = struct.unpack("i",f.read(4))
		
	def pack(self):
		ret = struct.pack("2i",self.count,self.offset)
		return ret
		
class Vec3:
	def __init__(self,f):
		self.x,	= struct.unpack("f",f.read(4))
		self.y,	= struct.unpack("f",f.read(4))
		self.z,	= struct.unpack("f",f.read(4))
		
	def pack(self):
		ret = struct.pack("f",self.x)
		ret += struct.pack("f",self.y)
		ret += struct.pack("f",self.z)
		return ret
		
class Vec2:
	def __init__(self,f):
		self.x,	= struct.unpack("f",f.read(4))
		self.y,	= struct.unpack("f",f.read(4))
		
	def pack(self):
		ret = struct.pack("f",self.x)
		ret += struct.pack("f",self.y)
		return ret
		
class Quat:
	def __init__(self,f):
		self.x, = struct.unpack("h",f.read(2))
		self.y, = struct.unpack("h",f.read(2))
		self.z, = struct.unpack("h",f.read(2))
		self.w, = struct.unpack("h",f.read(2))
		
	def pack(self):
		ret = struct.pack("h",self.x)
		ret += struct.pack("h",self.y)
		ret += struct.pack("h",self.z)
		ret += struct.pack("h",self.w)
		return ret
		
class Bounds:
	def __init__(self,f):
		self.BoundingBox	= struct.unpack("6f",f.read(24))
		self.Radius,		= struct.unpack("f",f.read(4))
		
	def pack(self):
		ret = struct.pack("6f",self.BoundingBox[0],self.BoundingBox[1],self.BoundingBox[2],self.BoundingBox[3],self.BoundingBox[4],self.BoundingBox[5])
		ret += struct.pack("f",self.Radius)
		return ret
	