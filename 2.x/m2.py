#!/usr/bin/python
import struct
import array
import os

from wowfile import *


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
	def __init__(self):
		self.magic         = 808600653
		self.version        = 260
		self.name          = Chunk()
		self.modeltype    = 0
		self.global_sequences = Chunk()
		self.animations     = Chunk()
		self.anim_lookup    = Chunk()
		self.DBlock	    = Chunk()
		self.bones          = Chunk()
		self.key_bones      = Chunk()
		self.vertices       = Chunk()
		self.views        = Chunk()
		self.colors         = Chunk()
		self.textures       = Chunk()
		self.transparency	= Chunk()
		self.IBlock		= Chunk()
		self.uv_anim        = Chunk()
		self.tex_replace    = Chunk()
		self.render_flags   = Chunk()
		self.bone_lookup    = Chunk()
		self.tex_lookup     = Chunk()
		self.tex_units      = Chunk()
		self.trans_lookup   = Chunk()
		self.uv_anim_lookup = Chunk()
		self.bound	= Bounds()
		self.vbox	= Bounds()
		self.bounding_triangles = Chunk()
		self.bounding_vertices = Chunk()
		self.bounding_normals = Chunk()
		self.attachments    = Chunk()
		self.attach_lookup  = Chunk()
		self.events         = Chunk()
		self.lights         = Chunk()
		self.cameras        = Chunk()
		self.camera_lookup  = Chunk()
		self.ribbon_emitters = Chunk()
		self.particle_emitters = Chunk()	

			
	def unpack(self,f):
		self.magic,         = struct.unpack("i",f.read(4))
		self.version,        = struct.unpack("i",f.read(4))
		self.name.unpack(f)
		self.modeltype,    = struct.unpack("i",f.read(4))
		self.global_sequences.unpack(f)
		self.animations.unpack(f)
		self.anim_lookup.unpack(f)
		self.DBlock.unpack(f)
		self.bones.unpack(f)
		self.key_bones.unpack(f)
		self.vertices.unpack(f)
		self.views.unpack(f)
		self.colors.unpack(f)
		self.textures.unpack(f)
		self.transparency.unpack(f)
		self.IBlock.unpack(f)
		self.uv_anim.unpack(f)
		self.tex_replace.unpack(f)
		self.render_flags.unpack(f)
		self.bone_lookup.unpack(f)
		self.tex_lookup.unpack(f)
		self.tex_units.unpack(f)
		self.trans_lookup.unpack(f)
		self.uv_anim_lookup.unpack(f)
		self.bound.unpack(f)
		self.vbox.unpack(f)
		self.bounding_triangles.unpack(f)
		self.bounding_vertices.unpack(f)
		self.bounding_normals.unpack(f)
		self.attachments.unpack(f)
		self.attach_lookup.unpack(f)
		self.events.unpack(f)
		self.lights.unpack(f)
		self.cameras.unpack(f)
		self.camera_lookup.unpack(f)
		self.ribbon_emitters.unpack(f)
		self.particle_emitters.unpack(f)	
		
	def pack(self):
		ret = struct.pack("i",self.magic)
		ret += struct.pack("i",self.version)
		ret += self.name.pack()
		ret += struct.pack("i",self.modeltype)
		ret += self.global_sequences.pack()
		ret += self.animations.pack()
		ret += self.anim_lookup.pack()
		ret += self.DBlock.pack()
		ret += self.bones.pack()
		ret += self.key_bones.pack()
		ret += self.vertices.pack()
		ret += self.views.pack()
		ret += self.colors.pack()
		ret += self.textures.pack()
		ret += self.transparency.pack()
		ret += self.IBlock.pack()
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
		return ret


class AnimBlock:
	def __init__(self):
		self.interpolation= 0
		self.gsequ	= -1
		self.nRanges	= 0
		self.ofsRanges	= 0
		self.Ranges	= []
		self.nTimes	= 0
		self.ofsTimes	= 0		
		self.Times	= []
		self.nKeys	= 0
		self.ofsKeys	= 0
		self.Keys	= []

		self.type = DATA_INT


	def unpack(self,f,type):
		self.type = type
		self.interpolation,= struct.unpack("h",f.read(2))
		self.gsequ,	= struct.unpack("h",f.read(2))

		self.nRanges,	= struct.unpack("i",f.read(4))
		self.ofsRanges,	= struct.unpack("i",f.read(4))
		
		oldpos = f.tell()
		f.seek(self.ofsRanges)
		self.Ranges = []
		for i in xrange(self.nRanges):
			temp = Range().unpack(f)
			self.Ranges.append(temp)
		f.seek(oldpos)

		self.nTimes,	= struct.unpack("i",f.read(4))
		self.ofsTimes,	= struct.unpack("i",f.read(4))
		
		oldpos = f.tell()
		f.seek(self.ofsTimes)
		self.Times = []
		for i in xrange(self.nTimes):
			temp, = struct.unpack("i",f.read(4))
			self.Times.append(temp)
		f.seek(oldpos)
		
		self.nKeys,	= struct.unpack("i",f.read(4))
		self.ofsKeys,	= struct.unpack("i",f.read(4))
		
		oldpos = f.tell()
		f.seek(self.ofsKeys)
		self.Keys = []
		for i in xrange(self.nKeys):
			if(type == DATA_QUAT):
				temp = Quat().unpack(f)
				self.Keys.append(temp)
			elif(type == DATA_VEC3):
				temp = Vec3().unpack(f)
				self.Keys.append(temp)
			elif(type == DATA_INT):
				temp, = struct.unpack("i",f.read(4))
				self.Keys.append(temp)
			elif(type == DATA_SHORT):
				temp, = struct.unpack("h",f.read(2))
				self.Keys.append(temp)
			elif(type == DATA_VEC2):
				temp = Vec2().unpack(f)
				self.Keys.append(temp)
			elif(type == DATA_VEC9):
				temp = Vec9().unpack(f)
				self.Keys.append(temp)
			elif(type == DATA_FLOAT):
				temp, = struct.unpack("f",f.read(4))
				self.Keys.append(temp)
			else:
				pass
		f.seek(oldpos)
		return self

	def pack(self):
		ret = struct.pack("h",self.interpolation)
		ret += struct.pack("h",self.gsequ)
		ret += struct.pack("i",self.nRanges)
		ret += struct.pack("i",self.ofsRanges)
		ret += struct.pack("i",self.nTimes)
		ret += struct.pack("i",self.ofsTimes)
		ret += struct.pack("i",self.nKeys)
		ret += struct.pack("i",self.ofsKeys)
		return ret


