# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui
from animeditor import AnimEditor
import m2

class UVAnimEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(514, 300)

		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(410, 10, 101, 81))
		self.buttonBox.setOrientation(QtCore.Qt.Vertical)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")

		self.comboBox = QtGui.QComboBox(Dialog)
		self.comboBox.setGeometry(QtCore.QRect(10, 10, 85, 27))
		self.comboBox.setObjectName("comboBox")

		self.addIcon = QtGui.QIcon("Icons/edit-add.png")
		self.addButton = QtGui.QPushButton(self.addIcon,"Add",self)
		self.addButton.setGeometry(QtCore.QRect(110, 10, 92, 28))
		self.addButton.setObjectName("addButton")
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.adduvanimation) 

		self.line = QtGui.QFrame(Dialog)
		self.line.setGeometry(QtCore.QRect(10, 40, 201, 21))
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")

		self.translationIcon = QtGui.QIcon("Icons/edit-translation.png")
		self.editTranslationButton =  QtGui.QPushButton(self.translationIcon,"Edit Translation",Dialog)
		self.editTranslationButton.setGeometry(QtCore.QRect(10, 50, 120, 28))
		self.editTranslationButton.setObjectName("editTranslationButton")
		self.connect(self.editTranslationButton, QtCore.SIGNAL("clicked()"), self.editTranslation) 

		self.scalingIcon = QtGui.QIcon("Icons/edit-scaling.png")
		self.editScalingButton = QtGui.QPushButton(self.scalingIcon,"Edit Scaling",Dialog)
		self.editScalingButton.setGeometry(QtCore.QRect(10, 90, 120, 28))
		self.editScalingButton.setObjectName("editScalingButton")
		self.connect(self.editScalingButton, QtCore.SIGNAL("clicked()"), self.editScaling) 

		self.rotationIcon = QtGui.QIcon("Icons/edit-rotation.png")
		self.editRotationButton = QtGui.QPushButton(self.rotationIcon,"Edit Rotation",Dialog)
		self.editRotationButton.setGeometry(QtCore.QRect(10, 130, 120, 28))
		self.editRotationButton.setObjectName("editRotationButton")
		self.connect(self.editRotationButton, QtCore.SIGNAL("clicked()"), self.editRotation) 


		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Edit UV-Animations", None, QtGui.QApplication.UnicodeUTF8))
		self.editTranslationButton.setText(QtGui.QApplication.translate("Dialog", "Edit Translation", None, QtGui.QApplication.UnicodeUTF8))
		self.editScalingButton.setText(QtGui.QApplication.translate("Dialog", "Edit Scaling", None, QtGui.QApplication.UnicodeUTF8))
		self.editRotationButton.setText(QtGui.QApplication.translate("Dialog", "Edit Rotation", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))

	
	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		for i in range(len(self.m2.uv_anim)):
			self.comboBox.addItem(str(i))

	def setTranslation(self):
		self.m2.uv_anim[self.comboBox.currentIndex()].translation = self.TranslationEditor.getAnimBlock()

	def editTranslation(self):		
		temp = self.comboBox.currentIndex()
		self.TranslationEditor = AnimEditor()
		self.TranslationEditor.setAnimBlock(self.m2.uv_anim[temp].translation,self.m2.gSequ)
		self.TranslationEditor.show()
		self.connect(self.TranslationEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setTranslation)


	def setScaling(self):
		self.m2.uv_anim[self.comboBox.currentIndex()].scaling = self.ScalingEditor.getAnimBlock()

	def editScaling(self):		
		temp = self.comboBox.currentIndex()
		self.ScalingEditor = AnimEditor()
		self.ScalingEditor.setAnimBlock(self.m2.uv_anim[temp].scaling,self.m2.gSequ)
		self.ScalingEditor.show()
		self.connect(self.ScalingEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setScaling)

	def setRotation(self):
		self.m2.uv_anim[self.comboBox.currentIndex()].rotation = self.RotationEditor.getAnimBlock()

	def editRotation(self):		
		temp = self.comboBox.currentIndex()
		self.RotationEditor = AnimEditor()
		self.RotationEditor.setAnimBlock(self.m2.uv_anim[temp].rotation,self.m2.gSequ)
		self.RotationEditor.show()
		self.connect(self.RotationEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setRotation)


	def adduvanimation(self):
		tr = m2.UVAnimation()
		tr.translation.type = m2.DATA_VEC3
		tr.scaling.type = m2.DATA_VEC3
		tr.rotation.type = m2.DATA_QUAT
		
		tl = m2.Lookup()
		tl.Id = self.m2.hdr.uv_anim .count

		self.comboBox.addItem(str(len(self.m2.uv_anim )))

		self.m2.uv_anim .append(tr)
		self.m2.hdr.uv_anim .count += 1

		self.m2.uv_anim_lookup.append(tl)
		self.m2.hdr.uv_anim_lookup.count += 1

