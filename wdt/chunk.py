#!/usr/bin/python
import struct
import array


class WChunk: #Chunk Basic Class for World Data (like adt,wmo etc.)
	def __init__(self):
		self.magic = 0
		self.size = 0
		
	def unpack(self,f):
		self.magic,         = struct.unpack("i",f.read(4))
		self.size,         = struct.unpack("i",f.read(4))
		self.unpackData(f)
		return self
		
	def pack(self):
		temp = self.packData()
		self.size = len(temp)		
		ret = struct.pack("i",self.magic)
		ret += struct.pack("i",self.size)
		ret += temp
		return ret
		
	def unpackData(self,f):
		pass
		
	def packData(self):
		return 0	
		
		
class MVER(WChunk):
	def unpackData(self,f):
		self.version, = struct.unpack("i",f.read(4))
		
	def packData(self):
		ret = struct.pack("i",self.version)
		return ret


class WoWFile:	
	def __init__(self):
		pass
		
	def readData(self,f):
		pass
		
	def writeData(self,f):
		return f
		
	def read(self,filename):
		f = open(filename,"r+b")		
		self.readData(f)			
		f.close()
		return self
	
	
	def write(self,filename):
		f = open(filename,"wb")		
		f = self.writeData(f)		
		f.close()
		