class GlobalSequence:
	def __init__(self):
		self.Timestamp = 0
	def unpack(self,f):
		self.Timestamp, = struct.unpack("i",f.read(4))
		return self
	def pack(self):
		return struct.pack("i",self.Timestamp)

class Sequ:
	def __init__(self):
		self.animId	= 0
		self.start	= 0
		self.end	= 0
		self.moveSpeed	= 0
		self.flags	= 0
		self.unk	=(0,0)
		self.playSpeed	= 0
		self.bound	= Bounds()
		self.next	= 0
		self.index	= 0
		
	def unpack(self,f):
		self.animId,	= struct.unpack("i",f.read(4))
		self.start,	= struct.unpack("i",f.read(4))
		self.end,	= struct.unpack("i",f.read(4))
		self.moveSpeed,	= struct.unpack("f",f.read(4))
		self.flags,	= struct.unpack("i",f.read(4))
		self.unk	= struct.unpack("3i",f.read(12))
		self.playSpeed,	= struct.unpack("i",f.read(4))
		self.bound.unpack(f)
		self.next,	= struct.unpack("h",f.read(2))
		self.index,	= struct.unpack("H",f.read(2))
		return self
	def pack(self):
		ret = struct.pack("i",self.animId)
		ret += struct.pack("i",self.start)
		ret += struct.pack("i",self.end)
		ret += struct.pack("f",self.moveSpeed)
		ret += struct.pack("i",self.flags)
		ret += struct.pack("2i",self.unk[0],self.unk[1])
		ret += struct.pack("i",self.playSpeed)
		ret += self.bound.pack()
		ret += struct.pack("h",self.next)
		ret += struct.pack("H",self.index)
		return ret

class Bone:
	def __init__(self):
		self.KeyBoneId	= 0
		self.flags	= 0
		self.parent	= 0
		self.unk	= (0,0,0)
		self.translation= AnimBlock()
		self.rotation	= AnimBlock()
		self.scaling	= AnimBlock()
		self.pivot	= Vec3()
	def unpack(self,f):
		self.KeyBoneId,	= struct.unpack("i",f.read(4))
		self.flags,	= struct.unpack("i",f.read(4))
		self.parent,	= struct.unpack("h",f.read(2))
		self.unk	= struct.unpack("3h",f.read(6))
		self.translation= AnimBlock().unpack(f,DATA_VEC3)
		self.rotation	= AnimBlock().unpack(f,DATA_QUAT)
		self.scaling	= AnimBlock().unpack(f,DATA_VEC3)
		self.pivot	= Vec3().unpack(f)
		return self
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


class Vertex:
	def __init__(self):
		self.pos        = (0,0,0)
		self.bweights   = (0,0,0,0)
		self.bindices   = (0,0,0,0)
		self.normal     = (0,0,0)
		self.uv         = (0,0)
		self.unk         = (0,0)
		
	def unpack(self,f):
		self.pos        = struct.unpack("3f",f.read(12))
		self.bweights   = struct.unpack("4B",f.read(4))
		self.bindices   = struct.unpack("4B",f.read(4))
		self.normal     = struct.unpack("3f",f.read(12))
		self.uv         = struct.unpack("2f",f.read(8))
		self.unk         = struct.unpack("2f",f.read(8))
		return self
	def pack(self):
		ret = struct.pack("3f",self.pos[0],self.pos[1],self.pos[2])
		ret += struct.pack("4B",self.bweights[0],self.bweights[1],self.bweights[2],self.bweights[3])
		ret += struct.pack("4B",self.bindices[0],self.bindices[1],self.bindices[2],self.bindices[3])
		ret += struct.pack("3f",self.normal[0],self.normal[1],self.normal[2])
		ret += struct.pack("2f",self.uv[0],self.uv[1])
		ret += struct.pack("2f",self.unk[0],self.unk[1])
		return ret

