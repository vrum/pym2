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
	def __init__(self):
		self.magic = 1297499474
		self.size = 4
		self.version = 18
	def unpackData(self,f):
		self.version, = struct.unpack("i",f.read(4))
		
	def packData(self):
		ret = struct.pack("i",self.version)
		return ret
		
class FilenameChunk(WChunk):
	def __init__(self,magic):
		self.magic = magic
		self.size = 0
		self.filenames = []
		
	def unpackData(self,f):
		pos = 1
		temp = f.read(1)
		tstr = str(temp)
		print self.size
		while(pos < self.size):			
			pos += 1
			while(temp != "\0"):
				temp = f.read(1)
				tstr += temp
				pos += 1
			self.filenames.append(tstr)
			tstr = ""
		#print self.filenames
		
	def packData(self):
		ret = ""
		for i in self.filenames:
			if len(i) == 0:
				i= "\0"
			if i[len(i)-1] != "\0":
				i += "\0"
			ret += i
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
		