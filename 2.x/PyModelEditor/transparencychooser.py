# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui
from animeditor import AnimEditor
import m2

class TransparencyChooser(QtGui.QDialog):
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
		self.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeEdit) 

		self.editButton = QtGui.QPushButton(Dialog)
		self.editButton.setGeometry(QtCore.QRect(110, 10, 92, 28))
		self.editButton.setObjectName("editButton")
		self.connect(self.editButton, QtCore.SIGNAL("clicked()"), self.editTransparency) 

		self.addIcon = QtGui.QIcon("Icons/edit-add.png")
		self.addButton = QtGui.QPushButton(self.addIcon,"Add",Dialog)
		self.addButton.setGeometry(QtCore.QRect(210, 10, 92, 28))
		self.addButton.setObjectName("addButton")
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addTransparency) 

		self.line = QtGui.QFrame(Dialog)
		self.line.setGeometry(QtCore.QRect(10, 40, 201, 21))
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")

		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(20, 70, 361, 211))
		self.label.setObjectName("label")

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Edit Transparency", None, QtGui.QApplication.UnicodeUTF8))
		self.editButton.setText(QtGui.QApplication.translate("Dialog", "Edit", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Dialog", "Transparency used by:", None, QtGui.QApplication.UnicodeUTF8))

	
	def setModel(self,m2):
		self.m2 = m2
		for i in range(len(self.m2.transparency)):
			self.comboBox.addItem(str(i))
		self.changeEdit()

	def changeEdit(self):
		s = "This transparency is used by:\n"
		for i in self.m2.materials[0]:
			try:
				if(self.m2.trans_lookup[i.transparency].Id == self.comboBox.currentIndex()):
					s += "Layer "+str(i.flags)+" Geoset "+str(i.submesh)+":"+str(i.submesh2)+"\n"
			except:
				pass
		self.label.setText(s)

	def setTransparency(self):
		self.m2.transparency[self.comboBox.currentIndex()].alpha = self.TransparencyEditor.getAnimBlock()

	def editTransparency(self):		
		transparency = self.comboBox.currentIndex()
		self.TransparencyEditor = AnimEditor()
		self.TransparencyEditor.setAnimBlock(self.m2.transparency[transparency].alpha,self.m2.gSequ)
		self.TransparencyEditor.show()
		self.connect(self.TransparencyEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setTransparency)


	def addTransparency(self):
		tr = m2.Transparency()
		tr.alpha.type = m2.DATA_SHORT
		
		tl = m2.Lookup()
		tl.Id = self.m2.hdr.transparency.count

		self.comboBox.addItem(str(len(self.m2.transparency)))

		self.m2.transparency.append(tr)
		self.m2.hdr.transparency.count += 1

		self.m2.trans_lookup.append(tl)
		self.m2.hdr.trans_lookup.count += 1