class Views:
	def __init__(self):
		self.Indices        = Chunk()
		self.Triangles      = Chunk()
		self.Properties     = Chunk()
		self.Submeshes      = Chunk()
		self.TextureUnits   = Chunk()
		self.lod	    = 0
	def unpack(self,f):
		self.Indices.unpack(f)
		self.Triangles.unpack(f)
		self.Properties.unpack(f)
		self.Submeshes.unpack(f)
		self.TextureUnits.unpack(f)
		self.lod,	    = struct.unpack("i",f.read(4))
		return self
	def pack(self):
		ret =  self.Indices.pack()
		ret +=  self.Triangles.pack()
		ret +=  self.Properties.pack()
		ret +=  self.Submeshes.pack()
		ret +=  self.TextureUnits.pack()
		ret += struct.pack("i", self.lod)
		return ret

class Mesh:
	def __init__(self):
		self.mesh_id		= 0
		self.vert_offset	= 0
		self.num_verts		= 0
		self.tri_offset	= 0
		self.num_tris		= 0
		self.num_bones		= 0
		self.start_bone		= 0
		self.unknown		= 0
		self.rootbone		= 0
		self.bound		= Bounds()
		
	def unpack(self,f):
		self.mesh_id,		= struct.unpack("i",f.read(4))
		self.vert_offset,	= struct.unpack("H",f.read(2))
		self.num_verts,		= struct.unpack("H",f.read(2))
		self.tri_offset,	= struct.unpack("H",f.read(2))
		self.num_tris,		= struct.unpack("H",f.read(2))
		self.num_bones,		= struct.unpack("H",f.read(2))
		self.start_bone,	= struct.unpack("H",f.read(2))
		self.unknown,		= struct.unpack("H",f.read(2))
		self.rootbone,		= struct.unpack("H",f.read(2))
		self.bound.unpack(f)
		return self
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
	def __init__(self):
		self.flags         = 0
		self.shading	    = 0
		self.submesh       = 0
		self.submesh2      = 0
		self.color         = -1
		self.renderflag    = 0
		self.texunit 	    = 0
		self.mode          = 0
		self.texture       = 0
		self.texunit2      = 0
		self.transparency  = 0
		self.animation      = 0
	def unpack(self,f):
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
		return self
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

class Propertie:
	def __init__(self):
		self.Bones = (0,0,0,0)
	def unpack(self,f):
		self.Bones = struct.unpack("4b",f.read(4))
		return self
	def pack(self):
		return struct.pack("4b",self.Bones[0],self.Bones[1],self.Bones[2],self.Bones[3])



class Renderflags:
	def __init__(self):
		self.flags	= 0
		self.blend	= 0
	def unpack(self,f):
		self.flags,	= struct.unpack("h",f.read(2))
		self.blend,	= struct.unpack("h",f.read(2))
		return self
	def pack(self):
		ret = struct.pack("h",self.flags)
		ret += struct.pack("h",self.blend)
		return ret

class Color:
	def __init__(self):
		self.color = AnimBlock()
		self.alpha = AnimBlock()
	def unpack(self,f):
		self.color = AnimBlock().unpack(f,DATA_VEC3)
		self.alpha = AnimBlock().unpack(f,DATA_SHORT)	
		return self
	def pack(self):
		ret = self.color.pack()
		ret += self.alpha.pack()
		return ret

class Transparency:
	def __init__(self):
		self.alpha = AnimBlock()
	def unpack(self,f):
		self.alpha = AnimBlock().unpack(f,DATA_SHORT)	
		return self
	def pack(self):
		return self.alpha.pack()
	

class Texture:
	def __init__(self):
		self.type	= 0
		self.flags	=0
		self.len_name	= 0
		self.ofs_name	= 0
		self.name = ""
		
	def unpack(self,f):
		self.type,	= struct.unpack("i",f.read(4))
		self.flags,	= struct.unpack("i",f.read(4))
		self.len_name,	= struct.unpack("i",f.read(4))
		self.ofs_name,	= struct.unpack("i",f.read(4))
		oldpos = f.tell()
		f.seek(self.ofs_name)
		self.name = f.read(self.len_name)
		f.seek(oldpos)
		return self
	def pack(self):
		ret = struct.pack("i",self.type)
		ret += struct.pack("i",self.flags)
		ret += struct.pack("i",self.len_name)
		ret += struct.pack("i",self.ofs_name)
		return ret


class UVAnimation:
	def __init__(self):
		self.translation= AnimBlock()
		self.rotation	= AnimBlock()
		self.scaling	= AnimBlock()
	def unpack(self,f):
		self.translation= AnimBlock().unpack(f,DATA_VEC3)
		self.rotation	= AnimBlock().unpack(f,DATA_QUAT)
		self.scaling	= AnimBlock().unpack(f,DATA_VEC3)	
		return self
	def pack(self):
		ret = self.translation.pack()
		ret += self.rotation.pack()
		ret += self.scaling.pack()
		return ret

