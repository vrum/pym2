import struct
import array
from wowfile import *

#Tilting Values
TILT_X = 1
TILT_Y = 2

#AnimBlock Data Types
DATA_QUAT = 0
DATA_VEC3 = 1
DATA_INT  = 2
DATA_SHORT= 3
DATA_VEC2 = 4
DATA_FLOAT= 5
DATA_VEC9 = 6

#Classes for the different structs
class M2Header:
	def __init__(self,f):
		self.magic,         = struct.unpack("i",f.read(4))
		self.version,        = struct.unpack("i",f.read(4))
		self.name          = Chunk(f)
		self.model_type,    = struct.unpack("i",f.read(4))
		self.global_sequences = Chunk(f)
		self.animations     = Chunk(f)
		self.anim_lookup    = Chunk(f)
		self.bones          = Chunk(f)
		self.key_bones      = Chunk(f)
		self.vertices       = Chunk(f)
		self.nviews,        = struct.unpack("i",f.read(4))
		self.colors         = Chunk(f)
		self.textures       = Chunk(f)
		self.transparency   = Chunk(f)
		self.uv_anim        = Chunk(f)
		self.tex_replace    = Chunk(f)
		self.render_flags   = Chunk(f)
		self.bone_lookup    = Chunk(f)
		self.tex_lookup     = Chunk(f)
		self.tex_units      = Chunk(f)
		self.trans_lookup   = Chunk(f)
		self.uv_anim_lookup = Chunk(f)
		self.bound	= Bounds(f)
		self.vbox	= Bounds(f)
		self.bounding_triangles = Chunk(f)
		self.bounding_vertices = Chunk(f)
		self.bounding_normals = Chunk(f)
		self.attachments    = Chunk(f)
		self.attach_lookup  = Chunk(f)
		self.events         = Chunk(f)
		self.lights         = Chunk(f)
		self.cameras        = Chunk(f)
		self.camera_lookup  = Chunk(f)
		self.ribbon_emitters = Chunk(f)
		self.particle_emitters = Chunk(f)	
		if(self.model_type&8):
			self.unknown = Chunk(f)
		
	def pack(self):
		ret = struct.pack("i",self.magic)
		ret += struct.pack("i",self.version)
		ret += self.name.pack()
		ret += struct.pack("i",self.model_type)
		ret += self.global_sequences.pack()
		ret += self.animations.pack()
		ret += self.anim_lookup.pack()
		ret += self.bones.pack()
		ret += self.key_bones.pack()
		ret += self.vertices.pack()
		ret += struct.pack("i",self.nviews)
		ret += self.colors.pack()
		ret += self.textures.pack()
		ret += self.transparency.pack()
		ret += self.uv_anim.pack()
		ret += self.tex_replace.pack()
		ret += self.render_flags.pack()
		ret += self.bone_lookup.pack()
		ret += self.tex_lookup.pack()
		ret += self.tex_units.pack()
		ret += self.trans_lookup.pack()
		ret += self.uv_anim_lookup.pack()
		ret += self.bound.pack()
		ret += self.vbox.pack()
		ret += self.bounding_triangles.pack()
		ret += self.bounding_vertices.pack()
		ret += self.bounding_normals.pack()
		ret += self.attachments.pack()
		ret += self.attach_lookup.pack()
		ret += self.events.pack()
		ret += self.lights.pack()
		ret += self.cameras.pack()
		ret += self.camera_lookup.pack()
		ret += self.ribbon_emitters.pack()
		ret += self.particle_emitters.pack()
		if(self.model_type&8):
			ret += self.unknown.pack()
		return ret

