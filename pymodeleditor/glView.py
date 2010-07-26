# -*- coding: utf-8 -*-

from OpenGL.GL import *
from PyQt4 import QtCore, QtGui, QtOpenGL

from m2 import *
from skin import *

LeftMouse = 0x1
RightMouse = 0x2
MidMouse = 0x4

ColPurple = QtGui.QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)


class GlWidget(QtOpenGL.QGLWidget):

	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		self.thing = self.makeObject()
		self.paintGL()
		self.updateGL()

	def initializeGL(self):
		self.qglClearColor(ColPurple.dark())
		self.modelname = "Test.m2"
		self.m2 = M2File(self.modelname)
		self.skinname = self.modelname[0:len(self.modelname)-3]+"00.skin"
		self.skin = SkinFile(self.skinname)
		self.xRot = 0
		self.yRot = 0
		self.zRot = 0
		self.mscale = 0.1
		#enable transparency
		glEnable (GL_BLEND)
		glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		self.thing = self.makeObject()
		glShadeModel(GL_FLAT)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_CULL_FACE)


	def makeObject(self):
		
		liste = glGenLists(1)
		glNewList(liste, GL_COMPILE)	
		
		glPolygonMode(GL_FRONT, GL_LINE)
	
		glBegin(GL_TRIANGLES)	
		s = 0	
		transparency = 1.0
		for i in self.skin.mesh:
			for j in self.skin.texunit:
				if j.submesh == s:
					try:
						transparency = self.m2.transparency[self.m2.trans_lookup[j.transparency].Id].alpha.KeySubs[0].values[0] / float(0x7FFF)	
					except:
						print "oO"
					break
			
			for t in range(i.num_tris/3):
				try:						
					v1 = self.m2.vertices[self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[0]].Id]
					v2 = self.m2.vertices[self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[1]].Id]
					v3 = self.m2.vertices[self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[2]].Id]
					glColor4f(0.0,0.0,1.0,transparency)
					glVertex3f(v1.pos.x*self.mscale,v1.pos.y*self.mscale,v1.pos.z*self.mscale)
					glVertex3f(v2.pos.x*self.mscale,v2.pos.y*self.mscale,v2.pos.z*self.mscale)
					
					glVertex3f(v3.pos.x*self.mscale,v3.pos.y*self.mscale,v3.pos.z*self.mscale)
					glColor3f(1.0,1.0,1.0)
				except Exception, e:
					print e
					#print "Vertex: " + str(t) + " failed"
			s += 1
		glEnd()		

		glBegin(GL_LINES)
		for i in self.m2.bones:
			if i.parent != -1:
				glColor4f(1.0,0.0,0.0,1.0)
				glVertex3f(i.pivot.x*self.mscale,i.pivot.y*self.mscale,i.pivot.z*self.mscale)
				glVertex3f(self.m2.bones[i.parent].pivot.x*self.mscale,self.m2.bones[i.parent].pivot.y*self.mscale,self.m2.bones[i.parent].pivot.z*self.mscale)
		glEnd()

		glPolygonMode(GL_FRONT, GL_FILL)
		glEndList()	
				
		return liste

	def paintGL(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glTranslated(0.0, 0.0, -10.0)
		glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0);
		glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0);
		glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0);

		glCallList(self.thing)

	def resizeGL(self,width,height):
		glViewport(0, 0, width, height)		# Reset The Current Viewport And Perspective Transformation
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0);
		glMatrixMode(GL_MODELVIEW)

	def setXRotation(self,angle):
		angle = self.normalizeAngle(angle)
		if (angle != self.xRot):
			self.xRot = angle
			self.updateGL()

	def setYRotation(self,angle):
		angle = self.normalizeAngle(angle)
		if (angle != self.yRot):
			self.yRot = angle
			self.updateGL()

	def setZRotation(self,angle):
		angle = self.normalizeAngle(angle)
		if (angle != self.zRot):
			self.zRot = angle
			self.updateGL()

	def setScale(self,scale):
		self.mscale = scale / 100.0
		glDeleteLists(self.thing,1)
		self.thing = self.makeObject()
		self.paintGL()
		self.updateGL()

	def mousePressEvent(self, event):
		self.lastPos = event.pos()

	def mouseMoveEvent(self,event):
		dx = event.x() - self.lastPos.x()
		dy = event.y() - self.lastPos.y()
		if (event.buttons() & LeftMouse):
			self.setXRotation(self.xRot + 8 * dy)
			self.setYRotation(self.yRot + 8 * dx)
		elif (event.buttons() & RightMouse):
			self.setXRotation(self.xRot + 8 * dy)
			self.setZRotation(self.zRot + 8 * dx)
		lastPos = event.pos()

	def normalizeAngle(self,angle):
		while (angle < 0):
			angle += 360*16
		while (angle > 360*16):
			angle -= 360*16
		return angle



