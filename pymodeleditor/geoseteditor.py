# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui

from glView import *

GeosetTypes = { "00" : "Hairstyles/Root", "01" : "Facial1", "02" : "Facial2", "03" : "Facial3",
"04" : "Bracers", "05" : "Boots", "06" : "Unknown1", "07" : "Ears", "08" : "Wristbands", "09" : "Kneepads",
"10" : "Unknown2", "11" : "Pants", "12" : "Tabard", "13" : "Trousers/Kilt", "14" : "Unknown3",
"15" : "Cape", "16" : "Unknown4", "17" : "Eyeglows", "18" : "Belt" } 

def GeosetName(Id):		
	s = str(Id)#Convert the GeosetId to a string
	j = len(s)#Get the Length of the string
	if (j<3):#If it's only two digits...
		s = "00"#the Id is 00
	elif(j<4):#if it's length is <4, then it has only one digit
		s =  "0" + s[0]
	else:#get the two important digits
		s =  s[0:2]
	return GeosetTypes[s]#print mesh_id and it's translation

def GeosetId(Id):		
	s = str(Id)
	j = len(s)
	if (j<3):
		s = "00"
	elif(j<4):
		s =  "0" + s[0]
	else:
		s =  s[0:2]
	return int(s)

#get the lower id
def GeosetGroupNumber(Id):		
	s = str(Id)
	j = len(s)
	if (j<2):
		s = "0" + s		
	elif (j<3):
		s = s
	elif (j<4):
		s =  s[1:3]
	else:
		s =  s[2:4]
	return s


class GeosetEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
		self.last = -1

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(583, 419)
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(230, 370, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")

		self.comboBox = QtGui.QComboBox(Dialog)
		self.comboBox.setGeometry(QtCore.QRect(10, 10, 85, 27))
		self.comboBox.setObjectName("comboBox")
		self.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeEdit) 

		self.idBox = QtGui.QComboBox(Dialog)
		self.idBox.setGeometry(QtCore.QRect(450, 40, 85, 27))
		self.idBox.setObjectName("idBox")
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())
		self.idBox.addItem(QtCore.QString())

		self.GlView = GlWidget(Dialog)
		self.GlView.setGeometry(QtCore.QRect(10, 40, 431, 321))
		self.GlView.setObjectName("GlView")
		self.GlView.setMode(1)

		self.lineEdit = QtGui.QLineEdit(Dialog)
		self.lineEdit.setGeometry(QtCore.QRect(450, 70, 91, 26))
		self.lineEdit.setObjectName("lineEdit")

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)


	def finalizeMe(self):
		self.saveOld()
		self.accept()

	def changeEdit(self):
		self.saveOld()
		self.last = self.comboBox.currentIndex()
		self.GlView.setModel(self.m2,self.skin,self.comboBox.currentIndex())
		self.idBox.setCurrentIndex(GeosetId(self.skin.mesh[self.comboBox.currentIndex()].mesh_id))
		self.lineEdit.setText(GeosetGroupNumber(self.skin.mesh[self.comboBox.currentIndex()].mesh_id))

	def saveOld(self):
		if (self.last == -1):
			return

		subId = str(self.lineEdit.text())
		subId.encode("cp1252")
		while len(subId) < 2:
			subId = "0" +subId
		if len(subId) > 2:#ugly Hack!!
			print ("Wrong Length " + str(len(subId))+" correct would be 0-2!")
			subId = subId[0:2]

		mainId = str(self.idBox.currentIndex())
		while len(mainId) < 2:
			mainId = "0" +mainId

		newId = mainId +subId
		self.skin.mesh[self.last].mesh_id = int(newId)
		

		self.comboBox.setItemText(self.last,str(self.last)+": "+GeosetName(self.skin.mesh[self.last].mesh_id))

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

		self.idBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Hairstyles/Root", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Facial 1", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Facial 2", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(3, QtGui.QApplication.translate("Dialog", "Facial 3", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(4, QtGui.QApplication.translate("Dialog", "Bracers", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(5, QtGui.QApplication.translate("Dialog", "Boots", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(6, QtGui.QApplication.translate("Dialog", "Unknown 1", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(7, QtGui.QApplication.translate("Dialog", "Ears", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(8, QtGui.QApplication.translate("Dialog", "Wristbands", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(9, QtGui.QApplication.translate("Dialog", "Kneepads", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(10, QtGui.QApplication.translate("Dialog", "Unknown 2", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(11, QtGui.QApplication.translate("Dialog", "Pants", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(12, QtGui.QApplication.translate("Dialog", "Tabard", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(13, QtGui.QApplication.translate("Dialog", "Trousers/Kilt", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(14, QtGui.QApplication.translate("Dialog", "Unknown 3", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(15, QtGui.QApplication.translate("Dialog", "Cape", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(16, QtGui.QApplication.translate("Dialog", "Unknown 4", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(17, QtGui.QApplication.translate("Dialog", "Eyeglows", None, QtGui.QApplication.UnicodeUTF8))
		self.idBox.setItemText(18, QtGui.QApplication.translate("Dialog", "Belt", None, QtGui.QApplication.UnicodeUTF8))


	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		for i in range(len(self.skin.mesh)):
			self.comboBox.addItem(str(i)+": "+GeosetName(self.skin.mesh[i].mesh_id))
		self.changeEdit()