class Ribbon:
	def __init__(self):
		self.Id	= 0
		self.Bone	= 0
		self.Pos	= Vec3()
		self.nTexRefs	= 0
		self.ofsTexRefs= 0
		self.TexRefs = []
		
		self.nBlendRef	= 0
		self.ofsBlendRef= 0
		self.BlendRef = []

		
		self.Color	= AnimBlock()
		self.Opacity	= AnimBlock()
		self.Above	= AnimBlock()
		self.Below	= AnimBlock()
		
		self.Resolution = 0
		self.Length	= 0
		self.Angle	= 0
		self.Flags	= 0
		self.Blend	= 0
		
		self.Unk1	= AnimBlock()
		self.Unk2	= AnimBlock()
		
		
	def unpack(self,f):
		self.Id,	= struct.unpack("i",f.read(4))
		self.Bone,	= struct.unpack("i",f.read(4))
		self.Pos	= Vec3().unpack(f)
		self.nTexRefs,	= struct.unpack("i",f.read(4))
		self.ofsTexRefs,= struct.unpack("i",f.read(4))
		oldpos = f.tell()
		f.seek(self.ofsTexRefs)
		self.TexRefs = []
		for i in xrange(self.nTexRefs):
			temp, = struct.unpack("i",f.read(4))
			self.TexRefs.append(temp)
		f.seek(oldpos)
		
		self.nBlendRef,	= struct.unpack("i",f.read(4))
		self.ofsBlendRef,= struct.unpack("i",f.read(4))
		oldpos = f.tell()
		f.seek(self.ofsBlendRef)
		self.BlendRef = []
		for i in xrange(self.nBlendRef):
			temp, = struct.unpack("i",f.read(4))
			self.BlendRef.append(temp)
		f.seek(oldpos)
		
		self.Color	= AnimBlock().unpack(f,DATA_VEC3)
		self.Opacity	= AnimBlock().unpack(f,DATA_SHORT)
		self.Above	= AnimBlock().unpack(f,DATA_FLOAT)
		self.Below	= AnimBlock().unpack(f,DATA_FLOAT)
		
		self.Resolution,= struct.unpack("f",f.read(4))
		self.Length,	= struct.unpack("f",f.read(4))
		self.Angle,	= struct.unpack("f",f.read(4))
		self.Flags,	= struct.unpack("h",f.read(2))
		self.Blend,	= struct.unpack("h",f.read(2))
		
		self.Unk1	= AnimBlock().unpack(f,DATA_SHORT)
		self.Unk2	= AnimBlock().unpack(f,DATA_INT)
		
		#self.pad,	= struct.unpack("i",f.read(4))
		return self
	def pack(self):
		ret = struct.pack("i",self.Id)
		ret += struct.pack("i",self.Bone)
		ret += self.Pos.pack()
		ret += struct.pack("i",self.nTexRefs)
		ret += struct.pack("i",self.ofsTexRefs)
		ret += struct.pack("i",self.nBlendRef)
		ret += struct.pack("i",self.ofsBlendRef)
		ret += self.Color.pack()
		ret += self.Opacity.pack()
		ret += self.Above.pack()
		ret += self.Below.pack()
		ret += struct.pack("f",self.Resolution)
		ret += struct.pack("f",self.Length)
		ret += struct.pack("f",self.Angle)
		ret += struct.pack("h",self.Flags)
		ret += struct.pack("h",self.Blend)
		ret += self.Unk1.pack()
		ret += self.Unk2.pack()
		#ret += struct.pack("i",self.pad)
		return ret




class Particle:
	def __init__(self):
		self.Id = 0
	def unpack(self,f):
		self.Id,	= struct.unpack("i",f.read(4))
		self.Flags,	= struct.unpack("i",f.read(4))
		self.Pos	= Vec3().unpack(f)
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

		self.emission_speed = AnimBlock().unpack(f,DATA_FLOAT)
		self.speed_var = AnimBlock().unpack(f,DATA_FLOAT)
		self.vert_range = AnimBlock().unpack(f,DATA_FLOAT)
		self.hor_range = AnimBlock().unpack(f,DATA_FLOAT)
		self.gravity = AnimBlock().unpack(f,DATA_FLOAT)
		self.lifespan = AnimBlock().unpack(f,DATA_FLOAT)
		self.emission_rate = AnimBlock().unpack(f,DATA_FLOAT)

		self.emission_area_len = AnimBlock().unpack(f,DATA_FLOAT)
		self.emission_area_width = AnimBlock().unpack(f,DATA_FLOAT)
		self.gravity2 = AnimBlock().unpack(f,DATA_FLOAT)

		#lazyness blah :/
		self.floats = []
		for i in range(72):
			self.floats.append(struct.unpack("f",f.read(4)))
		
		self.Enabled = AnimBlock().unpack(f,DATA_INT)
		
		return self
	def pack(self):
		ret = struct.pack("i",self.Id)
		ret += struct.pack("i",self.Flags)
		ret += self.Pos.pack()
		ret += struct.pack("h",self.bone)
		ret += struct.pack("h",self.texture)
		
		ret += struct.pack("i",self.lenModel)
		ret += struct.pack("i",self.ofsModel)
		ret += struct.pack("i",self.lenParticle)
		ret += struct.pack("i",self.ofsParticle)
		
		ret += struct.pack("b",self.blend)
		ret += struct.pack("b",self.emitter)
		ret += struct.pack("h",self.color_dbc)
		ret += struct.pack("b",self.particletype)
		ret += struct.pack("b",self.head_or_tail)
		ret += struct.pack("h",self.tex_tile_rot)
		ret += struct.pack("h",self.tex_rows)
		ret += struct.pack("h",self.tex_cols)
		
		ret += self.emission_speed.pack()
		ret += self.speed_var.pack()
		ret += self.vert_range.pack()
		ret += self.hor_range.pack()
		ret += self.gravity.pack()
		ret += self.lifespan.pack()
		ret += self.emission_rate.pack()
		ret += self.emission_area_len.pack()
		ret += self.emission_area_width.pack()
		ret += self.gravity2.pack()

		
		for i in range(72):
			ret += struct.pack("f",self.floats[i])

		
		ret += self.Enabled.pack()
		
		return ret


