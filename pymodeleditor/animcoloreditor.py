# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from m2 import *

class AnimColorEditor_Ui(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(538, 373)		

		self.currentAnim = -1
		
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(180, 330, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.finished_now) 
		self.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.close_now)
		
		self.scrollArea = QtGui.QScrollArea(Dialog)
		self.scrollArea.setGeometry(QtCore.QRect(10, 50, 511, 271))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		
		self.addIcon = QtGui.QIcon("Icons/edit-add.png")
		
		self.animCombo = QtGui.QComboBox(Dialog)
		self.animCombo.setGeometry(QtCore.QRect(10, 10, 85, 27))
		self.animCombo.setObjectName("animCombo")
		
		
		self.addButton = QtGui.QPushButton(self.addIcon,"Add AnimSub",self)
		self.addButton.setGeometry(QtCore.QRect(110, 10, 92, 28))
		self.addButton.setObjectName("addButton")
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addAnimSub)
		
		self.interpolCombo = QtGui.QComboBox(Dialog)
		self.interpolCombo.setGeometry(QtCore.QRect(220, 10, 85, 27))
		self.interpolCombo.setObjectName("interpolCombo")
		self.interpolCombo.addItem("No Interpolation")
		self.interpolCombo.addItem("Linear Interpolation")
		self.interpolCombo.addItem("Hermite Interpolation")
		self.interpolCombo.addItem("Bezier Interpolation")
		
		self.globalCombo = QtGui.QComboBox(Dialog)
		self.globalCombo.setGeometry(QtCore.QRect(330, 10, 85, 27))
		self.globalCombo.setObjectName("globalCombo")
		self.globalCombo.addItem("None: -1")

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
		
		self.colEditors = []
		
		#no other types!
		self.type = DATA_VEC3

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Animated Color Editor", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "add", None, QtGui.QApplication.UnicodeUTF8))
		
	def fillScrollArea(self,data):	
	
		self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 269))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
		
		self.editColBtns = []
		self.colVals = []
		self.colTimeEdits = []
		self.delColBtns = []
		y = 0
		if (self.currentAnim !=-1)and(self.animblock.nKeys > self.currentAnim ):
			for i in range(self.animblock.KeySubs[self.currentAnim].nEntries):
		
				editColorBtn = QtGui.QPushButton(self.scrollAreaWidgetContents)
				editColorBtn.setGeometry(QtCore.QRect(10, 10+y, 92, 28))
				editColorBtn.setObjectName("editColorBtn"+str(i))
				editColorBtn.setText("Edit Color")
				
				self.connect(editColorBtn, QtCore.SIGNAL("clicked()"), self.curryeditCol(i))
				self.editColBtns.append(editColorBtn)
				self.colVals.append(self.animblock.KeySubs[self.currentAnim].values[i])				
		
				colTimeEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
				colTimeEdit.setGeometry(QtCore.QRect(120, 10+y, 181, 26))
				colTimeEdit.setObjectName("colTimeEdit"+str(i))
				colTimeEdit.setText(str(self.animblock.TimeSubs[self.currentAnim ].values[i]))
				self.colTimeEdits.append(colTimeEdit)				
		
				delColBtn = QtGui.QPushButton(self.scrollAreaWidgetContents)
				delColBtn.setGeometry(QtCore.QRect(330, 10+y, 92, 28))
				delColBtn.setObjectName("delColBtn"+str(i))
				delColBtn.setText("Delete")
				self.delColBtns.append(delColBtn)
						
				y += 35		
		
		self.addColBtn = QtGui.QPushButton(self.addIcon,"Add Timestamp", self.scrollAreaWidgetContents)
		self.addColBtn.setGeometry(QtCore.QRect(330, 10+y, 130, 28))
		self.addColBtn.setObjectName("addColBtn")
		self.connect(self.addColBtn, QtCore.SIGNAL("clicked()"), self.addTimestamp)	
		
		
		self.scrollAreaWidgetContents.setMinimumSize(380,50+y)	
		
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)

	def setAnimBlock(self,animblock,globalsequ):
		#set the animations
		self.animblock = animblock
		self.type = animblock.type
		for i in range(animblock.nKeys):
			self.animCombo.addItem(str(i))
		if animblock.nKeys != 0:
			self.currentAnim = 0
		for i in globalsequ:
			self.globalCombo.addItem(str(i.Timestamp))

		self.globalCombo.setCurrentIndex(self.animblock.gsequ + 1)
		self.interpolCombo.setCurrentIndex(self.animblock.interpolation)
		self.fillScrollArea(self.currentAnim)
		self.connect(self.animCombo, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeAnimation) 
	
	
	def addTimestamp(self):		
		if self.currentAnim !=-1:
			(self.animblock.TimeSubs[self.currentAnim],self.animblock.KeySubs[self.currentAnim])= self.getAnimSub()
		self.animblock.TimeSubs[self.currentAnim].nEntries += 1
		self.animblock.TimeSubs[self.currentAnim].values.append(0)
		self.animblock.KeySubs[self.currentAnim].nEntries += 1
		self.animblock.KeySubs[self.currentAnim].values.append(Vec3())
		self.fillScrollArea(self.currentAnim)
	
	def curryeditCol(self, argument):
		return lambda : self.editColVal( argument)
	
	def editColVal(self, num):
		editornum = len(self.colEditors)
		colEditor = QtGui.QColorDialog()
		col = QtGui.QColor()
		col.setRgbF(self.colVals[num].x, self.colVals[num].y, self.colVals[num].z)
		colEditor.setCurrentColor(col)
		#overflow, do this better or get a way to delete this ~.~
		self.colEditors.append(colEditor)
		colEditor.show()		
		QtCore.QObject.connect(colEditor, QtCore.SIGNAL("accepted()"), self.currygetEditetColVal(num,editornum))
	
	def currygetEditetColVal(self, argument,arg2):
		return lambda : self.getEditetColVal( argument,arg2)	
		
	def getEditetColVal(self,num,editor):
		col = self.colEditors[editor].currentColor()
		self.colVals[num].x = col.redF()
		self.colVals[num].y = col.greenF()
		self.colVals[num].z = col.blueF()
		#segmentation fault ._.
		#del self.colEditors[editor]

	def finished_now(self):
		self.hide()
		(self.animblock.TimeSubs[self.currentAnim],self.animblock.KeySubs[self.currentAnim])= self.getAnimSub()		
		self.emit(QtCore.SIGNAL("AnimBlockEdited()"))

	def changeAnimation(self):
		if self.currentAnim !=-1:
			(self.animblock.TimeSubs[self.currentAnim],self.animblock.KeySubs[self.currentAnim])= self.getAnimSub()
		self.currentAnim = self.animCombo.currentIndex()
		self.fillScrollArea(self.currentAnim)

	def getAnimBlock(self):
		self.animblock.interpolation = self.interpolCombo.currentIndex()
		self.animblock.gsequ = self.globalCombo.currentIndex() - 1		
		if self.currentAnim !=-1:
			(self.animblock.TimeSubs[self.currentAnim], self.animblock.KeySubs[self.currentAnim])= self.getAnimSub()
		return self.animblock

	def getAnimSub(self):
		timesub = AnimSub()
		timesub.type = DATA_INT
		timesub.nEntries = len(self.editColBtns)
		timesub.values = []
		for i in range(timesub.nEntries):			
			val = str(self.colTimeEdits[i].text())
			val.encode("cp1252")
			timesub.values.append(int(val))
		

		keysub = AnimSub()
		keysub.type = self.type
		keysub.nEntries = len(self.editColBtns)
		keysub.values = []
		for i in range(keysub.nEntries):
			keysub.values.append(self.colVals[i])
		return (timesub,keysub)

			
	def addAnimSub(self):
		self.animblock.nKeys += 1
		keysub = AnimSub()
		keysub.type = self.animblock.type
		keysub.nEntries = 1
		if self.type == DATA_VEC3:
			k = Vec3()
			keysub.values.append(k)
		else:
			pass 
		self.animblock.KeySubs.append(keysub)
		self.animblock.nTimes += 1
		timesub = AnimSub()
		timesub.nEntries = 1
		timesub.values.append(0)
		self.animblock.TimeSubs.append(timesub)
		
		self.animCombo.addItem(str(self.animblock.nKeys-1))

	def close_now(self):
		self.hide()
		


class AnimColorEditor(QtGui.QDialog, AnimColorEditor_Ui): 
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)

