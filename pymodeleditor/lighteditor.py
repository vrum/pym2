# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui
from animeditor import AnimEditor
from animcoloreditor import AnimColorEditor
import m2

KeyBoneTypes = {-1:"None", 0 :"ArmL", 1: "ArmR", 2 :"ShoulderL", 3 :"ShoulderR", 4: "SpineLow", 5: "Waist", 6: "Head", 7 :"Jaw", 8: "IndexFingerR", 9: "MiddleFingerR", 10: "PinkyFingerR", 11:"RingFingerR", 12 :"ThumbR", 13 :"IndexFingerL", 14 :"MiddleFingerL", 15 :"PinkyFingerL", 16: "RingFingerL", 17: "ThumbL", 18: "$BTH", 19: "$CSR", 20: "$CSL", 21: "_Breath", 22 :"_Name", 23 :"_NameMount", 24 :"$CHD", 25 :"$CCH", 26 :"Root", 27 :"Wheel1", 28 :"Wheel2", 29 :"Wheel3", 30 :"Wheel4", 31 :"Wheel5", 32: "Wheel6", 33: "Wheel7", 34: "Wheel8" }

LightTypes = {0:"Directional Light",1:"Point Light"}

class LightEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
		self.last = -1
		
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(450, 323)
		
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(90, 280, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		
		self.lightList = QtGui.QComboBox(Dialog)
		self.lightList.setGeometry(QtCore.QRect(10, 10, 69, 22))
		self.lightList.setObjectName("lightList")
		self.connect(self.lightList, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeEdit) 
		
		self.line = QtGui.QFrame(Dialog)
		self.line.setGeometry(QtCore.QRect(10, 40, 211, 16))
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")
		
		self.addIcon = QtGui.QIcon("Icons/edit-add.png")
		self.addButton = QtGui.QPushButton(self.addIcon,"Add",Dialog)
		self.addButton.setGeometry(QtCore.QRect(100, 10, 75, 23))
		self.addButton.setObjectName("addButton")
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addLight)
		
		self.boneBox = QtGui.QComboBox(Dialog)
		self.boneBox.setGeometry(QtCore.QRect(10, 60, 101, 22))
		self.boneBox.setObjectName("boneBox")
		
		self.typeBox = QtGui.QComboBox(Dialog)
		self.typeBox.setGeometry(QtCore.QRect(10, 100, 101, 22))
		self.typeBox.setObjectName("typeBox")
		self.typeBox.addItem(LightTypes[0])
		self.typeBox.addItem(LightTypes[1])
		
		self.xPos = QtGui.QLineEdit(Dialog)
		self.xPos.setGeometry(QtCore.QRect(10, 160, 31, 20))
		self.xPos.setObjectName("xPos")
		
		self.yPos = QtGui.QLineEdit(Dialog)
		self.yPos.setGeometry(QtCore.QRect(50, 160, 31, 20))
		self.yPos.setObjectName("yPos")
		
		self.zPos = QtGui.QLineEdit(Dialog)
		self.zPos.setGeometry(QtCore.QRect(90, 160, 31, 20))
		self.zPos.setObjectName("zPos")
		
		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(10, 140, 46, 13))
		self.label.setObjectName("label")
		
		self.ambientColorButton = QtGui.QPushButton(Dialog)
		self.ambientColorButton.setGeometry(QtCore.QRect(150, 60, 80, 30))
		self.ambientColorButton.setObjectName("ambientColorButton")
		self.connect(self.ambientColorButton, QtCore.SIGNAL("clicked()"), self.editAmbientColor)
		
		self.ambientIntButton = QtGui.QPushButton(Dialog)
		self.ambientIntButton.setGeometry(QtCore.QRect(240, 60, 80, 30))
		self.ambientIntButton.setObjectName("ambientIntButton")
		self.connect(self.ambientIntButton, QtCore.SIGNAL("clicked()"), self.editAmbientIntensity)
		
		self.diffuseColorButton = QtGui.QPushButton(Dialog)
		self.diffuseColorButton.setGeometry(QtCore.QRect(150, 100, 80, 30))
		self.diffuseColorButton.setObjectName("diffuseColorButton")
		self.connect(self.diffuseColorButton, QtCore.SIGNAL("clicked()"), self.editDiffuseColor)
		
		self.diffuseIntButton = QtGui.QPushButton(Dialog)
		self.diffuseIntButton.setGeometry(QtCore.QRect(240, 100, 80, 30))
		self.diffuseIntButton.setObjectName("diffuseIntButton")
		self.connect(self.diffuseIntButton, QtCore.SIGNAL("clicked()"), self.editDiffuseIntensity)
		
		self.attStartButton = QtGui.QPushButton(Dialog)
		self.attStartButton.setGeometry(QtCore.QRect(150, 140, 80, 30))
		self.attStartButton.setObjectName("attStartButton")
		self.connect(self.attStartButton, QtCore.SIGNAL("clicked()"), self.editAttenuationStart)
		
		self.attEndButton = QtGui.QPushButton(Dialog)
		self.attEndButton.setGeometry(QtCore.QRect(240, 140, 80, 30))
		self.attEndButton.setObjectName("attEndButton")
		self.connect(self.attEndButton, QtCore.SIGNAL("clicked()"), self.editAttenuationEnd)
		
		self.enabledButton = QtGui.QPushButton(Dialog)
		self.enabledButton.setGeometry(QtCore.QRect(10, 200, 80, 30))
		self.enabledButton.setObjectName("enabledButton")
		self.connect(self.enabledButton, QtCore.SIGNAL("clicked()"), self.editEnabled)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Light Editor", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Dialog", "Position:", None, QtGui.QApplication.UnicodeUTF8))
		self.ambientColorButton.setText(QtGui.QApplication.translate("Dialog", "AmbientColor", None, QtGui.QApplication.UnicodeUTF8))
		self.ambientIntButton.setText(QtGui.QApplication.translate("Dialog", "AmbientInt", None, QtGui.QApplication.UnicodeUTF8))
		self.diffuseColorButton.setText(QtGui.QApplication.translate("Dialog", "DiffuseColor", None, QtGui.QApplication.UnicodeUTF8))
		self.diffuseIntButton.setText(QtGui.QApplication.translate("Dialog", "DiffuseInt", None, QtGui.QApplication.UnicodeUTF8))
		self.attStartButton.setText(QtGui.QApplication.translate("Dialog", "AttStart", None, QtGui.QApplication.UnicodeUTF8))
		self.attEndButton.setText(QtGui.QApplication.translate("Dialog", "AttEnd", None, QtGui.QApplication.UnicodeUTF8))
		self.enabledButton.setText(QtGui.QApplication.translate("Dialog", "Enabled", None, QtGui.QApplication.UnicodeUTF8))


	def finalizeMe(self):
		self.saveOld()
		self.accept()

	def setCurrentEditing(self,i):
		self.lightList.setCurrentIndex(i)
		self.changeEdit()

	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		for i in range(len(self.m2.lights)):
			self.lightList.addItem(str(i)+": "+LightTypes[self.m2.lights[i].Type])
		for i in range(len(self.m2.bones)+1):
			if i == 0:
				self.boneBox.addItem("None "+str(i-1))
			else:
				self.boneBox.addItem("Bone: "+str(i-1)+" "+KeyBoneTypes[self.m2.bones[i-1].KeyBoneId])
		self.changeEdit()
		
		
	def addLight(self):
		l = m2.Light()
		l.AmbientCol.type = m2.DATA_VEC3
		l.AmbientInt.type = m2.DATA_FLOAT
		l.DiffuseCol.type = m2.DATA_VEC3
		l.DiffuseInt.type = m2.DATA_FLOAT
		l.AttStart.type = m2.DATA_FLOAT
		l.AttEnd.type = m2.DATA_FLOAT
		l.Enabled.type = m2.DATA_INT

		self.m2.lights.append(l)
		
		self.lightList.addItem(str(self.m2.hdr.lights.count)+": "+LightTypes[self.m2.lights[self.last].Type])
		self.m2.hdr.lights.count += 1

	def saveOld(self):
		if (self.last == -1):
			return
		self.m2.lights[self.last].Type = self.typeBox.currentIndex()
		self.m2.lights[self.last].Pos.x = float(self.xPos.text())
		self.m2.lights[self.last].Pos.y = float(self.yPos.text())
		self.m2.lights[self.last].Pos.z = float(self.zPos.text())
		self.m2.lights[self.last].Bone = self.boneBox.currentIndex()-1
		self.lightList.setItemText(self.last,str(self.last)+": "+LightTypes[self.m2.lights[self.last].Type])
			
			
			
			
	def changeEdit(self):
		self.saveOld()
		self.last = self.lightList.currentIndex()
		if not len(self.m2.lights)<1:			
			self.typeBox.setCurrentIndex(self.m2.lights[self.lightList.currentIndex()].Type)
			self.xPos.setText(str(self.m2.lights[self.lightList.currentIndex()].Pos.x))
			self.yPos.setText(str(self.m2.lights[self.lightList.currentIndex()].Pos.y))
			self.zPos.setText(str(self.m2.lights[self.lightList.currentIndex()].Pos.z))			
			self.boneBox.setCurrentIndex(self.m2.lights[self.lightList.currentIndex()].Bone+1)
			
			
	

	def editAmbientColor(self):		
		temp = self.lightList.currentIndex()
		self.AmbColEditor = AnimColorEditor()
		self.AmbColEditor.setAnimBlock(self.m2.lights[temp].AmbientCol,self.m2.gSequ)
		self.AmbColEditor.show()
		self.connect(self.AmbColEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setAmbientColor)

	def setAmbientColor(self):
		self.m2.lights[self.lightList.currentIndex()].AmbientCol = self.AmbColEditor.getAnimBlock()

	def editAmbientIntensity(self):		
		temp = self.lightList.currentIndex()
		self.AmbIntEditor = AnimEditor()
		self.AmbIntEditor.setAnimBlock(self.m2.lights[temp].AmbientInt,self.m2.gSequ)
		self.AmbIntEditor.show()
		self.connect(self.AmbIntEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setAmbientIntensity)

	def setAmbientIntensity(self):
		self.m2.lights[self.lightList.currentIndex()].AmbientInt = self.AmbIntEditor.getAnimBlock()

	def editDiffuseColor(self):		
		temp = self.lightList.currentIndex()
		self.DiffColEditor = AnimColorEditor()
		self.DiffColEditor.setAnimBlock(self.m2.lights[temp].DiffuseCol,self.m2.gSequ)
		self.DiffColEditor.show()
		self.connect(self.DiffColEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setDiffuseColor)

	def setDiffuseColor(self):
		self.m2.lights[self.lightList.currentIndex()].DiffuseCol = self.DiffColEditor.getAnimBlock()

	def editDiffuseIntensity(self):		
		temp = self.lightList.currentIndex()
		self.DiffIntEditor = AnimEditor()
		self.DiffIntEditor.setAnimBlock(self.m2.lights[temp].DiffuseInt,self.m2.gSequ)
		self.DiffIntEditor.show()
		self.connect(self.DiffIntEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setDiffuseIntensity)

	def setDiffuseIntensity(self):
		self.m2.lights[self.lightList.currentIndex()].DiffuseInt = self.DiffIntEditor.getAnimBlock()

	def editAttenuationStart(self):		
		temp = self.lightList.currentIndex()
		self.AttStartEditor = AnimEditor()
		self.AttStartEditor.setAnimBlock(self.m2.lights[temp].AttStart,self.m2.gSequ)
		self.AttStartEditor.show()
		self.connect(self.AttStartEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setAttenuationStart)

	def setAttenuationStart(self):
		self.m2.lights[self.lightList.currentIndex()].AttStart = self.AttStartEditor.getAnimBlock()

	def editAttenuationEnd(self):		
		temp = self.lightList.currentIndex()
		self.AttEndEditor = AnimEditor()
		self.AttEndEditor.setAnimBlock(self.m2.lights[temp].AttEnd,self.m2.gSequ)
		self.AttEndEditor.show()
		self.connect(self.AttEndEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setAttenuationEnd)

	def setAttenuationEnd(self):
		self.m2.lights[self.lightList.currentIndex()].AttEnd = self.AttEndEditor.getAnimBlock()

	def editEnabled(self):		
		temp = self.lightList.currentIndex()
		self.EnabledEditor = AnimEditor()
		self.EnabledEditor.setAnimBlock(self.m2.lights[temp].Enabled,self.m2.gSequ)
		self.EnabledEditor.show()
		self.connect(self.EnabledEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setEnabled)

	def setEnabled(self):
		self.m2.lights[self.lightList.currentIndex()].Enabled = self.EnabledEditor.getAnimBlock()
			

