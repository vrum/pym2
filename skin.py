import struct
import array
from wowfile import *

class SkinHeader:
	def __init__(self,f):
		self.magic,         = struct.unpack("4s",f.read(4))
		self.Indices,        = Chunk(f)
		self.Triangles,      = Chunk(f)
		self.Properties,     = Chunk(f)
		self.Submeshes,      = Chunk(f)
		self.TextureUnits,   = Chunk(f)
		self.lod,	    = struct.unpack("i",f.read(4))
		
	def pack(self):
		ret = struct.pack("4s",self.magic)
		ret +=  self.Indices.pack()
		ret +=  self.Triangles.pack()
		ret +=  self.Properties.pack()
		ret +=  self.Submeshes.pack()
		ret +=  self.TextureUnits.pack()
		ret += struct.pack("i", self.lod)
		return ret
	
class Mesh:
	def __init__(self,f):
		self.mesh_id,		= struct.unpack("i",f.read(4))
		self.vert_offset,	= struct.unpack("H",f.read(2))
		self.num_verts,		= struct.unpack("H",f.read(2))
		self.tri_offset,	= struct.unpack("H",f.read(2))
		self.num_tris,		= struct.unpack("H",f.read(2))
		self.num_bones,		= struct.unpack("H",f.read(2))
		self.start_bone,	= struct.unpack("H",f.read(2))
		self.unknown,		= struct.unpack("H",f.read(2))
		self.rootbone,		= struct.unpack("H",f.read(2))
		self.bound,		= Bounds(f)
		
	def pack(self):
		ret = struct.pack("i",self.mesh_id)
		ret += struct.pack("H",self.vert_offset)
		ret += struct.pack("H", self.num_verts)
		ret += struct.pack("H", self.tri_offset)
		ret += struct.pack("H", self.num_tris)
		ret += struct.pack("H", self.num_bones)
		ret += struct.pack("H", self.start_bone)
		ret += struct.pack("H", self.unknown)
		ret += struct.pack("H", self.rootbone)
		ret += self.bound.pack()
		return ret
		

class Material:
	def __init__(self,f):
		self.flags,         = struct.unpack("H",f.read(2))
		self.shading,	    = struct.unpack("H",f.read(2))
		self.submesh,       = struct.unpack("H",f.read(2))
		self.submesh2,      = struct.unpack("H",f.read(2))
		self.color,         = struct.unpack("h",f.read(2))
		self.renderflag,    = struct.unpack("H",f.read(2))
		self.texunit, 	    = struct.unpack("H",f.read(2))
		self.mode,          = struct.unpack("H",f.read(2))
		self.texture,       = struct.unpack("H",f.read(2))
		self.texunit2,      = struct.unpack("H",f.read(2))
		self.transparency,  = struct.unpack("H",f.read(2))
		self.animation,      = struct.unpack("H",f.read(2))
		
	def pack(self):
		ret = struct.pack("H",self.flags)
		ret += struct.pack("H",self.shading)
		ret += struct.pack("H",self.submesh)
		ret += struct.pack("H",self.submesh2)
		ret += struct.pack("h",self.color)
		ret += struct.pack("H",self.renderflag)
		ret += struct.pack("H",self.texunit)
		ret += struct.pack("H",self.mode)
		ret += struct.pack("H",self.texture)
		ret += struct.pack("H",self.texunit2)
		ret += struct.pack("H",self.transparency)
		ret += struct.pack("H",self.animation)
		return ret

class Skin:
	def __init__(self,filename):
		f = open(filename,"r+b")
		self.header	= SkinHeader(f)
		self.indices	= []
		self.tri	= []
		self.prop	= []
		self.mesh	= []
		self.texunit	= []
		
		f.seek(self.header.Indices.offset)
		for i in range(self.header.Indices.count):
			temp	= struct.unpack("h",f.read(2))
			self.indices.append(temp)
		
		f.seek(self.header.Triangles.offset)		
		for i in range(self.header.Triangles.count / 3):
			temp	= struct.unpack("3H",f.read(6))
			self.tri.append(temp)
			
		f.seek(self.header.Properties.offset)
		for i in range(self.header.Properties.count):
			temp	= struct.unpack("4b",f.read(4))
			self.prop.append(temp)
			
		f.seek(self.header.Submeshes.offset)
		for i in range(self.header.Submeshes.count):
			temp	= Mesh(f)
			self.mesh.append(temp)
			
		f.seek(self.header.TextureUnits.offset)
		for i in range(self.header.TextureUnits.count):
			temp	= Material(f)
			self.texunit.append(temp)
			
		
	def write(self,filename):
		f = open(filename,"wb")
		f.write(self.header.pack())
		
		ofs = f.tell()
		self.header.Indices.offset = ofs
		for i in range(self.header.Indices.count):
			temp = struct.pack("h",self.indices[i][0])
			f.write(temp)
		FillLine(f)
		
		ofs = f.tell()
		self.header.Triangles.offset = ofs
		for i in range(self.header.Triangles.count / 3):
			temp = struct.pack("3H",self.tri[i][0],self.tri[i][1],self.tri[i][2])
			f.write(temp)
		FillLine(f)
		
		ofs = f.tell()
		self.header.Properties.offset = ofs
		for i in range(self.header.Properties.count):
			temp = struct.pack("4b",self.prop[i][0],self.prop[i][1],self.prop[i][2],self.prop[i][3])
			f.write(temp)
		FillLine(f)
		
		ofs = f.tell()
		self.header.Submeshes.offset = ofs
		for i in range(self.header.Submeshes.count):
			temp = self.mesh[i].pack()
			f.write(temp)
		FillLine(f)
		
		ofs = f.tell()
		self.header.TextureUnits.offset = ofs
		for i in range(self.header.TextureUnits.count):
			temp = self.texunit[i].pack()
			f.write(temp)
		FillLine(f)
		
		f.seek(0,SEEK_SET)
		f.write(self.header.pack())
	


