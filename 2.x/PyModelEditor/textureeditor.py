# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui
import m2

tex_type = { 0 : 0, 1 : 1, 2:2, 3:3, 4:6, 5:8,6:9,7:10,8:11,9:12,10:13,11:14}
type_tex = { 0 : 0, 1 : 1, 2:2, 3:3, 6:4,8:5,9:6,10:7,11:8,12:9,13:10,14:11}

TextureTypes = { 0 : "Hardcoded" , 1 : "Body/Clothes" , 2 : "Items", 3 : "ArmorReflect?", 6 : "Hair/Beard",
8 : "Tauren fur", 9 : "Inventory Art 1", 10 : "quillboarpinata", 11 : "Skin for creatures or gameobjects 1",
12 : "Skin for creatures or gameobjects 2" ,13 : "Skin for creatures or gameobjects 3", 14 : "Inventory Art 2"} 

class TextureEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
		self.last = -1

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(480, 327)
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(130, 280, 341, 32))
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
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addTexture)

		self.line = QtGui.QFrame(Dialog)
		self.line.setGeometry(QtCore.QRect(10, 50, 261, 16))
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")

		self.typeBox = QtGui.QComboBox(Dialog)
		self.typeBox.setGeometry(QtCore.QRect(20, 70, 100, 27))
		self.typeBox.setObjectName("typeBox")
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())
		self.typeBox.addItem(QtCore.QString())

		self.lineEdit = QtGui.QLineEdit(Dialog)
		self.lineEdit.setGeometry(QtCore.QRect(20, 110, 361, 26))
		self.lineEdit.setObjectName("lineEdit")

		self.xwrap = QtGui.QCheckBox(Dialog)
		self.xwrap.setGeometry(QtCore.QRect(20, 140, 100, 26))
		self.xwrap.setObjectName("xwrap")

		self.ywrap = QtGui.QCheckBox(Dialog)
		self.ywrap.setGeometry(QtCore.QRect(130, 140, 100, 26))
		self.ywrap.setObjectName("ywrap")

		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(20, 170, 62, 18))
		self.label.setObjectName("label")

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.finalizeMe)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)


	def finalizeMe(self):
		self.saveOld()
		self.accept()

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Texture Editor", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Dialog", "Info", None, QtGui.QApplication.UnicodeUTF8))
		self.ywrap.setText(QtGui.QApplication.translate("Dialog", "Y-Wrap", None, QtGui.QApplication.UnicodeUTF8))
		self.xwrap.setText(QtGui.QApplication.translate("Dialog", "X-Wrap", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))


		self.typeBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Hardcoded", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Body or Clothes", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Item/Capes", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(3, QtGui.QApplication.translate("Dialog", "Armor Reflect ?", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(4, QtGui.QApplication.translate("Dialog", "Hair/Beard", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(5, QtGui.QApplication.translate("Dialog", "Fur", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(6, QtGui.QApplication.translate("Dialog", "Inventory 1", None, QtGui.QApplication.UnicodeUTF8))		
		self.typeBox.setItemText(7, QtGui.QApplication.translate("Dialog", "Strange thing oO", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(8, QtGui.QApplication.translate("Dialog", "DBC Reference 1", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(9, QtGui.QApplication.translate("Dialog", "DBC Reference 2", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(10, QtGui.QApplication.translate("Dialog", "DBC Reference 3", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(11, QtGui.QApplication.translate("Dialog", "Inventory 2", None, QtGui.QApplication.UnicodeUTF8))


	def saveOld(self):
		if (self.last == -1):
			return
		name = str(self.lineEdit.text())
		name.encode("cp1252")
		if len(name) == 0:
			name = "\0"
		if name[len(name)-1] != "\0":
				name += "\0"
		self.m2.textures[self.last].name = name
		self.m2.textures[self.last].type = tex_type[self.typeBox.currentIndex()]
		flags = 0
		if (self.xwrap.checkState() == 2):
			flags += 1
		if (self.ywrap.checkState() == 2):
			flags += 2

		self.m2.textures[self.last].flags = flags

		self.comboBox.setItemText(self.last,str(self.last)+": "+TextureTypes[self.m2.textures[self.last].type]+" "+self.m2.textures[self.last].name)

	def setModel(self,m2):
		self.m2 = m2
		for i in range(len(self.m2.textures)):
			self.comboBox.addItem(str(i)+": "+TextureTypes[self.m2.textures[i].type]+" "+self.m2.textures[i].name)
		self.changeEdit()

	def addTexture(self):
		tex = m2.Texture()
		self.m2.textures.append(tex)
		lu = m2.Lookup()
		lu.Id = self.m2.hdr.textures.count
		self.m2.tex_lookup.append(lu)
		self.comboBox.addItem(str(self.m2.hdr.textures.count))
		self.m2.hdr.textures.count += 1
		self.m2.hdr.tex_lookup.count += 1

	def changeEdit(self):
		self.saveOld()
		self.last = self.comboBox.currentIndex()
		self.typeBox.setCurrentIndex(type_tex[self.m2.textures[self.comboBox.currentIndex()].type])
		self.lineEdit.setText(self.m2.textures[self.comboBox.currentIndex()].name)

		if self.m2.textures[self.comboBox.currentIndex()].flags & 1:
			self.xwrap.setCheckState(2)
		else:
			self.xwrap.setCheckState(0) 

		if self.m2.textures[self.comboBox.currentIndex()].flags & 2:
			self.ywrap.setCheckState(2)
		else:
			self.ywrap.setCheckState(0) 