class Vertex:
	def __init__(self,f):
		self.pos        = struct.unpack("3f",f.read(12))
		self.bweights   = struct.unpack("4B",f.read(4))
		self.bindices   = struct.unpack("4B",f.read(4))
		self.normal     = struct.unpack("3f",f.read(12))
		self.uv         = struct.unpack("2f",f.read(8))
		self.unk         = struct.unpack("2f",f.read(8))
		
	def pack(self):
		ret = struct.pack("3f",self.pos[0],self.pos[1],self.pos[2])
		ret += struct.pack("4B",self.bweights[0],self.bweights[1],self.bweights[2],self.bweights[3])
		ret += struct.pack("4B",self.bindices[0],self.bindices[1],self.bindices[2],self.bindices[3])
		ret += struct.pack("3f",self.normal[0],self.normal[1],self.normal[2])
		ret += struct.pack("2f",self.uv[0],self.uv[1])
		ret += struct.pack("2f",self.unk[0],self.unk[1])
		return ret
		
class Sequ:
	def __init__(self,f):
		self.animId,	= struct.unpack("H",f.read(2))
		self.subId,	= struct.unpack("H",f.read(2))
		self.len,	= struct.unpack("i",f.read(4))
		self.moveSpeed,	= struct.unpack("f",f.read(4))
		self.flags,	= struct.unpack("i",f.read(4))
		self.prob,	= struct.unpack("h",f.read(2))
		self.pad,	= struct.unpack("h",f.read(2))
		self.unk	= struct.unpack("2i",f.read(8))
		self.playSpeed,	= struct.unpack("i",f.read(4))
		self.bound	= Bounds(f)
		self.next,	= struct.unpack("h",f.read(2))
		self.index,	= struct.unpack("H",f.read(2))
		
	def pack(self):
		ret = struct.pack("H",self.animId)
		ret += struct.pack("H",self.subId)
		ret += struct.pack("i",self.len)
		ret += struct.pack("f",self.moveSpeed)
		ret += struct.pack("i",self.flags)
		ret += struct.pack("h",self.prob)
		ret += struct.pack("h",self.pad)
		ret += struct.pack("2i",self.unk[0],self.unk[1])
		ret += struct.pack("i",self.playSpeed)
		ret += self.bound.pack()
		ret += struct.pack("h",self.next)
		ret += struct.pack("H",self.index)
		return ret
	

class AnimSub:
	def __init__(self,f,type):
		self.nEntries,	= struct.unpack("i",f.read(4))
		self.ofsEntries,= struct.unpack("i",f.read(4))
		oldpos = f.tell()
		f.seek(self.ofsEntries)
		self.values = []
		for i in range(self.nEntries):
			if(type == DATA_QUAT):
				temp = Quat(f)
				self.values.append(temp)
			elif(type == DATA_VEC3):
				temp = Vec3(f)
				self.values.append(temp)
			elif(type == DATA_INT):
				temp = struct.unpack("i",f.read(4))
				self.values.append(temp)
			elif(type == DATA_SHORT):
				temp = struct.unpack("h",f.read(2))
				self.values.append(temp)
			elif(type == DATA_VEC2):
				temp = Vec2(f)
				self.values.append(temp)
			elif(type == DATA_FLOAT):
				temp = struct.unpack("f",f.read(4))
				self.values.append(temp)
			else:
				pass
		f.seek(oldpos)
		
	def pack(self,type):
		ret = struct.pack("i",self.nEntries)
		ret += struct.pack("i",self.ofsEntries)
		return ret
	
class AnimBlock:
	def __init__(self,f,type):
		self.interpolation,= struct.unpack("h",f.read(2))
		self.gsequ,	= struct.unpack("h",f.read(2))
		self.nTimes,	= struct.unpack("i",f.read(4))
		self.ofsTimes,	= struct.unpack("i",f.read(4))
		
		oldpos = f.tell()
		f.seek(self.ofsTimes)
		self.TimeSubs = []
		for i in range(self.nTimes):
			temp = AnimSub(f,DATA_INT)
			self.TimeSubs.append(temp)
		f.seek(oldpos)
		
		self.nKeys,	= struct.unpack("i",f.read(4))
		self.ofsKeys,	= struct.unpack("i",f.read(4))
		
		oldpos = f.tell()
		f.seek(self.ofsKeys)
		self.KeySubs = []
		for i in range(self.nKeys):
			temp = AnimSub(f,type)
			self.KeySubs.append(temp)
		f.seek(oldpos)
		
	def pack(self):
		ret = struct.pack("h",self.interpolation)
		ret += struct.pack("h",self.gsequ)
		ret += struct.pack("i",self.nTimes)
		ret += struct.pack("i",self.ofsTimes)
		ret += struct.pack("i",self.nKeys)
		ret += struct.pack("i",self.ofsKeys)
		return ret
		
	
