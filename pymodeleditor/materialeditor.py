

# Form implementation generated from reading ui file 'Material.ui'
#
# Created: Sun Jun  6 19:48:55 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import skin

TextureTypes = { 0 : "Hardcoded" , 1 : "Body/Clothes" , 2 : "Items", 3 : "ArmorReflect?", 6 : "Hair/Beard",
8 : "Tauren fur", 9 : "Inventory Art 1", 10 : "quillboarpinata", 11 : "Skin for creatures or gameobjects 1",
12 : "Skin for creatures or gameobjects 2" ,13 : "Skin for creatures or gameobjects 3", 14 : "Inventory Art 2"} 

GeosetTypes = { "00" : "Hairstyles", "01" : "Facial1", "02" : "Facial2", "03" : "Facial3",
"04" : "Bracers", "05" : "Boots", "06" : "Unknown1", "07" : "Ears", "08" : "Wristbands", "09" : "Kneepads",
"10" : "Unknown2", "11" : "Pants", "12" : "Tabard", "13" : "Trousers/Kilt", "14" : "Unknown3",
"15" : "Cape", "16" : "Unknown4", "17" : "Eyeglows", "18" : "Belt" } 

class MaterialEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
		self.lastchoice = -1

	def setupUi(self, MaterialEditor):
		MaterialEditor.setObjectName("MaterialEditor")
		MaterialEditor.resize(527, 377)
		self.buttonBox = QtGui.QDialogButtonBox(MaterialEditor)
		self.buttonBox.setGeometry(QtCore.QRect(180, 340, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")

		self.chooseBox = QtGui.QComboBox(MaterialEditor)
		self.chooseBox.setGeometry(QtCore.QRect(10, 10, 85, 27))
		self.chooseBox.setObjectName("chooseBox")
		self.connect(self.chooseBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeEdit) 

		self.addIcon = QtGui.QIcon("Icons/edit-add.png")
		self.addButton = QtGui.QPushButton(self.addIcon,"Add",MaterialEditor)
		self.addButton.setGeometry(QtCore.QRect(110, 10, 92, 28))
		self.addButton.setObjectName("addButton")
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addMaterial) 

		self.frame = QtGui.QFrame(MaterialEditor)
		self.frame.setGeometry(QtCore.QRect(20, 70, 431, 231))
		self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtGui.QFrame.Raised)
		self.frame.setObjectName("frame")

		self.checkBox = QtGui.QCheckBox(self.frame)
		self.checkBox.setGeometry(QtCore.QRect(10, 10, 93, 23))
		self.checkBox.setObjectName("checkBox")

		self.submeshChoose = QtGui.QComboBox(self.frame)
		self.submeshChoose.setGeometry(QtCore.QRect(10, 60, 85, 27))
		self.submeshChoose.setObjectName("submeshChoose")
		self.label = QtGui.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(10, 40, 71, 18))
		self.label.setObjectName("label")

		self.colorChoose = QtGui.QComboBox(self.frame)
		self.colorChoose.setGeometry(QtCore.QRect(10, 120, 85, 27))
		self.colorChoose.setObjectName("colorChoose")
		self.label_2 = QtGui.QLabel(self.frame)
		self.label_2.setGeometry(QtCore.QRect(10, 100, 62, 18))
		self.label_2.setObjectName("label_2")

		self.label_3 = QtGui.QLabel(self.frame)
		self.label_3.setGeometry(QtCore.QRect(160, 40, 62, 20))
		self.label_3.setObjectName("label_3")
		self.textureChoose = QtGui.QComboBox(self.frame)
		self.textureChoose.setGeometry(QtCore.QRect(160, 60, 85, 27))
		self.textureChoose.setObjectName("textureChoose")

		self.transparencyChoose = QtGui.QComboBox(self.frame)
		self.transparencyChoose.setGeometry(QtCore.QRect(160, 120, 85, 27))
		self.transparencyChoose.setObjectName("transparencyChoose")
		self.label_4 = QtGui.QLabel(self.frame)
		self.label_4.setGeometry(QtCore.QRect(160, 100, 101, 18))
		self.label_4.setObjectName("label_4")

		self.label_5 = QtGui.QLabel(self.frame)
		self.label_5.setGeometry(QtCore.QRect(300, 40, 101, 18))
		self.label_5.setObjectName("label_5")
		self.uvanimChoose = QtGui.QComboBox(self.frame)
		self.uvanimChoose.setGeometry(QtCore.QRect(300, 60, 85, 27))
		self.uvanimChoose.setObjectName("uvanimChoose")

		self.label_6 = QtGui.QLabel(self.frame)
		self.label_6.setGeometry(QtCore.QRect(300, 100, 101, 18))
		self.label_6.setObjectName("label_6")
		self.renderflagChoose = QtGui.QComboBox(self.frame)
		self.renderflagChoose.setGeometry(QtCore.QRect(300, 120, 85, 27))
		self.renderflagChoose.setObjectName("renderflagChoose")

		self.label_7 = QtGui.QLabel(self.frame)
		self.label_7.setGeometry(QtCore.QRect(10, 160, 62, 18))
		self.label_7.setObjectName("label_7")
		self.texunitChoose = QtGui.QComboBox(self.frame)
		self.texunitChoose.setGeometry(QtCore.QRect(10, 180, 85, 27))
		self.texunitChoose.setObjectName("texunitChoose")

		self.label_8 = QtGui.QLabel(self.frame)
		self.label_8.setGeometry(QtCore.QRect(160, 160, 62, 18))
		self.label_8.setObjectName("label_8")
		self.shadingEdit = QtGui.QLineEdit(self.frame)
		self.shadingEdit.setGeometry(QtCore.QRect(160, 180, 113, 26))
		self.shadingEdit.setObjectName("shadingEdit")

		self.label_9 = QtGui.QLabel(self.frame)
		self.label_9.setGeometry(QtCore.QRect(300, 160, 62, 18))
		self.label_9.setObjectName("label_9")
		self.modeEdit = QtGui.QLineEdit(self.frame)
		self.modeEdit.setGeometry(QtCore.QRect(300, 180, 113, 26))
		self.modeEdit.setObjectName("modeEdit")

		self.retranslateUi(MaterialEditor)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), MaterialEditor.finalizeMe)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), MaterialEditor.reject)
		QtCore.QMetaObject.connectSlotsByName(MaterialEditor)

	def retranslateUi(self, MaterialEditor):
		MaterialEditor.setWindowTitle(QtGui.QApplication.translate("MaterialEditor", "Material Editor", None, QtGui.QApplication.UnicodeUTF8))
		self.checkBox.setText(QtGui.QApplication.translate("MaterialEditor", "Animated", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("MaterialEditor", "Submesh:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate("MaterialEditor", "Color:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setText(QtGui.QApplication.translate("MaterialEditor", "Texture:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_4.setText(QtGui.QApplication.translate("MaterialEditor", "Transparency:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_5.setText(QtGui.QApplication.translate("MaterialEditor", "UV Animation:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_6.setText(QtGui.QApplication.translate("MaterialEditor", "Renderflags:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_7.setText(QtGui.QApplication.translate("MaterialEditor", "TexUnit:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_8.setText(QtGui.QApplication.translate("MaterialEditor", "Shading:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_9.setText(QtGui.QApplication.translate("MaterialEditor", "Mode:", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))


	def finalizeMe(self):
		self.saveOld()
		self.accept()


	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		for i in range(len(self.skin.texunit)):
			self.chooseBox.addItem(str(i))
		if len(self.skin.texunit) != 0:
			self.lastchoice = 0

		for i in range(len(self.skin.mesh)):
			temp = str(self.skin.mesh[i].mesh_id)
			j = len(temp)
			if (j<3):				
				number = temp
				temp = "00"
			elif(j<4):
				number = temp[1::]
				temp =  "0" + temp[0]
			else:
				number = temp[2::]
				temp =  temp[0:2]
			try:
				self.submeshChoose.addItem(str(i)+":"+GeosetTypes[temp]+ " "+number)
			except:
				print temp
				print self.skin.mesh[i].mesh_id
				self.submeshChoose.addItem(str(i)+":"+str(self.skin.mesh[i].mesh_id))

		for i in range(len(self.m2.colors)+1):
			self.colorChoose.addItem(str(i-1))

		for i in range(len(self.m2.tex_lookup)):
			self.textureChoose.addItem(str(i) + ": " + TextureTypes[self.m2.textures[self.m2.tex_lookup[i].Id].type] + " " + str(self.m2.textures[self.m2.tex_lookup[i].Id].name))

		for i in range(len(self.m2.trans_lookup)):
			self.transparencyChoose.addItem(str(i) + ": " + str(self.m2.trans_lookup[i].Id))

		for i in range(len(self.m2.uv_anim_lookup)):
			self.uvanimChoose.addItem(str(i) + ": " + str(self.m2.uv_anim_lookup[i].Id))

		for i in range(len(self.m2.renderflags)):
			self.renderflagChoose.addItem(str(i))

		for i in range(len(self.m2.tex_units)):
			self.texunitChoose.addItem(str(i) + ": " + str(self.m2.tex_units[i].Id))

		self.changeEdit()
		

		


	def changeEdit(self):
		self.saveOld()
		self.lastchoice = self.chooseBox.currentIndex()
		tu = self.skin.texunit[self.chooseBox.currentIndex()]
		if tu.flags & 0x10:
			self.checkBox.setCheckState(0)
		else:
			self.checkBox.setCheckState(2)
		self.submeshChoose.setCurrentIndex(tu.submesh)
		self.colorChoose.setCurrentIndex(tu.color + 1)
		self.textureChoose.setCurrentIndex(tu.texture)
		self.transparencyChoose.setCurrentIndex(tu.transparency)
		self.uvanimChoose.setCurrentIndex(tu.animation)
		self.renderflagChoose.setCurrentIndex(tu.renderflag)
		self.texunitChoose.setCurrentIndex(tu.texunit)

		self.modeEdit.setText(str(tu.mode))
		self.shadingEdit.setText(str(tu.shading))

	def saveOld(self):
		if self.lastchoice == -1:
			return

		tu = self.skin.texunit[self.lastchoice]

		if self.checkBox.checkState() == 0:
			tu.flags = 0x10
		else:
			tu.flags = 0

		tu.submesh = self.submeshChoose.currentIndex()
		tu.submesh2 = self.submeshChoose.currentIndex()
		tu.color = self.colorChoose.currentIndex()-1
		tu.texture = self.textureChoose.currentIndex()
		tu.transparency = self.transparencyChoose.currentIndex()
		tu.animation = self.uvanimChoose.currentIndex()
		tu.renderflag = self.renderflagChoose.currentIndex()
		tu.texunit = self.texunitChoose.currentIndex()
		tu.texunit2 = self.texunitChoose.currentIndex()
		
		tu.mode = int(self.modeEdit.text())
		tu.shading = int(self.shadingEdit.text())

		self.skin.texunit[self.lastchoice] = tu

	def addMaterial(self):
		tu = skin.Material()
		self.skin.texunit.append(tu)		
		self.chooseBox.addItem(str(self.skin.header.TextureUnits.count))
		self.skin.header.TextureUnits.count +=1

