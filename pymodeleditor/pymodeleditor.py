#! /usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
#
# Created: Wed May 19 12:19:34 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtOpenGL


from m2 import *
from skin import *

from glView import *

from transparencychooser import *
from renderflags import *
from textureeditor import *
from gsequedit import *
from uvanimeditor import *
from materialeditor import *
from attachmenteditor import *
from nodetree import *


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


		self.attachmentButton = QtGui.QPushButton(Form)
		self.attachmentButton.setGeometry(QtCore.QRect(10, 570, 132, 28))
		self.attachmentButton.setObjectName("attachmentButton")
		self.connect(self.attachmentButton, QtCore.SIGNAL("clicked()"), self.editAttachments)


		self.boneButton = QtGui.QPushButton(Form)
		self.boneButton.setGeometry(QtCore.QRect(140, 570, 132, 28))
		self.boneButton.setObjectName("boneButton")
		self.connect(self.boneButton, QtCore.SIGNAL("clicked()"), self.showBoneTree)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "PyModelEditor", None, QtGui.QApplication.UnicodeUTF8))
		self.transparencyButton.setText(QtGui.QApplication.translate("Form", "Edit Transparency", None, QtGui.QApplication.UnicodeUTF8))
		self.renderflagButton.setText(QtGui.QApplication.translate("Form", "Edit Renderflags", None, QtGui.QApplication.UnicodeUTF8))
		self.textureButton.setText(QtGui.QApplication.translate("Form", "Edit Textures", None, QtGui.QApplication.UnicodeUTF8))
		self.gsequButton.setText(QtGui.QApplication.translate("Form", "Global Sequences", None, QtGui.QApplication.UnicodeUTF8))
		self.uvanimButton.setText(QtGui.QApplication.translate("Form", "Edit UV Animations", None, QtGui.QApplication.UnicodeUTF8))
		self.materialButton.setText(QtGui.QApplication.translate("Form", "Edit Materials", None, QtGui.QApplication.UnicodeUTF8))
		self.attachmentButton.setText(QtGui.QApplication.translate("Form", "Edit Attachments", None, QtGui.QApplication.UnicodeUTF8))
		self.boneButton.setText(QtGui.QApplication.translate("Form", "Show Node Tree", None, QtGui.QApplication.UnicodeUTF8))

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
		self.m2 = self.tChooser.m2
		self.Gl.setModel(self.m2,self.skin)

	def editRenderflags(self):
		self.rfChooser = RenderFlagsEditor()
		self.rfChooser.setModel(self.m2,self.skin)
		self.rfChooser.show()
		QtCore.QObject.connect(self.rfChooser, QtCore.SIGNAL("accepted()"), self.setRenderflags)

	def setRenderflags(self):
		self.m2 = self.rfChooser.m2
		self.Gl.setModel(self.m2,self.skin)

	def editTextures(self):
		self.texChooser = TextureEditor()
		self.texChooser.setModel(self.m2,self.skin)
		self.texChooser.show()
		QtCore.QObject.connect(self.texChooser, QtCore.SIGNAL("accepted()"), self.setTextures)

	def setTextures(self):
		self.m2 = self.texChooser.m2
		self.Gl.setModel(self.m2,self.skin)


	def editGlobalSequences(self):
		self.gEditor = GSequEditor()
		self.gEditor.setModel(self.m2,self.skin)
		self.gEditor.show()
		QtCore.QObject.connect(self.gEditor, QtCore.SIGNAL("accepted()"), self.setGlobalSequences)

	def setGlobalSequences(self):
		self.m2 = self.gEditor.m2
		self.Gl.setModel(self.m2,self.skin)


	def editUVAnimations(self):
		self.uvEditor = UVAnimEditor()
		self.uvEditor.setModel(self.m2,self.skin)
		self.uvEditor.show()
		QtCore.QObject.connect(self.uvEditor, QtCore.SIGNAL("accepted()"), self.setUVAnimations)

	def setUVAnimations(self):
		self.m2 = self.uvEditor.m2
		self.Gl.setModel(self.m2,self.skin)


	def editMaterials(self):
		self.matEditor = MaterialEditor()
		self.matEditor.setModel(self.m2,self.skin)
		self.matEditor.show()
		QtCore.QObject.connect(self.matEditor, QtCore.SIGNAL("accepted()"), self.setMaterials)

	def setMaterials(self):
		self.skin.texunit = self.matEditor.skin.texunit
		self.Gl.setModel(self.m2,self.skin)


	def editAttachments(self):
		self.attEditor = AttachmentEditor()
		self.attEditor.setModel(self.m2,self.skin)
		self.attEditor.show()
		QtCore.QObject.connect(self.attEditor, QtCore.SIGNAL("accepted()"), self.setAttachments)

	def setAttachments(self):
		self.m2 = self.attEditor.m2
		self.Gl.setModel(self.m2,self.skin)

	def showBoneTree(self):
		self.bonetree = BoneView()
		self.bonetree.setModel(self.m2,self.skin)
		self.bonetree.show()

