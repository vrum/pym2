#! /usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
#
# Created: Wed May 19 12:19:34 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtOpenGL
from OpenGL.GL import *

from m2 import *
from skin import *

from transparencychooser import *
from renderflags import *
from textureeditor import *
from gsequedit import *
from uvanimeditor import *
from materialeditor import *

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
		for i in self.skin.mesh:
			transparency = self.m2.transparency[0].alpha.KeySubs[0].values[0] / float(0x7FFF)
			for t in range(i.num_tris/3):#i.tri_offset+
				try:						
					v1 = self.m2.vertices[self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[0]].Id]
					v2 = self.m2.vertices[self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[1]].Id]
					v3 = self.m2.vertices[self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[2]].Id]
					glColor4f(1.0,0.0,0.0,transparency)
					glVertex3f(v1.pos[0]*self.mscale,v1.pos[1]*self.mscale,v1.pos[2]*self.mscale)
					glColor4f(0.0,1.0,0.0,transparency)
					glVertex3f(v2.pos[0]*self.mscale,v2.pos[1]*self.mscale,v2.pos[2]*self.mscale)
					glColor4f(0.0,0.0,1.0,transparency)
					glVertex3f(v3.pos[0]*self.mscale,v3.pos[1]*self.mscale,v3.pos[2]*self.mscale)
					glColor3f(1.0,1.0,1.0)
				except:
					print "Vertex: " + str(t) + "failed"
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


