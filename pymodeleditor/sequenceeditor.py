# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui


import m2
from DBC.animdbc import *


class SequenceEditor(QtGui.QDialog):
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

		self.animBox = QtGui.QComboBox(Dialog)
		self.animBox.setGeometry(QtCore.QRect(10, 40, 120, 27))
		self.animBox.setObjectName("animBox")
		for i in animdbc.entries:
			self.animBox.addItem(str(i.Id)+" "+giveAnimName(i.Id))


		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(140, 40, 80, 26))
		self.label.setObjectName("label")

		self.subEdit = QtGui.QLineEdit(Dialog)
		self.subEdit.setGeometry(QtCore.QRect(220, 40, 50, 26))
		self.subEdit.setObjectName("subEdit")

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.finalizeMe)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)


	def finalizeMe(self):
		self.saveOld()
		self.accept()

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Sequence Editor", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Dialog", "SubAnimId:", None, QtGui.QApplication.UnicodeUTF8))

	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		for i in range(len(self.m2.animations)):
			self.comboBox.addItem(str(i)+": "+giveAnimName(m2.animations[i].animId)+" ("+str(m2.animations[i].animId)+")")
		self.changeEdit()

	def setCurrentEditing(self,i):
		self.comboBox.setCurrentIndex(i)
		self.changeEdit()

	def changeEdit(self):
		self.saveOld()
		self.last = self.comboBox.currentIndex()
		if not len(self.m2.animations)<1:
			self.animBox.setCurrentIndex(self.m2.animations[self.last].animId)
			self.subEdit.setText(str(self.m2.animations[self.last].subId))

	def saveOld(self):
		if (self.last == -1):
			return
		self.m2.animations[self.last].animId = self.animBox.currentIndex()
		self.m2.animations[self.last].subId = int(self.subEdit.text())
		self.comboBox.setItemText(self.last,str(self.last)+": "+giveAnimName(self.m2.animations[self.last].animId)+" ("+str(self.m2.animations[self.last].animId)+")")

