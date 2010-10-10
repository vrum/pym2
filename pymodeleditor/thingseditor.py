# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from boundseditor import *

class ThingsEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
		self.last = -1
	def setupUi(self, ThingsEditor):
		ThingsEditor.setObjectName("ThingsEditor")
		ThingsEditor.resize(400, 300)
		
		self.buttonBox = QtGui.QDialogButtonBox(ThingsEditor)
		self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		
		self.calcModel = QtGui.QPushButton(ThingsEditor)
		self.calcModel.setGeometry(QtCore.QRect(10, 10, 171, 23))
		self.calcModel.setObjectName("calcModel")
		self.connect(self.calcModel, QtCore.SIGNAL("clicked()"), self.calculateBounds_Model)
		
		self.editView = QtGui.QPushButton(ThingsEditor)
		self.editView.setGeometry(QtCore.QRect(200, 10, 151, 23))
		self.editView.setObjectName("editView")
		self.connect(self.editView, QtCore.SIGNAL("clicked()"), self.editViewDistance)
		
		self.editBound = QtGui.QPushButton(ThingsEditor)
		self.editBound.setGeometry(QtCore.QRect(200, 40, 151, 23))
		self.editBound.setObjectName("editBound")
		self.connect(self.editBound, QtCore.SIGNAL("clicked()"), self.editBoundBox)

		self.retranslateUi(ThingsEditor)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.finalizeMe)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ThingsEditor.reject)
		QtCore.QMetaObject.connectSlotsByName(ThingsEditor)
		
	def finalizeMe(self):
		self.accept()

	def retranslateUi(self, ThingsEditor):
		ThingsEditor.setWindowTitle(QtGui.QApplication.translate("ThingsEditor", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
		self.calcModel.setText(QtGui.QApplication.translate("ThingsEditor", "Calculate Bounds from Model", None, QtGui.QApplication.UnicodeUTF8))
		self.editView.setText(QtGui.QApplication.translate("ThingsEditor", "Edit View Distance", None, QtGui.QApplication.UnicodeUTF8))
		self.editBound.setText(QtGui.QApplication.translate("ThingsEditor", "Edit BoundBox", None, QtGui.QApplication.UnicodeUTF8))
		
	
	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		
	def calculateBounds_Model(self):
		self.m2.bounding_triangles = []
		self.m2.bounding_vertices = []
		self.m2.bounding_normals = []

		self.m2.hdr.bounding_triangles.count = len(self.skin.tri)
		self.m2.hdr.bounding_vertices.count = len(self.skin.indices)
		self.m2.hdr.bounding_normals.count = len(self.skin.indices)

		for i in self.skin.indices:
			self.m2.bounding_vertices.append(self.m2.vertices[i.Id].pos)
			self.m2.bounding_normals.append(self.m2.vertices[i.Id].normal)

		for i in self.skin.tri:
			self.m2.bounding_triangles.append(i)
			
	def editViewDistance(self):		
		self.viewEditor = BoundsEditor()
		self.viewEditor.setBounds(self.m2.hdr.vbox)
		self.viewEditor.show()
		QtCore.QObject.connect(self.viewEditor, QtCore.SIGNAL("accepted()"), self.setViewDistance)
	def setViewDistance(self):
		self.m2.hdr.vbox = self.viewEditor.bounds
		
	def editBoundBox(self):		
		self.boundsEditor = BoundsEditor()
		self.boundsEditor.setBounds(self.m2.hdr.bound)
		self.boundsEditor.show()
		QtCore.QObject.connect(self.boundsEditor, QtCore.SIGNAL("accepted()"), self.setBoundBox)
	def setBoundBox(self):
		self.m2.hdr.bound = self.boundsEditor.bounds