class Bone:
	def __init__(self,f):
		self.KeyBoneId,	= struct.unpack("i",f.read(4))
		self.flags,	= struct.unpack("i",f.read(4))
		self.parent,	= struct.unpack("h",f.read(2))
		self.unk	= struct.unpack("3h",f.read(6))
		self.translation= AnimBlock(f,DATA_VEC3)
		self.rotation	= AnimBlock(f,DATA_QUAT)
		self.scaling	= AnimBlock(f,DATA_VEC3)
		self.pivot	= Vec3(f)
	def pack(self):
		ret = struct.pack("i",self.KeyBoneId)
		ret += struct.pack("i",self.flags)
		ret += struct.pack("h",self.parent)
		ret += struct.pack("3h",self.unk[0],self.unk[1],self.unk[2])
		ret += self.translation.pack()
		ret += self.rotation.pack()
		ret += self.scaling.pack()
		ret += self.pivot.pack()
		return ret
		
class Attachment:
	def __init_(self,f):
		self.Id,	= struct.unpack("i",f.read(4))
		self.bone,	= struct.unpack("i",f.read(4))
		self.pos	= Vec3(f)
		self.Enabled	= AnimBlock(f,DATA_INT)
	def pack(self):
		ret = struct.pack("i",self.Id)
		ret += struct.pack("i",self.bone)
		ret += self.pos.pack()
		ret += self.Enabled.pack()
		return ret
		
class Texture:
	def __init__(self,f):
		self.type,	= struct.unpack("i",f.read(4))
		self.flags,	= struct.unpack("i",f.read(4))
		self.len_name,	= struct.unpack("i",f.read(4))
		self.ofs_name,	= struct.unpack("i",f.read(4))
		oldpos = f.tell()
		f.seek(self.ofs_name)
		self.name = f.read(self.len_name)
		f.seek(oldpos)
	def pack(self):
		ret = struct.pack("i",self.type)
		ret += struct.pack("i",self.flags)
		ret += struct.pack("i",self.len_name)
		ret += struct.pack("i",self.ofs_name)
		return ret
		
class Renderflags:
	def __init__(self,f):
		self.flags,	= struct.unpack("h",f.read(2))
		self.blend,	= struct.unpack("h",f.read(2))
	def pack(self):
		ret = struct.pack("h",self.flags)
		ret += struct.pack("h",self.blend)
		return ret
		
class UVAnimation:
	def __init__(self,f):
		self.translation= AnimBlock(f,DATA_VEC3)
		self.rotation	= AnimBlock(f,DATA_QUAT)
		self.scaling	= AnimBlock(f,DATA_VEC3)
		
	def pack(self):
		ret = self.translation.pack()
		ret += self.rotation.pack()
		ret += self.scaling.pack()
		return ret

class Color:
	def __init__(self,f):
		self.color = AnimBlock(f,DATA_VEC3)
		self.alpha = AnimBlock(f,DATA_SHORT)
		
	def pack(self):
		ret = self.color.pack()
		ret += self.alpha.pack()
	