class Light:
	def __init__(self):
		self.Type	= 0
		self.Bone	= 0
		self.Pos	= Vec3()
		self.AmbientCol	= AnimBlock()
		self.AmbientInt	= AnimBlock()
		self.DiffuseCol	= AnimBlock()
		self.DiffuseInt	= AnimBlock()
		self.AttStart	= AnimBlock()
		self.AttEnd	= AnimBlock()
		self.Enabled	= AnimBlock()
	def unpack(self,f):
		self.Type,	= struct.unpack("h",f.read(2))
		self.Bone,	= struct.unpack("h",f.read(2))
		self.Pos	= Vec3().unpack(f)
		self.AmbientCol	= AnimBlock().unpack(f,DATA_VEC3)
		self.AmbientInt	= AnimBlock().unpack(f,DATA_FLOAT)
		self.DiffuseCol	= AnimBlock().unpack(f,DATA_VEC3)
		self.DiffuseInt	= AnimBlock().unpack(f,DATA_FLOAT)
		self.AttStart	= AnimBlock().unpack(f,DATA_FLOAT)
		self.AttEnd	= AnimBlock().unpack(f,DATA_FLOAT)
		self.Enabled	= AnimBlock().unpack(f,DATA_INT)
		return self
	def pack(self):
		ret = struct.pack("h",self.Type)
		ret += struct.pack("h",self.Bone)
		ret += self.Pos.pack()
		ret += self.AmbientCol.pack()
		ret += self.AmbientInt.pack()
		ret += self.DiffuseCol.pack()
		ret += self.DiffuseInt.pack()
		ret += self.AttStart.pack()
		ret += self.AttEnd.pack()
		ret += self.Enabled.pack()
		return ret

class Camera:
	def __init__(self):
		self.Type	= 0
		self.FOV	= 0
		self.FarClip	= 0
		self.NearClip	= 0
		self.TransPos	= AnimBlock()
		self.Pos	= Vec3()
		self.TransTar	= AnimBlock()
		self.Target	= Vec3()
		self.Scaling	= AnimBlock()
		
	def unpack(self,f):
		self.Type,	= struct.unpack("i",f.read(4))
		self.FOV,	= struct.unpack("f",f.read(4))
		self.FarClip,	= struct.unpack("f",f.read(4))
		self.NearClip,	= struct.unpack("f",f.read(4))
		self.TransPos	= AnimBlock().unpack(f,DATA_VEC9)
		self.Pos	= Vec3().unpack(f)
		self.TransTar	= AnimBlock().unpack(f,DATA_VEC9)
		self.Target	= Vec3().unpack(f)
		self.Scaling	= AnimBlock().unpack(f,DATA_VEC3)
		return self
	def pack(self):
		ret = struct.pack("i",self.Type)
		ret += struct.pack("f",self.FOV)
		ret += struct.pack("f",self.FarClip)
		ret += struct.pack("f",self.NearClip)
		ret += self.TransPos.pack()
		ret += self.Pos.pack()
		ret += self.TransTar.pack()
		ret += self.Target.pack()
		ret += self.Scaling.pack()
		return ret


class Attachment:
	def __init__(self):
		self.Id	= 0
		self.bone	= 0
		self.pos	= Vec3()
		self.Enabled	= AnimBlock()
	def unpack(self,f):
		self.Id,	= struct.unpack("i",f.read(4))
		self.bone,	= struct.unpack("i",f.read(4))
		self.pos	= Vec3().unpack(f)
		self.Enabled	= AnimBlock().unpack(f,DATA_INT)
		return self
	def pack(self):
		ret = struct.pack("i",self.Id)
		ret += struct.pack("i",self.bone)
		ret += self.pos.pack()
		ret += self.Enabled.pack()
		return ret


class DUnknown:
	def __init__(self):
		self.a = 0
		self.b = 0
	def unpack(self,f):
		self.a, = struct.unpack("i",f.read(4))
		self.b, = struct.unpack("i",f.read(4))
	def pack(self):
		ret = struct.pack("i",self.a)
		ret += struct.pack("i",self.b)
		return ret

