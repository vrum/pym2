# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from animeditor import AnimEditor
import m2


attachment_types = { 0:"Mountpoint/Left Wrist", 1:"Right Palm", 2:"Left Palm", 3:"Right Elbow", 4:"Left Elbow", 5:"Right Shoulder", 6:"Left Shoulder",
7:"Right Knee", 8:"Left Knee", 9:"Unk1",10:"Unk2",11:"Helmet",12:"Back",13:"Unk3",14:"Unk4",15:"Bust1",16:"Bust2",17:"Breath",18:"Name",19:"Ground",
20:"Top of Head",21:"Left Palm 2", 22:"Right Palm 2",23:"Unk5",24:"Unk6",25:"Unk7",26:"Right Back Sheath",27:"Left Back Sheath",28:"Middle Back Sheath",
29:"Belly",30:"Left Back",31:"Right Back",32:"Left Hip Sheath",33:"Right Hip Sheath",34:"Bust3",35:"Right Palm 3",36:"Unk8",37:"demolishervehicle1",
38:"demolishervehicle2",39:"vehicle seat 1",40:"vehicle seat 2",41:"vehicle seat 3",42:"vehicle seat 4",43:"Unk9",44:"Unk10",45:"Unk11",46:"Unk12",
47:"Unk13",48:"Unk14",49:"Unk15"}



class AttachmentEditor(QtGui.QDialog):
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
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addAttachment)


		self.line = QtGui.QFrame(Dialog)
		self.line.setGeometry(QtCore.QRect(10, 50, 261, 16))
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")

		self.typeBox = QtGui.QComboBox(Dialog)
		self.typeBox.setGeometry(QtCore.QRect(20, 70, 100, 27))
		self.typeBox.setObjectName("typeBox")
		for i in range(50):			
			self.typeBox.addItem(QtCore.QString())


		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(20, 110, 62, 18))
		self.label.setObjectName("label")

		self.xEdit = QtGui.QLineEdit(Dialog)
		self.xEdit.setGeometry(QtCore.QRect(20, 130, 50, 26))
		self.xEdit.setObjectName("xEdit")

		self.yEdit = QtGui.QLineEdit(Dialog)
		self.yEdit.setGeometry(QtCore.QRect(80, 130, 50, 26))
		self.yEdit.setObjectName("yEdit")

		self.zEdit = QtGui.QLineEdit(Dialog)
		self.zEdit.setGeometry(QtCore.QRect(140, 130, 50, 26))
		self.zEdit.setObjectName("zEdit")

		self.boneBox = QtGui.QComboBox(Dialog)
		self.boneBox.setGeometry(QtCore.QRect(20, 170, 100, 27))
		self.boneBox.setObjectName("boneBox")


		self.enabledIcon = QtGui.QIcon("Icons/edit-enabled.png")
		self.enabledButton = QtGui.QPushButton(self.enabledIcon,"Edit Enabled",Dialog)
		self.enabledButton.setGeometry(QtCore.QRect(20, 200, 140, 28))
		self.enabledButton.setObjectName("enabledButton")
		self.connect(self.enabledButton, QtCore.SIGNAL("clicked()"), self.editEnabled)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.finalizeMe)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)


	def finalizeMe(self):
		self.saveOld()
		self.accept()

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Attachment Editor", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Dialog", "Position:", None, QtGui.QApplication.UnicodeUTF8))

		for i in range(50):
			self.typeBox.setItemText(i, QtGui.QApplication.translate("Dialog", str(i)+": "+attachment_types[i], None, QtGui.QApplication.UnicodeUTF8))

	

	def setModel(self,m2):
		self.m2 = m2
		for i in range(len(self.m2.attachments)):
			self.comboBox.addItem(str(i)+": "+attachment_types[self.m2.attachments[i].Id])
		for i in range(len(self.m2.bones)):
			self.boneBox.addItem("Bone: "+str(i)+"/"+str(self.m2.bones[i].KeyBoneId))
		self.changeEdit()

	def setCurrentEditing(self,i):
		self.comboBox.setCurrentIndex(i)
		self.changeEdit()

	def addAttachment(self):
		att = m2.Attachment()
		att.Enabled.type = m2.DATA_INT
		lu = m2.Lookup()
		lu.Id = self.m2.hdr.attachments.count
		self.m2.attach_lookup.append(lu)
		self.m2.attachments.append(att)
		self.comboBox.addItem(str(self.m2.hdr.attachments.count)+": "+attachment_types[self.m2.attachments[self.m2.hdr.attachments.count].Id])
		self.m2.hdr.attachments.count += 1
		self.m2.hdr.attach_lookup.count += 1


	def changeEdit(self):
		self.saveOld()
		self.last = self.comboBox.currentIndex()
		if not len(self.m2.attachments)<1:
			self.typeBox.setCurrentIndex(self.m2.attachments[self.comboBox.currentIndex()].Id)
			self.xEdit.setText(str(self.m2.attachments[self.comboBox.currentIndex()].pos.x))
			self.yEdit.setText(str(self.m2.attachments[self.comboBox.currentIndex()].pos.y))
			self.zEdit.setText(str(self.m2.attachments[self.comboBox.currentIndex()].pos.z))
			self.boneBox.setCurrentIndex(self.m2.attachments[self.comboBox.currentIndex()].bone)

	def saveOld(self):
		if (self.last == -1):
			return
		self.m2.attachments[self.last].Id = self.typeBox.currentIndex()
		self.m2.attachments[self.last].pos.x = float(self.xEdit.text())
		self.m2.attachments[self.last].pos.y = float(self.yEdit.text())
		self.m2.attachments[self.last].pos.z = float(self.zEdit.text())
		self.m2.attachments[self.last].bone = self.boneBox.currentIndex()
		self.comboBox.setItemText(self.last,str(self.last)+": "+attachment_types[self.m2.attachments[self.last].Id])

	def editEnabled(self):		
		temp = self.comboBox.currentIndex()
		self.EnabledEditor = AnimEditor()
		self.EnabledEditor.setAnimBlock(self.m2.attachments[temp].Enabled,self.m2.gSequ)
		self.EnabledEditor.show()
		self.connect(self.EnabledEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setEnabled)

	def setEnabled(self):
		self.m2.attachments[self.comboBox.currentIndex()].Enabled = self.EnabledEditor.getAnimBlock()