class PyModelEditor(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(800, 600)

		#remove later
		modelname = "Test.m2"
		self.m2 = M2File(modelname)
		skinname = modelname[0:len(modelname)-3]+"00.skin"
		self.skin = SkinFile(skinname)

		self.openIcon = QtGui.QIcon("Icons/document-open.png")
		self.openButton = QtGui.QPushButton(self.openIcon,"Open File",Form)
		self.openButton.setGeometry(QtCore.QRect(0, 5, 92, 28))
		self.openButton.setObjectName("openButton")
		self.connect(self.openButton, QtCore.SIGNAL("clicked()"), self.openM2)

		self.saveIcon = QtGui.QIcon("Icons/document-save.png")
		self.saveButton = QtGui.QPushButton(self.saveIcon,"Save File",Form)
		self.saveButton.setGeometry(QtCore.QRect(100, 5, 92, 28))
		self.saveButton.setObjectName("saveButton")
		self.connect(self.saveButton, QtCore.SIGNAL("clicked()"), self.saveM2)

		self.Gl = GlWidget(Form)
		self.Gl.setGeometry(QtCore.QRect(10, 40, 640, 480))

		self.xslider = QtGui.QSlider(Form)
		self.xslider.setGeometry(QtCore.QRect(660,30,30,480))
		self.xslider.setRange(0,360*16)
		self.xslider.setSingleStep(16)
		self.xslider.setPageStep(15*16)
		self.xslider.setTickInterval(15*16)
		self.connect(self.xslider,QtCore.SIGNAL("valueChanged(int)"),self.Gl.setXRotation)

		self.yslider = QtGui.QSlider(Form)
		self.yslider.setGeometry(QtCore.QRect(700,30,30,480))
		self.yslider.setRange(0,360*16)
		self.yslider.setSingleStep(16)
		self.yslider.setPageStep(15*16)
		self.yslider.setTickInterval(15*16)
		self.connect(self.yslider,QtCore.SIGNAL("valueChanged(int)"),self.Gl.setYRotation)

		self.zslider = QtGui.QSlider(Form)
		self.zslider.setGeometry(QtCore.QRect(730,30,30,480))
		self.zslider.setRange(0,360*16)
		self.zslider.setSingleStep(16)
		self.zslider.setPageStep(15*16)
		self.zslider.setTickInterval(15*16)
		self.connect(self.zslider,QtCore.SIGNAL("valueChanged(int)"),self.Gl.setZRotation)

		self.scaleslider = QtGui.QSlider(Form)
		self.scaleslider.setGeometry(QtCore.QRect(760,30,30,480))
		self.scaleslider.setRange(1,500)
		self.scaleslider.setSingleStep(10)
		self.scaleslider.setPageStep(50)
		self.scaleslider.setTickInterval(50)
		self.connect(self.scaleslider,QtCore.SIGNAL("valueChanged(int)"),self.Gl.setScale)


		self.transparencyButton = QtGui.QPushButton(Form)
		self.transparencyButton.setGeometry(QtCore.QRect(10, 520, 132, 28))
		self.transparencyButton.setObjectName("transparencyButton")
		self.connect(self.transparencyButton, QtCore.SIGNAL("clicked()"), self.editTransparency)

		self.renderflagButton = QtGui.QPushButton(Form)
		self.renderflagButton.setGeometry(QtCore.QRect(140, 520, 132, 28))
		self.renderflagButton.setObjectName("renderflagButton")
		self.connect(self.renderflagButton, QtCore.SIGNAL("clicked()"), self.editRenderflags)

		self.textureButton = QtGui.QPushButton(Form)
		self.textureButton.setGeometry(QtCore.QRect(270, 520, 132, 28))
		self.textureButton.setObjectName("textureButton")
		self.connect(self.textureButton, QtCore.SIGNAL("clicked()"), self.editTextures)

		self.gsequButton = QtGui.QPushButton(Form)
		self.gsequButton.setGeometry(QtCore.QRect(10, 545, 132, 28))
		self.gsequButton.setObjectName("gsequButton")
		self.connect(self.gsequButton, QtCore.SIGNAL("clicked()"), self.editGlobalSequences)


		self.uvanimButton = QtGui.QPushButton(Form)
		self.uvanimButton.setGeometry(QtCore.QRect(140, 545, 132, 28))
		self.uvanimButton.setObjectName("uvanimButton")
		self.connect(self.uvanimButton, QtCore.SIGNAL("clicked()"), self.editUVAnimations)


		self.materialButton = QtGui.QPushButton(Form)
		self.materialButton.setGeometry(QtCore.QRect(270, 545, 132, 28))
		self.materialButton.setObjectName("materialButton")
		self.connect(self.materialButton, QtCore.SIGNAL("clicked()"), self.editMaterials)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "PyModelEditor", None, QtGui.QApplication.UnicodeUTF8))
		self.exitButton.setText(QtGui.QApplication.translate("Form", "Exit", None, QtGui.QApplication.UnicodeUTF8))
		self.okButton.setText(QtGui.QApplication.translate("Form", "Ok", None, QtGui.QApplication.UnicodeUTF8))
		self.transparencyButton.setText(QtGui.QApplication.translate("Form", "Edit Transparency", None, QtGui.QApplication.UnicodeUTF8))
		self.renderflagButton.setText(QtGui.QApplication.translate("Form", "Edit Renderflags", None, QtGui.QApplication.UnicodeUTF8))
		self.textureButton.setText(QtGui.QApplication.translate("Form", "Edit Textures", None, QtGui.QApplication.UnicodeUTF8))
		self.gsequButton.setText(QtGui.QApplication.translate("Form", "Global Sequences", None, QtGui.QApplication.UnicodeUTF8))
		self.uvanimButton.setText(QtGui.QApplication.translate("Form", "Edit UV Animations", None, QtGui.QApplication.UnicodeUTF8))
		self.materialButton.setText(QtGui.QApplication.translate("Form", "Edit Materials", None, QtGui.QApplication.UnicodeUTF8))

	def openM2(self):
		openname = QtGui.QFileDialog().getOpenFileName(self,"Open File",QtCore.QDir.currentPath())
		self.m2 = M2File(openname)
		skinname = openname[0:len(openname)-3]+"00.skin"
		self.skin = SkinFile(skinname)
		self.Gl.setModel(self.m2,self.skin)

	def saveM2(self):
		savename = QtGui.QFileDialog().getSaveFileName(self,"Save File",QtCore.QDir.currentPath())
		self.m2.write(savename)
		skinname = savename[0:len(savename)-3]+"00.skin"
		self.skin.write(skinname)

	def editTransparency(self):
		self.tChooser = TransparencyChooser()
		self.tChooser.setModel(self.m2,self.skin)
		self.tChooser.show()
		QtCore.QObject.connect(self.tChooser, QtCore.SIGNAL("accepted()"), self.setTransparency)

	def setTransparency(self):
		self.m2.transparency = self.tChooser.m2.transparency
		self.Gl.setModel(self.m2,self.skin)

	def editRenderflags(self):
		self.rfChooser = RenderFlagsEditor()
		self.rfChooser.setModel(self.m2,self.skin)
		self.rfChooser.show()
		QtCore.QObject.connect(self.rfChooser, QtCore.SIGNAL("accepted()"), self.setRenderflags)

	def setRenderflags(self):
		self.m2.renderflags = self.rfChooser.m2.renderflags
		self.Gl.setModel(self.m2,self.skin)

	def editTextures(self):
		self.texChooser = TextureEditor()
		self.texChooser.setModel(self.m2,self.skin)
		self.texChooser.show()
		QtCore.QObject.connect(self.texChooser, QtCore.SIGNAL("accepted()"), self.setTextures)

	def setTextures(self):
		self.m2.textures = self.texChooser.m2.textures
		self.Gl.setModel(self.m2,self.skin)


	def editGlobalSequences(self):
		self.gEditor = GSequEditor()
		self.gEditor.setModel(self.m2,self.skin)
		self.gEditor.show()
		QtCore.QObject.connect(self.gEditor, QtCore.SIGNAL("accepted()"), self.setGlobalSequences)

	def setGlobalSequences(self):
		self.m2.gSequ = self.gEditor.m2.gSequ
		self.Gl.setModel(self.m2,self.skin)


	def editUVAnimations(self):
		self.uvEditor = UVAnimEditor()
		self.uvEditor.setModel(self.m2,self.skin)
		self.uvEditor.show()
		QtCore.QObject.connect(self.uvEditor, QtCore.SIGNAL("accepted()"), self.setUVAnimations)

	def setUVAnimations(self):
		self.m2.uv_anim = self.uvEditor.m2.uv_anim
		self.Gl.setModel(self.m2,self.skin)


	def editMaterials(self):
		self.matEditor = MaterialEditor()
		self.matEditor.setModel(self.m2,self.skin)
		self.matEditor.show()
		QtCore.QObject.connect(self.matEditor, QtCore.SIGNAL("accepted()"), self.setMaterials)

	def setMaterials(self):
		self.skin.texunit = self.matEditor.skin.texunit
		self.Gl.setModel(self.m2,self.skin)
		