class Event:
	def __init__(self):
		self.Id	= 0
		self.Data	= 0
		self.Bone	= 0
		self.Pos	= Vec3()
		self.interpolation= 0
		self.gsequ	= 0
		
		self.nRanges	= 0
		self.ofsRange	= 0

		self.Ranges = []

		self.nTimes	= 0
		self.ofsTimes	= 0

		self.Times = []

		
	def unpack(self,f):
		self.Id,	= struct.unpack("i",f.read(4))
		self.Data,	= struct.unpack("i",f.read(4))
		self.Bone,	= struct.unpack("i",f.read(4))
		self.Pos	= Vec3().unpack(f)
		self.interpolation,= struct.unpack("h",f.read(2))
		self.gsequ,	= struct.unpack("h",f.read(2))

		self.nRanges,	= struct.unpack("i",f.read(4))
		self.ofsRanges,	= struct.unpack("i",f.read(4))
		
		oldpos = f.tell()
		f.seek(self.ofsRanges)
		self.Ranges = []
		for i in xrange(self.nRanges):
			temp = Range().unpack(f)
			self.Ranges.append(temp)
		f.seek(oldpos)

		self.nTimes,	= struct.unpack("i",f.read(4))
		self.ofsTimes,	= struct.unpack("i",f.read(4))
		
		oldpos = f.tell()
		f.seek(self.ofsTimes)
		self.Times = []
		for i in xrange(self.nTimes):
			temp, = struct.unpack("i",f.read(4))
			self.Times.append(temp)
		f.seek(oldpos)
		return self
	def pack(self):
		ret = struct.pack("i",self.Id)
		ret += struct.pack("i",self.Data)
		ret += struct.pack("i",self.Bone)
		ret += self.Pos.pack()
		ret += struct.pack("h",self.interpolation)
		ret += struct.pack("h",self.gsequ)
		ret += struct.pack("i",self.nRanges)
		ret += struct.pack("i",self.ofsRanges)
		ret += struct.pack("i",self.nTimes)
		ret += struct.pack("i",self.ofsTimes)
		return ret


def WriteAnimBlock(f,block):
	if(block.nTimes != 0):
		block.ofsRanges = f.tell()
	
		for j in block.Ranges:
			f.write(j.pack())
		FillLine(f)


		block.ofsTimes = f.tell()
	
		for j in block.Times:
			f.write(struct.pack("i",j))
		FillLine(f)

	
	
		block.ofsKeys = f.tell()

		for j in block.Keys:
			if(block.type == DATA_QUAT):
				f.write(j.pack())
			elif(block.type == DATA_VEC3):
				f.write(j.pack())
			elif(block.type == DATA_INT):
				f.write(struct.pack("i",j))
			elif(block.type == DATA_SHORT):
				f.write(struct.pack("h",j))
			elif(block.type == DATA_VEC2):
				f.write(j.pack())
			elif(block.type == DATA_VEC9):
				f.write(j.pack())
			elif(block.type == DATA_FLOAT):
				f.write(struct.pack("f",j))
			else:	
				pass
		FillLine(f)

	else:
		block.ofsTimes = 0
		block.ofsRanges = 0
		block.ofsKeys = 0