class Event:
	def __init__(self,f):
		self.Id,	= struct.unpack("i",f.read(4))
		self.Data,	= struct.unpack("i",f.read(4))
		self.Bone,	= struct.unpack("i",f.read(4))
		self.Pos,	= Vec3(f)
		self.interpolation,= struct.unpack("h",f.read(2))
		self.gsequ,	= struct.unpack("h",f.read(2))
		self.nTimes,	= struct.unpack("i",f.read(4))
		self.ofsTimes,	= struct.unpack("i",f.read(4))
		
		oldpos = f.tell()
		f.seek(self.ofsTimes)
		self.TimeSubs = []
		for i in range(self.nTimes):
			temp = AnimSub(f,DATA_INT)
			self.TimeSubs.append(temp)
		f.seek(oldpos)
	
	def pack(self):
		ret = struct.pack("i",self.Id)
		ret += struct.pack("i",self.Data)
		ret += struct.pack("i",self.Bone)
		ret += self.Pos.pack()
		ret += struct.pack("h",self.interpolation)
		ret += struct.pack("h",self.gsequ)
		ret += struct.pack("i",self.nTimes)
		ret += struct.pack("i",self.ofsTimes)
	
class Light:
	def __init__(self,f):
		self.Type,	= struct.unpack("h",f.read(2))
		self.Bone,	= struct.unpack("h",f.read(2))
		self.Pos,	= Vec3(f)
		self.AmbientCol	= AnimBlock(f,DATA_VEC3)
		self.AmbientInt	= AnimBlock(f,DATA_FLOAT)
		self.DiffuseCol	= AnimBlock(f,DATA_VEC3)
		self.DiffuseInt	= AnimBlock(f,DATA_FLOAT)
		self.AttStart	= AnimBlock(f,DATA_FLOAT)
		self.AttEnd	= AnimBlock(f,DATA_FLOAT)
		self.Enabled	= AnimBlock(f,DATA_INT)
	def pack(self):
		pass

class FakeAnim:
	def __init__(self,f,type):
		self.nTimes,	= struct.unpack("i",f.read(4))
		self.ofsTimes,	= struct.unpack("i",f.read(4))
		
		oldpos = f.tell()
		f.seek(self.ofsTimes)
		self.Times = []
		for i in range(self.nTimes):
			temp = struct.unpack("h",f.read(2))
			self.Times.append(temp)
		f.seek(oldpos)
		
		self.nKeys,	= struct.unpack("i",f.read(4))
		self.ofsKeys,	= struct.unpack("i",f.read(4))
		
		oldpos = f.tell()
		f.seek(self.ofsKeys)
		self.Keys = []
		for i in range(self.nKeys):
			if (type == DATA_SHORT):
				temp = struct.unpack("h",f.read(2))
				self.Keys.append(temp)
			elif ( type == DATA_VEC3):
				temp = Vec3(f)
				self.Keys.append(temp)
			elif ( type == DATA_VEC2):
				temp = Vec2(f)
				self.Keys.append(temp)
			else:
				pass
		f.seek(oldpos)
			
	def pack(self):
		ret = struct.pack("i",self.nTimes)
		ret += struct.pack("i",self.ofsTimes)
		ret += struct.pack("i",self.nKeys)
		ret += struct.pack("i",self.ofsKeys)
		return ret

