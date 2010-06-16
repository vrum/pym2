# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from m2 import *
from array import *

class Ui_AnimEditor(object):
	def setupUi(self, AnimEditor):
		AnimEditor.setObjectName("AnimEditor")
		AnimEditor.resize(540, 373)


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
		self.textEdit.setGeometry(QtCore.QRect(220, 50, 300, 251))
		self.textEdit.setObjectName("textEdit")

		self.rangeEdit = QtGui.QTextEdit(AnimEditor)
		self.rangeEdit.setGeometry(QtCore.QRect(10, 50, 200, 251))
		self.rangeEdit.setObjectName("rangeEdit")

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
		self.rangeEdit.setHtml(QtGui.QApplication.translate("AnimEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

	def setAnimBlock(self,animblock,globalsequ):
		#set the animations
		self.animblock = animblock
		self.type = animblock.type
		for i in globalsequ:
			self.globalCombo.addItem(str(i.Timestamp))

		self.globalCombo.setCurrentIndex(self.animblock.gsequ + 1)
		self.interpolCombo.setCurrentIndex(self.animblock.interpolation)
		self.setTextData()


	def setTextData(self):
		s = ""
		for i in range(self.animblock.nKeys):
			s += str(self.animblock.Times[i]) +":" + str(self.animblock.Keys[i]) +"\n"
		self.textEdit.setPlainText(s)	
		s = ""
		for i in range(self.animblock.nRanges):
			s += str(self.animblock.Ranges[i]) +"\n"
		self.rangeEdit.setPlainText(s)	

	def finished_now(self):
		self.hide()
		(self.animblock.Times,self.animblock.Keys,self.animblock.Ranges)= self.getAnimSub()	
		self.animblock.nTimes = len(self.animblock.Times)	
		self.animblock.nKeys = len(self.animblock.Keys)		
		self.animblock.nRanges = len(self.animblock.Ranges)		
		self.emit(QtCore.SIGNAL("AnimBlockEdited()"))


	def getAnimBlock(self):
		self.animblock.interpolation = self.interpolCombo.currentIndex()
		self.animblock.gsequ = self.globalCombo.currentIndex() - 1
		return self.animblock

	def getAnimSub(self):
		t= self.textEdit.toPlainText().split("\n")
		times = []
		keys = []
		for i in t:
			s = i.split(":")
			if (s[0]!=""):
				times.append(int(s[0]))
				keys.append(s[1])


		key = []
	
		if self.type == DATA_INT:
			for i in keys:
				key.append(int(i))
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
				key.append(k)
		elif self.type == DATA_SHORT: 
			for i in keys:
				key.append(int(i))
		elif self.type == DATA_FLOAT: 
			for i in keys:
				key.append(float(i)) 
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
				key.append(k)
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
				key.append(k)
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
				key.append(k)
		else:
			pass 


		t= self.rangeEdit.toPlainText().split("\n")
		ranges = []
		for i in t:
			if (i!=""):
				temp = i[1:len(i)-1]
				temp.replace(" ","")
				temp = temp.split(",")
				k = Range()
				try:
					k.Start = int(temp[0])
					k.End = int(temp[1])
				except:
					print "FAILED!!!"
				ranges.append(k)

		return (times,key,ranges)

			
	def close_now(self):
		self.hide()



class AnimEditor(QtGui.QDialog, Ui_AnimEditor): 
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)