class M2File:
	def __init__(self,filename):
		f = open(filename,"r+b")
		self.hdr = M2Header()
		self.hdr.unpack(f)
		hdr = self.hdr #just spare some time in tipping
		
		f.seek(hdr.name.offset)#Go to the name
		self.name = f.read(hdr.name.count)#Read the name
		#Read Blocks
		self.gSequ		= ReadBlock(f,hdr.global_sequences,GlobalSequence)			
		self.animations		= ReadBlock(f,hdr.animations,Sequ)
		self.anim_lookup	= ReadBlock(f,hdr.anim_lookup,Lookup)		
		self.dblock		= ReadBlock(f,hdr.DBlock,DUnknown)
		self.bones 		= ReadBlock(f,hdr.bones,Bone)
		self.key_bones 		= ReadBlock(f,hdr.key_bones,Lookup)
		self.vertices 		= ReadBlock(f,hdr.vertices,Vertex)
		self.views 		= ReadBlock(f,hdr.views,Views)
		#todo: Check if they're relative or absolute in the file!
		self.indices		= []
		self.triangles		= []
		self.properties		= []
		self.submeshes		= []
		self.materials		= []
		for i in range(self.hdr.views.count):
			self.indices.append(ReadBlock(f,self.views[i].Indices,Lookup))
			self.triangles.append(ReadBlock(f,self.views[i].Triangles,Triangle))
			self.properties.append(ReadBlock(f,self.views[i].Properties,Propertie))
			self.submeshes.append(ReadBlock(f,self.views[i].Submeshes,Mesh))
			self.materials.append(ReadBlock(f,self.views[i].TextureUnits,Material))

		self.colors		= ReadBlock(f,hdr.colors,Color)
		self.textures 		= ReadBlock(f,hdr.textures,Texture)	
		self.transparency 	= ReadBlock(f,hdr.transparency,Transparency)	
		#self.iblock	 	= ReadBlock(f,hdr.IBlock,IUnknown)
		self.uv_anim 		= ReadBlock(f,hdr.uv_anim,UVAnimation)
		self.tex_replace 	= ReadBlock(f,hdr.tex_replace,Lookup)
		self.renderflags 	= ReadBlock(f,hdr.render_flags,Renderflags)
		self.bone_lookup 	= ReadBlock(f,hdr.bone_lookup,Lookup)
		self.tex_lookup 	= ReadBlock(f,hdr.tex_lookup,Lookup)
		self.tex_units		= ReadBlock(f,hdr.tex_units,Lookup)
		self.trans_lookup 	= ReadBlock(f,hdr.trans_lookup,Lookup)
		self.uv_anim_lookup 	= ReadBlock(f,hdr.uv_anim_lookup,Lookup)
		self.bounding_triangles = ReadBlock(f,hdr.bounding_triangles,Triangle)
		self.bounding_vertices	= ReadBlock(f,hdr.bounding_vertices,Vec3)
		self.bounding_normals	= ReadBlock(f,hdr.bounding_normals,Vec3)
		self.attachments	= ReadBlock(f,hdr.attachments,Attachment)
		self.attach_lookup	= ReadBlock(f,hdr.attach_lookup,Lookup)
		self.events		= ReadBlock(f,hdr.events,Event)
		self.lights		= ReadBlock(f,hdr.lights,Light)
		self.cameras		= ReadBlock(f,hdr.cameras,Camera)
		self.camera_lookup 	= ReadBlock(f,hdr.camera_lookup,Lookup)
		self.ribbon_emitters	= ReadBlock(f,hdr.ribbon_emitters,Ribbon)
		self.particle_emitters	= ReadBlock(f,hdr.particle_emitters,Particle)
			
		f.close()


	def write(self,filename):
		f = open(filename,"w+b")
		
		tempname = filename[0:len(filename)-3]
		
		f.seek(0)
		f.write(self.hdr.pack())
		FillLine(f)
		
		self.hdr.name.offset = f.tell()
		f.write(self.name)
		FillLine(f)
		
		WriteBlock(f,self.hdr.global_sequences,self.gSequ)			
		WriteBlock(f,self.hdr.animations,self.animations)		
		WriteBlock(f,self.hdr.anim_lookup,self.anim_lookup)


		######bones#####
		
		WriteBlock(f,self.hdr.bones,self.bones)
		for i in self.bones:
			WriteAnimBlock(f,i.translation)
			WriteAnimBlock(f,i.rotation)
			WriteAnimBlock(f,i.scaling)
		oldpos = f.tell()
		f.seek(self.hdr.bones.offset)
		WriteBlock(f,self.hdr.bones,self.bones)
		f.seek(oldpos)
		
		
		WriteBlock(f,self.hdr.key_bones,self.key_bones)
		WriteBlock(f,self.hdr.vertices,self.vertices )


		##### views #####
		WriteBlock(f,self.hdr.views,self.views)
		for i in range(self.hdr.views.count):
			WriteBlock(f,self.views[i].Indices,self.indices[i])
			WriteBlock(f,self.views[i].Triangles,self.triangles[i])
			WriteBlock(f,self.views[i].Properties,self.properties[i])
			WriteBlock(f,self.views[i].Submeshes,self.submeshes[i])
			WriteBlock(f,self.views[i].TextureUnits,self.materials[i])		
		oldpos = f.tell()
		f.seek(self.hdr.views.offset)
		WriteBlock(f,self.hdr.views,self.views)
		f.seek(oldpos)
		
		


		######colors######
		
		WriteBlock(f,self.hdr.colors,self.colors)
		for i in self.colors:
			WriteAnimBlock(f,i.color)
			WriteAnimBlock(f,i.alpha)
		oldpos = f.tell()
		f.seek(self.hdr.colors.offset)
		WriteBlock(f,self.hdr.colors,self.colors)
		f.seek(oldpos)	


		####textures####
		
		WriteBlock(f,self.hdr.textures,self.textures )	
		for i in self.textures:
			i.ofs_name = f.tell()
			f.write(i.name)
			FillLine(f)
		oldpos = f.tell()
		f.seek(self.hdr.textures.offset)
		WriteBlock(f,self.hdr.textures,self.textures)
		f.seek(oldpos)	


		####transparency#####
		
		WriteBlock(f,self.hdr.transparency,self.transparency)
		for i in self.transparency:
			WriteAnimBlock(f,i.alpha)
		oldpos = f.tell()
		f.seek(self.hdr.transparency.offset)
		WriteBlock(f,self.hdr.transparency,self.transparency)
		f.seek(oldpos)	

		####uv animation#####
		
		WriteBlock(f,self.hdr.uv_anim,self.uv_anim )
		for i in self.uv_anim:
			WriteAnimBlock(f,i.translation)
			WriteAnimBlock(f,i.rotation)
			WriteAnimBlock(f,i.scaling)
		oldpos = f.tell()
		f.seek(self.hdr.uv_anim.offset)
		WriteBlock(f,self.hdr.uv_anim,self.uv_anim)
		f.seek(oldpos)	


		######lookups####		
				
		WriteBlock(f,self.hdr.tex_replace,self.tex_replace)
		WriteBlock(f,self.hdr.render_flags,self.renderflags )
		WriteBlock(f,self.hdr.bone_lookup,self.bone_lookup)
		WriteBlock(f,self.hdr.tex_lookup,self.tex_lookup)
		WriteBlock(f,self.hdr.tex_units,self.tex_units)
		WriteBlock(f,self.hdr.trans_lookup,self.trans_lookup)
		WriteBlock(f,self.hdr.uv_anim_lookup,self.uv_anim_lookup)
		WriteBlock(f,self.hdr.bounding_triangles,self.bounding_triangles)
		WriteBlock(f,self.hdr.bounding_vertices,self.bounding_vertices)
		WriteBlock(f,self.hdr.bounding_normals,self.bounding_normals)


		####attachments####
		
		WriteBlock(f,self.hdr.attachments,self.attachments)
		for i in self.attachments:
			WriteAnimBlock(f,i.Enabled)
		oldpos = f.tell()
		f.seek(self.hdr.attachments.offset)
		WriteBlock(f,self.hdr.attachments,self.attachments)
		f.seek(oldpos)	
		
		WriteBlock(f,self.hdr.attach_lookup,self.attach_lookup)


		#######events#####
		
		WriteBlock(f,self.hdr.events,self.events)
		for i in self.events:

			i.ofsTimes = f.tell()
			for j in i.Times:
				f.write(struct.pack("i",j))
			FillLine(f)

			i.ofsRanges = f.tell()
			for j in i.Ranges:
				f.write(j.pack())
			FillLine(f)

		FillLine(f)			
		oldpos = f.tell()
		f.seek(self.hdr.events.offset)
		WriteBlock(f,self.hdr.events,self.events)
		f.seek(oldpos)	
		
		####lights####

		WriteBlock(f,self.hdr.lights,self.lights)
		for i in self.lights:
			WriteAnimBlock(f,i.AmbientCol)
			WriteAnimBlock(f,i.AmbientInt)
			WriteAnimBlock(f,i.DiffuseCol)
			WriteAnimBlock(f,i.DiffuseInt)
			WriteAnimBlock(f,i.AttStart)
			WriteAnimBlock(f,i.AttEnd)
			WriteAnimBlock(f,i.Enabled)
		oldpos = f.tell()
		f.seek(self.hdr.lights.offset)
		WriteBlock(f,self.hdr.lights,self.lights)
		f.seek(oldpos)	
		
		

		#####cameras######

		WriteBlock(f,self.hdr.cameras,self.cameras)
		for i in self.cameras:
			WriteAnimBlock(f,i.TransPos)
			WriteAnimBlock(f,i.TransTar)
			WriteAnimBlock(f,i.Scaling)
		oldpos = f.tell()
		f.seek(self.hdr.cameras.offset)
		WriteBlock(f,self.hdr.cameras,self.cameras)
		f.seek(oldpos)	
		
		WriteBlock(f,self.hdr.camera_lookup,self.camera_lookup)

		#####ribbon emitters####
		
		WriteBlock(f,self.hdr.ribbon_emitters,self.ribbon_emitters)
		for i in self.ribbon_emitters:
			i.ofsTexRefs = f.tell()
			for j in i.TexRefs:
				f.write(struct.pack("i",j))
			FillLine(f)
			i.ofsBlendRef = f.tell()
			for j in i.BlendRef:
				f.write(struct.pack("i",j))
			FillLine(f)
			WriteAnimBlock(f,i.Color)
			WriteAnimBlock(f,i.Opacity)
			WriteAnimBlock(f,i.Above)
			WriteAnimBlock(f,i.Below)
			WriteAnimBlock(f,i.Unk1)
			WriteAnimBlock(f,i.Unk2)
		oldpos = f.tell()
		f.seek(self.hdr.ribbon_emitters.offset)
		WriteBlock(f,self.hdr.ribbon_emitters,self.ribbon_emitters)
		f.seek(oldpos)	

		#####Particle Emitters####
		
		WriteBlock(f,self.hdr.particle_emitters,self.particle_emitters)
		for i in self.particle_emitters:
			i.ofsModel = f.tell()
			f.write(i.ModelName)
			FillLine(f)
			i.ofsParticle = f.tell()
			f.write(i.ParticleName)
			FillLine(f)
			
			WriteAnimBlock(f,i.emission_speed)
			WriteAnimBlock(f,i.speed_var)
			WriteAnimBlock(f,i.vert_range)
			WriteAnimBlock(f,i.hor_range)
			WriteAnimBlock(f,i.gravity)
			WriteAnimBlock(f,i.lifespan)
			WriteAnimBlock(f,i.emission_rate)
			WriteAnimBlock(f,i.emission_area_len)
			WriteAnimBlock(f,i.emission_area_width)
			WriteAnimBlock(f,i.gravity2)
			WriteAnimBlock(f,i.Enabled)
			
		oldpos = f.tell()
		f.seek(self.hdr.particle_emitters.offset)
		WriteBlock(f,self.hdr.particle_emitters,self.particle_emitters)
		f.seek(oldpos)	
		
		
		
		
		
		f.seek(0,SEEK_SET)
		f.write(self.hdr.pack())
		
		f.close()

