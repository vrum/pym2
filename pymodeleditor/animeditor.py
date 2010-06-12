# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from m2 import *
from array import *

class Ui_AnimEditor(object):
	def setupUi(self, AnimEditor):
		AnimEditor.setObjectName("AnimEditor")
		AnimEditor.resize(540, 373)

		self.currentAnim = -1

		self.animCombo = QtGui.QComboBox(AnimEditor)
		self.animCombo.setGeometry(QtCore.QRect(10, 10, 85, 27))
		self.animCombo.setObjectName("animCombo")

		self.addIcon = QtGui.QIcon("Icons/edit-add.png")
		self.addButton = QtGui.QPushButton(self.addIcon,"Add AnimSub",self)
		self.addButton.setGeometry(QtCore.QRect(100, 10, 122, 27))
		self.addButton.setObjectName("addButton")
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addAnimSub)

		self.interpolCombo = QtGui.QComboBox(AnimEditor)
		self.interpolCombo.setGeometry(QtCore.QRect(230, 10, 170, 27))
		self.interpolCombo.setObjectName("interpolCombo")
		self.interpolCombo.addItem("No Interpolation")
		self.interpolCombo.addItem("Linear Interpolation")
		self.interpolCombo.addItem("Hermite Interpolation")
		self.interpolCombo.addItem("Bezier Interpolation")

		self.globalCombo = QtGui.QComboBox(AnimEditor)
		self.globalCombo.setGeometry(QtCore.QRect(410, 10, 85, 27))
		self.globalCombo.setObjectName("globalCombo")
		self.globalCombo.addItem("None: -1")

		self.buttonBox = QtGui.QDialogButtonBox(AnimEditor)
		self.buttonBox.setGeometry(QtCore.QRect(310, 320, 206, 34))
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.finished_now) 
		self.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.close_now)

		self.textEdit = QtGui.QTextEdit(AnimEditor)
		self.textEdit.setGeometry(QtCore.QRect(10, 50, 511, 251))
		self.textEdit.setObjectName("textEdit")

		self.retranslateUi(AnimEditor)
		QtCore.QMetaObject.connectSlotsByName(AnimEditor)

		self.type = DATA_INT

	def retranslateUi(self, AnimEditor):
		AnimEditor.setWindowTitle(QtGui.QApplication.translate("AnimEditor", "Animation Block Editor", None, QtGui.QApplication.UnicodeUTF8))
		self.textEdit.setHtml(QtGui.QApplication.translate("AnimEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

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
		self.setTextData(self.currentAnim)
		self.connect(self.animCombo, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeAnimation) 


	def setTextData(self,anim):
		s = ""
		if self.currentAnim !=-1:
			if(self.animblock.nKeys > anim):
				for i in range(self.animblock.KeySubs[anim].nEntries):
					s += str(self.animblock.TimeSubs[anim].values[i]) +":" + str(self.animblock.KeySubs[anim].values[i]) +"\n"		
		self.textEdit.setPlainText(s)

	def finished_now(self):
		self.hide()
		(self.animblock.TimeSubs[self.currentAnim],self.animblock.KeySubs[self.currentAnim])= self.getAnimSub()		
		self.emit(QtCore.SIGNAL("AnimBlockEdited()"))

	def changeAnimation(self):
		if self.currentAnim !=-1:
			(self.animblock.TimeSubs[self.currentAnim],self.animblock.KeySubs[self.currentAnim])= self.getAnimSub()
		self.currentAnim = self.animCombo.currentIndex()
		self.setTextData(self.currentAnim)

	def getAnimBlock(self):
		self.animblock.interpolation = self.interpolCombo.currentIndex()
		self.animblock.gsequ = self.globalCombo.currentIndex() - 1
		return self.animblock

	def getAnimSub(self):
		t= self.textEdit.toPlainText().split("\n")
		c = 0
		times = []
		keys = []
		for i in t:
			s = i.split(":")
			if (s[0]!=""):
				times.append(int(s[0]))
				keys.append(s[1])
				c += 1

		timesub = AnimSub()
		timesub.type = DATA_INT
		timesub.nEntries = c
		timesub.values = times

		keysub = AnimSub()
		keysub.type = self.type
		keysub.nEntries = c

		
		if self.type == DATA_INT:
			for i in keys:
				keysub.values.append(int(i))
		elif self.type == DATA_VEC3:
			for i in keys:
				temp = i[1:len(i)-1]
				temp.replace(" ","")
				temp = temp.split(",")
				k = Vec3()
				try:
					k.x = float(temp[0])
					k.y = float(temp[1])
					k.z = float(temp[2])
				except:
					print "FAILED!!!"
				keysub.values.append(k)
		elif self.type == DATA_SHORT: 
			for i in keys:
				keysub.values.append(int(i))
		elif self.type == DATA_FLOAT: 
			for i in keys:
				keysub.values.append(float(i)) 
		elif self.type == DATA_VEC9: 
			for i in keys:
				temp = i[1:len(i)-1]
				temp.replace(" ","")
				temp = temp.split(",")
				k = Vec9()
				try:
					k.x1 = float(temp[0])
					k.x2 = float(temp[1])
					k.x3 = float(temp[2])
					k.y1 = float(temp[3])
					k.y2 = float(temp[4])
					k.y3 = float(temp[5])
					k.z1 = float(temp[6])
					k.z2 = float(temp[7])
					k.z3 = float(temp[8])
				except:
					print "FAILED!!!"
				keysub.values.append(k)
		elif self.type == DATA_VEC2: 
			for i in keys:
				temp = i[1:len(i)-1]
				temp.replace(" ","")
				temp = temp.split(",")
				k = Vec2()
				try:
					k.x = float(temp[0])
					k.y = float(temp[1])
				except:
					print "FAILED!!!"
				keysub.values.append(k)
		elif self.type == DATA_QUAT: 
			for i in keys:
				temp = i[1:len(i)-1]
				temp.replace(" ","")
				temp = temp.split(",")
				k = Quat()
				try:
					k.x = int(temp[0])
					k.y = int(temp[1])
					k.z = int(temp[2])
					k.w = int(temp[3])
				except:
					print "FAILED!!!"
				keysub.values.append(k)
		else:
			pass 

		return (timesub,keysub)

			
	def addAnimSub(self):
		self.animCombo.addItem(str(self.animblock.nKeys))
		self.animblock.nKeys += 1
		keysub = AnimSub()
		keysub.type = self.animblock.type
		keysub.nEntries = 1
		if self.type == DATA_INT:
			keysub.values.append(int(0))
		elif self.type == DATA_VEC3:
			k = Vec3()
			keysub.values.append(k)
		elif self.type == DATA_SHORT: 
			keysub.values.append(int(0))
		elif self.type == DATA_FLOAT: 
			keysub.values.append(float(0)) 
		elif self.type == DATA_VEC9: 
			k = Vec9()
			keysub.values.append(k)			
		elif self.type == DATA_VEC2: 
			k = Vec2()
			keysub.values.append(k)				
		elif self.type == DATA_QUAT: 
			k = Quat()
			keysub.values.append(k)
		else:
			pass 
		self.animblock.KeySubs.append(keysub)
		self.animblock.nTimes += 1
		timesub = AnimSub()
		timesub.nEntries = 1
		timesub.values.append(0)
		self.animblock.TimeSubs.append(timesub)

	def close_now(self):
		self.hide()



class AnimEditor(QtGui.QDialog, Ui_AnimEditor): 
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)

