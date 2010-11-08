



from PyQt4 import QtCore, QtGui
import m2

FLAG_UNLIT = 0x1
FLAG_UNFOGGED = 0x2
FLAG_TWOSIDED = 0x4
FLAG_SPHERE = 0x8
FLAG_NO_D_TEST =0x10
FLAG_NO_D_SET = 0x20

class RenderFlagsEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi()
		self.last = -1

	def setupUi(self):
		self.setObjectName("Dialog")
		self.resize(489, 300)
		self.buttonBox = QtGui.QDialogButtonBox(self)
		self.buttonBox.setGeometry(QtCore.QRect(350, 20, 101, 241))
		self.buttonBox.setOrientation(QtCore.Qt.Vertical)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")

		self.comboBox = QtGui.QComboBox(self)
		self.comboBox.setGeometry(QtCore.QRect(10, 10, 85, 27))
		self.comboBox.setObjectName("comboBox")
		self.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeEdit) 

		self.label = QtGui.QLabel(self)
		self.label.setGeometry(QtCore.QRect(100, 10, 200, 30))
		self.label.setObjectName("label")

		self.addIcon = QtGui.QIcon("Icons/edit-add.png")
		self.addButton = QtGui.QPushButton(self.addIcon,"Add",self)
		self.addButton.setGeometry(QtCore.QRect(240, 10, 92, 28))
		self.addButton.setObjectName("addButton")
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addRenderflag) 

		self.line = QtGui.QFrame(self)
		self.line.setGeometry(QtCore.QRect(10, 50, 201, 16))
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")

		self.groupBox = QtGui.QGroupBox(self)
		self.groupBox.setGeometry(QtCore.QRect(10, 60, 301, 131))
		self.groupBox.setObjectName("groupBox")

		self.frame = QtGui.QFrame(self.groupBox)
		self.frame.setGeometry(QtCore.QRect(0, 30, 301, 80))
		self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtGui.QFrame.Raised)
		self.frame.setObjectName("frame")

		self.unlitCheck = QtGui.QCheckBox(self.frame)
		self.unlitCheck.setGeometry(QtCore.QRect(10, 10, 93, 23))
		self.unlitCheck.setObjectName("unlitCheck")

		self.unfogCheck = QtGui.QCheckBox(self.frame)
		self.unfogCheck.setGeometry(QtCore.QRect(10, 30, 93, 23))
		self.unfogCheck.setObjectName("unfogCheck")

		self.twoCheck = QtGui.QCheckBox(self.frame)
		self.twoCheck.setGeometry(QtCore.QRect(10, 50, 93, 23))
		self.twoCheck.setObjectName("twoCheck")

		self.billCheck = QtGui.QCheckBox(self.frame)
		self.billCheck.setGeometry(QtCore.QRect(110, 10, 231, 23))
		self.billCheck.setObjectName("billCheck")

		self.checkBox = QtGui.QCheckBox(self.frame)
		self.checkBox.setGeometry(QtCore.QRect(110, 30, 181, 23))
		self.checkBox.setObjectName("checkBox")

		self.zCheck = QtGui.QCheckBox(self.frame)
		self.zCheck.setGeometry(QtCore.QRect(110, 50, 121, 23))
		self.zCheck.setObjectName("zCheck")

		self.groupBox_2 = QtGui.QGroupBox(self)
		self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 251, 101))
		self.groupBox_2.setObjectName("groupBox_2")

		self.frame_2 = QtGui.QFrame(self.groupBox_2)
		self.frame_2.setGeometry(QtCore.QRect(0, 20, 211, 61))
		self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")

		self.blendBox = QtGui.QComboBox(self.frame_2)
		self.blendBox.setGeometry(QtCore.QRect(10, 10, 171, 27))
		self.blendBox.setObjectName("blendBox")
		self.blendBox.addItem(QtCore.QString())
		self.blendBox.addItem(QtCore.QString())
		self.blendBox.addItem(QtCore.QString())
		self.blendBox.addItem(QtCore.QString())
		self.blendBox.addItem(QtCore.QString())
		self.blendBox.addItem(QtCore.QString())
		self.blendBox.addItem(QtCore.QString())

		self.retranslateUi()
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.finalizeMe)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)
		QtCore.QMetaObject.connectSlotsByName(self)

	def finalizeMe(self):
		self.saveOld()
		self.accept()

	def retranslateUi(self):
		self.setWindowTitle(QtGui.QApplication.translate("Dialog", "Renderflags Editor", None, QtGui.QApplication.UnicodeUTF8))

		self.label.setText(QtGui.QApplication.translate("Dialog", "Choose Renderflags", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))

		self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Flags", None, QtGui.QApplication.UnicodeUTF8))
		self.unlitCheck.setText(QtGui.QApplication.translate("Dialog", "Unlit", None, QtGui.QApplication.UnicodeUTF8))
		self.unfogCheck.setText(QtGui.QApplication.translate("Dialog", "Unfogged", None, QtGui.QApplication.UnicodeUTF8))
		self.twoCheck.setText(QtGui.QApplication.translate("Dialog", "Two-Sided", None, QtGui.QApplication.UnicodeUTF8))
		self.billCheck.setText(QtGui.QApplication.translate("Dialog", "Sphere Enviroment Map", None, QtGui.QApplication.UnicodeUTF8))
		self.checkBox.setText(QtGui.QApplication.translate("Dialog", "No Depth Set", None, QtGui.QApplication.UnicodeUTF8))
		self.zCheck.setText(QtGui.QApplication.translate("Dialog", "No Depth Test", None, QtGui.QApplication.UnicodeUTF8))

		self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Blending Mode", None, QtGui.QApplication.UnicodeUTF8))
		self.blendBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Opaque", None, QtGui.QApplication.UnicodeUTF8))
		self.blendBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Modulate", None, QtGui.QApplication.UnicodeUTF8))
		self.blendBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Decal", None, QtGui.QApplication.UnicodeUTF8))
		self.blendBox.setItemText(3, QtGui.QApplication.translate("Dialog", "Additive", None, QtGui.QApplication.UnicodeUTF8))
		self.blendBox.setItemText(4, QtGui.QApplication.translate("Dialog", "Modulate 2x", None, QtGui.QApplication.UnicodeUTF8))
		self.blendBox.setItemText(5, QtGui.QApplication.translate("Dialog", "Fade", None, QtGui.QApplication.UnicodeUTF8))
		self.blendBox.setItemText(6, QtGui.QApplication.translate("Dialog", "\"Deeprun\"", None, QtGui.QApplication.UnicodeUTF8))


	def saveOld(self):
		if (self.last == -1):
			return

		flags = 0
		if (self.unlitCheck.checkState() == 2):
			flags += FLAG_UNLIT

		if self.unfogCheck.checkState() == 2:
			flags += FLAG_UNFOGGED

		if self.twoCheck.checkState() == 2:
			flags += FLAG_TWOSIDED

		if self.billCheck.checkState() == 2:
			flags += FLAG_SPHERE

		if self.zCheck.checkState() == 2:
			flags += FLAG_NO_D_TEST

		if self.checkBox.checkState() == 2:
			flags += FLAG_NO_D_SET

		self.m2.renderflags[self.last].flags = flags
		self.m2.renderflags[self.last].blend = self.blendBox.currentIndex()

	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		for i in range(len(self.m2.renderflags)):
			self.comboBox.addItem(str(i))
		self.changeEdit()

	def addRenderflag(self):
		rf = m2.Renderflags()
		self.m2.renderflags.append(rf)
		self.comboBox.addItem(str(self.m2.hdr.renderflags.count))
		self.m2.hdr.renderflags.count += 1

	def changeEdit(self):
		self.saveOld()
		self.last = self.comboBox.currentIndex()
		rf = self.m2.renderflags[self.comboBox.currentIndex()]
		
		if rf.flags & FLAG_UNLIT:
			self.unlitCheck.setCheckState(2)
		else:
			self.unlitCheck.setCheckState(0)

		if rf.flags & FLAG_UNFOGGED:
			self.unfogCheck.setCheckState(2)
		else:
			self.unfogCheck.setCheckState(0)

		if rf.flags & FLAG_TWOSIDED:
			self.twoCheck.setCheckState(2)
		else:
			self.twoCheck.setCheckState(0)

		if rf.flags & FLAG_SPHERE:
			self.billCheck.setCheckState(2)
		else:
			self.billCheck.setCheckState(0)

		
		if rf.flags & FLAG_NO_D_TEST:
			self.zCheck.setCheckState(2)
		else:
			self.zCheck.setCheckState(0)

		if rf.flags & FLAG_NO_D_SET:
			self.checkBox.setCheckState(2)
		else:
			self.checkBox.setCheckState(0)

		self.blendBox.setCurrentIndex(rf.blend)