class Particle:
	def __init__(self,f):
		self.Id,	= struct.unpack("i",f.read(4))
		self.flags1,	= struct.unpack("h",f.read(2))
		self.flags2,	= struct.unpack("h",f.read(2))
		self.Pos,	= Vec3(f)
		self.bone,	= struct.unpack("h",f.read(2))
		self.texture,	= struct.unpack("h",f.read(2))
		
		self.lenModel,	= struct.unpack("i",f.read(4))
		self.ofsModel,	= struct.unpack("i",f.read(4))
		oldpos	= f.tell()
		f.seek(self.ofsModel)
		self.ModelName = f.read(self.lenModel)
		f.seek(oldpos)
		
		self.lenParticle,	= struct.unpack("i",f.read(4))
		self.ofsParticle,	= struct.unpack("i",f.read(4))
		oldpos	= f.tell()
		f.seek(self.ofsParticle)
		self.ParticleName = f.read(self.lenParticle)
		f.seek(oldpos)
		
		self.blend,	= struct.unpack("b",f.read(1))
		self.emitter,	= struct.unpack("b",f.read(1))
		self.color_dbc,	= struct.unpack("h",f.read(2))
		self.particletype, = struct.unpack("b",f.read(1))
		self.head_or_tail, = struct.unpack("b",f.read(1))
		self.tex_tile_rot, = struct.unpack("h",f.read(2))
		self.tex_rows,	= struct.unpack("h",f.read(2))
		self.tex_cols,	= struct.unpack("h",f.read(2))
		self.emission_speed, = AnimBlock(f,DATA_FLOAT)
		self.speed_var, = AnimBlock(f,DATA_FLOAT)
		self.vert_range, = AnimBlock(f,DATA_FLOAT)
		self.hor_range, = AnimBlock(f,DATA_FLOAT)
		self.gravity, = AnimBlock(f,DATA_FLOAT)
		self.lifespan, = AnimBlock(f,DATA_FLOAT)
		self.pad1,	= struct.unpack("i",f.read(4))
		self.emission_rate, = AnimBlock(f,DATA_FLOAT)
		self.pad2,	= struct.unpack("i",f.read(4))
		self.emission_area_len, = AnimBlock(f,DATA_FLOAT)
		self.emission_area_width, = AnimBlock(f,DATA_FLOAT)
		self.gravity2, = AnimBlock(f,DATA_FLOAT)
		self.color,	= FakeAnim(f,DATA_VEC3)
		self.opacity,	= FakeAnim(f,DATA_SHORT)
		self.size,	= FakeAnim(f,DATA_VEC2)
		self.pad3	= struct.unpack("2i",f.read(8))
		self.intensity,	= FakeAnim(f,DATA_SHORT)
		self.unkfake,	= FakeAnim(f,DATA_SHORT)
		self.unk1,	= Vec3(f)
		self.scale,	= Vec3(f)
		self.slowdown,	= struct.unpack("f",f.read(4))
		self.unk2	= struct.unpack("5f",f.read(20))
		self.rot1,	= Vec3(f)
		self.rot2,	= Vec3(f)
		self.translation,= Vec3(f)
		self.unk3	= struct.unpack("4f",f.read(16))
		
		self.nUnk,	= struct.unpack("i",f.read(4))
		self.ofsUnk,	= struct.unpack("i",f.read(4))
		oldpos = f.tell()
		self.UnkRef = []
		f.seek(self.ofsUnk)
		for i in range(self.nUnk):
			temp = Vec3(f)
			self.UnkRef.append(temp)
		f.seek(oldpos)
		
		self.Enabled, = AnimBlock(f,DATA_INT)
		
	def pack(self):#todo
		pass
		
		
