# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui
from animeditor import AnimEditor
from animcoloreditor import AnimColorEditor
import m2


class ColorEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
		self.last = -1
		
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(450, 150)
		
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(90, 110, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		
		self.colorList = QtGui.QComboBox(Dialog)
		self.colorList.setGeometry(QtCore.QRect(10, 10, 69, 22))
		self.colorList.setObjectName("colorList")
		self.connect(self.colorList, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeEdit) 
		
		self.line = QtGui.QFrame(Dialog)
		self.line.setGeometry(QtCore.QRect(10, 40, 211, 16))
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")
		
		self.addIcon = QtGui.QIcon("Icons/edit-add.png")
		self.addButton = QtGui.QPushButton(self.addIcon,"Add",Dialog)
		self.addButton.setGeometry(QtCore.QRect(100, 10, 75, 23))
		self.addButton.setObjectName("addButton")
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addColor)
		
		self.colorButton = QtGui.QPushButton(Dialog)
		self.colorButton.setGeometry(QtCore.QRect(150, 60, 75, 23))
		self.colorButton.setObjectName("colorButton")
		self.connect(self.colorButton, QtCore.SIGNAL("clicked()"), self.editColor)
		
		self.alphaButton = QtGui.QPushButton(Dialog)
		self.alphaButton.setGeometry(QtCore.QRect(240, 60, 75, 23))
		self.alphaButton.setObjectName("alphaButton")
		self.connect(self.alphaButton, QtCore.SIGNAL("clicked()"), self.editAlpha)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Color Editor", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
		self.colorButton.setText(QtGui.QApplication.translate("Dialog", "Edit Color", None, QtGui.QApplication.UnicodeUTF8))
		self.alphaButton.setText(QtGui.QApplication.translate("Dialog", "Edit Alpha", None, QtGui.QApplication.UnicodeUTF8))
		


	def editColor(self):		
		temp = self.colorList.currentIndex()
		self.ColEditor = AnimColorEditor()
		self.ColEditor.setAnimBlock(self.m2.colors[temp].color,self.m2.gSequ)
		self.ColEditor.show()
		self.connect(self.ColEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setColor)

	def setColor(self):
		self.m2.colors[self.colorList.currentIndex()].color = self.ColEditor.getAnimBlock()

	def editAlpha(self):		
		temp = self.colorList.currentIndex()
		self.AlphaEditor = AnimEditor()
		self.AlphaEditor.setAnimBlock(self.m2.colors[temp].alpha,self.m2.gSequ)
		self.AlphaEditor.show()
		self.connect(self.AlphaEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setAlpha)

	def setAlpha(self):
		self.m2.colors[self.colorList.currentIndex()].alpha = self.AlphaEditor.getAnimBlock()


	def finalizeMe(self):
		self.saveOld()
		self.accept()

	def setCurrentEditing(self,i):
		self.colorList.setCurrentIndex(i)
		self.changeEdit()

	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		for i in range(len(self.m2.colors)):
			self.colorList.addItem(str(i))
		self.changeEdit()
		
		
	def addColor(self):
		l = m2.Color()
		l.color.type = m2.DATA_VEC3
		l.alpha.type = m2.DATA_FLOAT

		self.m2.colors.append(l)
		
		self.colorList.addItem(str(self.m2.hdr.colors.count))
		self.m2.hdr.colors.count += 1

	def saveOld(self):
		if (self.last == -1):
			return		
			
			
	def changeEdit(self):
		self.saveOld()
		self.last = self.colorList.currentIndex()
			
			
		
		
		
