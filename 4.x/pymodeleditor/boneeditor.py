# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from animeditor import AnimEditor
import m2

KeyBoneTypes = {-1:"None", 0 :"ArmL", 1: "ArmR", 2 :"ShoulderL", 3 :"ShoulderR", 4: "SpineLow", 5: "Waist", 6: "Head", 7 :"Jaw", 8: "IndexFingerR", 9: "MiddleFingerR", 10: "PinkyFingerR", 11:"RingFingerR", 12 :"ThumbR", 13 :"IndexFingerL", 14 :"MiddleFingerL", 15 :"PinkyFingerL", 16: "RingFingerL", 17: "ThumbL", 18: "$BTH", 19: "$CSR", 20: "$CSL", 21: "_Breath", 22 :"_Name", 23 :"_NameMount", 24 :"$CHD", 25 :"$CCH", 26 :"Root", 27 :"Wheel1", 28 :"Wheel2", 29 :"Wheel3", 30 :"Wheel4", 31 :"Wheel5", 32: "Wheel6", 33: "Wheel7", 34: "Wheel8" }


class BoneEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
		self.last = -1


	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(480, 350)
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(130, 300, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")

		self.comboBox = QtGui.QComboBox(Dialog)
		self.comboBox.setGeometry(QtCore.QRect(10, 10, 201, 27))
		self.comboBox.setObjectName("comboBox")
		self.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeEdit) 

		self.addIcon = QtGui.QIcon("Icons/edit-add.png")
		self.addButton = QtGui.QPushButton(self.addIcon,"Add",Dialog)
		self.addButton.setGeometry(QtCore.QRect(220, 10, 92, 28))
		self.addButton.setObjectName("addButton")
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addBone)


		self.line = QtGui.QFrame(Dialog)
		self.line.setGeometry(QtCore.QRect(10, 50, 261, 16))
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")

		self.typeBox = QtGui.QComboBox(Dialog)
		self.typeBox.setGeometry(QtCore.QRect(20, 70, 100, 27))
		self.typeBox.setObjectName("typeBox")
		for i in range(36):			
			self.typeBox.addItem(QtCore.QString())


		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(20, 110, 62, 18))
		self.label.setObjectName("label")

		self.xEdit = QtGui.QLineEdit(Dialog)
		self.xEdit.setGeometry(QtCore.QRect(20, 130, 50, 26))
		self.xEdit.setObjectName("xEdit")

		self.yEdit = QtGui.QLineEdit(Dialog)
		self.yEdit.setGeometry(QtCore.QRect(80, 130, 50, 26))
		self.yEdit.setObjectName("yEdit")

		self.zEdit = QtGui.QLineEdit(Dialog)
		self.zEdit.setGeometry(QtCore.QRect(140, 130, 50, 26))
		self.zEdit.setObjectName("zEdit")


		self.parentlabel = QtGui.QLabel(Dialog)
		self.parentlabel.setGeometry(QtCore.QRect(20, 170, 62, 18))
		self.parentlabel.setObjectName("parentlabel")

		self.boneBox = QtGui.QComboBox(Dialog)
		self.boneBox.setGeometry(QtCore.QRect(20, 200, 100, 27))
		self.boneBox.setObjectName("boneBox")


		self.translationIcon = QtGui.QIcon("Icons/edit-translation.png")
		self.translationButton = QtGui.QPushButton(self.translationIcon,"Edit Translation",Dialog)
		self.translationButton.setGeometry(QtCore.QRect(20, 230, 140, 28))
		self.translationButton.setObjectName("translationButton")
		self.connect(self.translationButton, QtCore.SIGNAL("clicked()"), self.editTranslation)


		self.scalingIcon = QtGui.QIcon("Icons/edit-scaling.png")
		self.scalingButton = QtGui.QPushButton(self.scalingIcon,"Edit Scaling",Dialog)
		self.scalingButton.setGeometry(QtCore.QRect(170, 230, 140, 28))
		self.scalingButton.setObjectName("translationButton")
		self.connect(self.scalingButton, QtCore.SIGNAL("clicked()"), self.editScaling)


		self.rotationIcon = QtGui.QIcon("Icons/edit-rotation.png")
		self.rotationButton = QtGui.QPushButton(self.rotationIcon,"Edit Rotation",Dialog)
		self.rotationButton.setGeometry(QtCore.QRect(320, 230, 140, 28))
		self.rotationButton.setObjectName("rotationButton")
		self.connect(self.rotationButton, QtCore.SIGNAL("clicked()"), self.editRotation)

		self.billBox = QtGui.QCheckBox(Dialog)
		self.billBox.setGeometry(QtCore.QRect(20, 270, 110, 23))
		self.billBox.setObjectName("checkBox")

		self.transBox = QtGui.QCheckBox(Dialog)
		self.transBox.setGeometry(QtCore.QRect(150, 270, 110, 23))
		self.transBox.setObjectName("transBox")

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.finalizeMe)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)


	def finalizeMe(self):
		self.saveOld()
		self.accept()

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Bone Editor", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Dialog", "Position:", None, QtGui.QApplication.UnicodeUTF8))
		self.parentlabel.setText(QtGui.QApplication.translate("Dialog", "Parent:", None, QtGui.QApplication.UnicodeUTF8))
		self.billBox.setText(QtGui.QApplication.translate("Dialog", "Billboarded", None, QtGui.QApplication.UnicodeUTF8))
		self.transBox.setText(QtGui.QApplication.translate("Dialog", "Transformed", None, QtGui.QApplication.UnicodeUTF8))

		for i in range(36):
			self.typeBox.setItemText(i, QtGui.QApplication.translate("Dialog", str(i-1)+": "+KeyBoneTypes[i-1], None, QtGui.QApplication.UnicodeUTF8))

	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		for i in range(len(self.m2.bones)):
			self.comboBox.addItem(str(i)+": "+KeyBoneTypes[self.m2.bones[i].KeyBoneId])
		for i in range(len(self.m2.bones)+1):
			if i == 0:
				self.boneBox.addItem("None "+str(i-1))
			else:
				self.boneBox.addItem("Bone: "+str(i-1)+" "+KeyBoneTypes[self.m2.bones[i-1].KeyBoneId])
		self.changeEdit()

	def setCurrentEditing(self,i):
		self.comboBox.setCurrentIndex(i)
		self.changeEdit()
	
	def addBone(self):
		b = m2.Bone()
		b.translation.type = m2.DATA_VEC3
		b.scaling.type = m2.DATA_VEC3
		b.rotation.type = m2.DATA_QUAT

		lu = m2.Lookup()
		lu.Id = self.m2.hdr.bones.count

		self.m2.bones.append(b)
		self.m2.bone_lookup.append(lu)
		
		self.comboBox.addItem(str(self.m2.hdr.bones.count)+": "+KeyBoneTypes[self.m2.bones[self.m2.hdr.bones.count].KeyBoneId])

		self.m2.hdr.bones.count += 1
		self.m2.hdr.bone_lookup.count += 1

	def changeEdit(self):
		self.saveOld()
		self.last = self.comboBox.currentIndex()
		if not len(self.m2.bones)<1:			
			self.typeBox.setCurrentIndex(self.m2.bones[self.comboBox.currentIndex()].KeyBoneId+1)
			self.xEdit.setText(str(self.m2.bones[self.comboBox.currentIndex()].pivot.x))
			self.yEdit.setText(str(self.m2.bones[self.comboBox.currentIndex()].pivot.y))
			self.zEdit.setText(str(self.m2.bones[self.comboBox.currentIndex()].pivot.z))			
			self.boneBox.setCurrentIndex(self.m2.bones[self.comboBox.currentIndex()].parent+1)
			if self.m2.bones[self.comboBox.currentIndex()].flags & 0x8:
				self.billBox.setCheckState(2)
			else:
				self.billBox.setCheckState(0)

			if self.m2.bones[self.comboBox.currentIndex()].flags & 0x200:
				self.transBox.setCheckState(2)
			else:
				self.transBox.setCheckState(0)

	def saveOld(self):
		if (self.last == -1):
			return
		self.m2.bones[self.last].KeyBoneId = self.typeBox.currentIndex()-1
		self.m2.bones[self.last].pivot.x = float(self.xEdit.text())
		self.m2.bones[self.last].pivot.y = float(self.yEdit.text())
		self.m2.bones[self.last].pivot.z = float(self.zEdit.text())
		self.m2.bones[self.last].parent = self.boneBox.currentIndex()-1
		self.m2.bones[self.last].flags = 0
		if self.billBox.checkState() == 2:
			self.m2.bones[self.last].flags += 0x8
		if self.transBox.checkState() == 2:
			self.m2.bones[self.last].flags += 0x200
		self.comboBox.setItemText(self.last,str(self.last)+": "+KeyBoneTypes[self.m2.bones[self.last].KeyBoneId])

	def setTranslation(self):
		self.m2.bones[self.comboBox.currentIndex()].translation = self.TranslationEditor.getAnimBlock()

	def editTranslation(self):		
		temp = self.comboBox.currentIndex()
		self.TranslationEditor = AnimEditor()
		self.TranslationEditor.setAnimBlock(self.m2.bones[temp].translation,self.m2.gSequ)
		self.TranslationEditor.show()
		self.connect(self.TranslationEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setTranslation)

	def setScaling(self):
		self.m2.bones[self.comboBox.currentIndex()].scaling = self.ScalingEditor.getAnimBlock()

	def editScaling(self):		
		temp = self.comboBox.currentIndex()
		self.ScalingEditor = AnimEditor()
		self.ScalingEditor.setAnimBlock(self.m2.bones[temp].scaling,self.m2.gSequ)
		self.ScalingEditor.show()
		self.connect(self.ScalingEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setScaling)

	def setRotation(self):
		self.m2.bones[self.comboBox.currentIndex()].rotation = self.RotationEditor.getAnimBlock()

	def editRotation(self):		
		temp = self.comboBox.currentIndex()
		self.RotationEditor = AnimEditor()
		self.RotationEditor.setAnimBlock(self.m2.bones[temp].rotation,self.m2.gSequ)
		self.RotationEditor.show()
		self.connect(self.RotationEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setRotation)