class M2File:
	def __init__(self,filename):
		f = open(filename,"r+b")
		self.hdr = M2Header(f)
		hdr = self.hdr #just spare some time in tipping
		
		f.seek(hdr.name.offset)#Go to the name
		self.name = f.read(hdr.name.count)#Read the name
		
		f.seek(hdr.global_sequences.offset)#go to Global Sequences
		self.gSequ = []#Create Array for Global Sequences
		for i in range(hdr.global_sequences.count):#Loop to read all Sequences
			temp = struct.unpack("i",f.read(4))
			self.gSequ.append(temp)
			
			
		f.seek(hdr.animations.offset)
		self.animations = [] # Animations or Sequences
		for i in range(hdr.animations.count):
			temp = Sequ(f)
			self.animations.append(temp)
			
		f.seek(hdr.anim_lookup.offset)
		self.anim_lookup = []
		for i in range(hdr.anim_lookup.count):
			temp = struct.unpack("h",f.read(2))
			self.anim_lookup.append(temp)
			
		f.seek(hdr.bones.offset)
		self.bones = []
		for i in range(hdr.bones.count):
			temp = Bone(f)
			self.bones.append(temp)
			
		f.seek(hdr.key_bones.offset)
		self.key_bones = []
		for i in range(hdr.key_bones.count):
			temp = struct.unpack("h",f.read(2))
			self.key_bones.append(temp)
			
		f.seek(hdr.vertices.offset)
		self.vertices = []
		for i in range(hdr.vertices.count):
			temp = Vertex(f)
			self.vertices.append(temp)
			
		f.seek(hdr.colors.offset)
		self.colors = []
		for i in range(hdr.colors.count):
			temp = Color(f)
			self.color.append(temp)
			
		f.seek(hdr.textures.offset)
		self.textures = []
		for i in range(hdr.textures.count):
			temp = Texture(f)
			self.textures.append(temp)
			
		f.seek(hdr.transparency.offset)
		self.transparency = []
		for i in range(hdr.transparency.count):
			temp = AnimBlock(f,DATA_SHORT)
			self.transparency.append(temp)
		
		f.seek(hdr.uv_anim.offset)
		self.uv_anim = []
		for i in range(hdr.uv_anim.count):
			temp = UVAnimation(f)
			self.uv_anim.append(temp)
		
		
		f.seek(hdr.tex_replace.offset)
		self.tex_replace = []
		for i in range(hdr.tex_replace.count):
			temp = struct.unpack("h",f.read(2))
			self.tex_replace.append(temp)
		
		f.seek(hdr.render_flags.offset)
		self.renderflags = []
		for i in range(hdr.render_flags.count):
			temp = Renderflags(f)
			self.renderflags.append(temp)

		f.seek(hdr.bone_lookup.offset)
		self.bone_lookup = []
		for i in range(hdr.bone_lookup.count):
			temp = struct.unpack("h",f.read(2))
			self.bone_lookup.append(temp)
			
		f.seek(hdr.tex_lookup.offset)
		self.tex_lookup = []
		for i in range(hdr.tex_lookup.count):
			temp = struct.unpack("h",f.read(2))
			self.tex_lookup.append(temp)
			
		f.seek(hdr.tex_units.offset)
		self.tex_units = []
		for i in range(hdr.tex_units.count):
			temp = struct.unpack("h",f.read(2))
			self.tex_units.append(temp)	
		
		f.seek(hdr.trans_lookup.offset)
		self.trans_lookup = []
		for i in range(hdr.trans_lookup.count):
			temp = struct.unpack("h",f.read(2))
			self.trans_lookup.append(temp)
		
		f.seek(hdr.uv_anim_lookup.offset)
		self.uv_anim_lookup = []
		for i in range(hdr.uv_anim_lookup.count):
			temp = struct.unpack("h",f.read(2))
			self.uv_anim_lookup.append(temp)

		f.seek(hdr.bounding_triangles.offset)
		self.bounding_triangles = []
		for i in range(hdr.bounding_triangles.count / 3):
			temp = struct.unpack("3H",f.read(6))
			self.bounding_triangles.append(temp)
			
		f.seek(hdr.bounding_vertices.offset)
		self.bounding_vertices = []
		for i in range(hdr.bounding_vertices.count):
			temp = Vec3(f)
			self.bounding_vertices.append(temp)
			
		f.seek(hdr.bounding_normals.offset)
		self.bounding_normals = []
		for i in range(hdr.bounding_normals.count):
			temp = Vec3(f)
			self.bounding_normals.append(temp)
			
		f.seek(hdr.attachments.offset)
		self.attachments = []
		for i in range(hdr.attachments.count):
			temp = Attachment(f)
			self.attachments.append(temp)
			
		f.seek(hdr.attach_lookup.offset)
		self.attach_lookup = []
		for i in range(hdr.attach_lookup.count):
			temp = struct.unpack("h",f.read(2))
			self.attach_lookup.append(temp)
			

		