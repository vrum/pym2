# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from animeditor import AnimEditor
from animcoloreditor import AnimColorEditor
import m2
from stuff import *


class ParticleEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
		self.last = -1
		
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(644, 590)
		
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(280, 540, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		
		self.chooseBox = QtGui.QComboBox(Dialog)
		self.chooseBox.setGeometry(QtCore.QRect(20, 20, 85, 27))
		self.chooseBox.setObjectName("chooseBox")
		self.connect(self.chooseBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeEdit) 
		

		self.addIcon = QtGui.QIcon("Icons/edit-add.png")
		self.addButton = QtGui.QPushButton(self.addIcon,"Add",Dialog)
		self.addButton.setGeometry(QtCore.QRect(110, 20, 92, 28))
		self.addButton.setObjectName("addButton")
		self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addParticle) 
		
		self.line = QtGui.QFrame(Dialog)
		self.line.setGeometry(QtCore.QRect(20, 60, 241, 16))
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")
		
		self.modelEdit = QtGui.QLineEdit(Dialog)
		self.modelEdit.setGeometry(QtCore.QRect(10, 100, 113, 26))
		self.modelEdit.setObjectName("modelEdit")
		
		self.particleEdit = QtGui.QLineEdit(Dialog)
		self.particleEdit.setGeometry(QtCore.QRect(10, 160, 113, 26))
		self.particleEdit.setObjectName("particleEdit")
		
		self.eSpeedButton = QtGui.QPushButton(Dialog)
		self.eSpeedButton.setGeometry(QtCore.QRect(231, 90, 111, 28))
		self.eSpeedButton.setObjectName("eSpeedButton")
		self.connect(self.eSpeedButton, QtCore.SIGNAL("clicked()"), self.editEmissionSpeed)
		
		self.speedVarButton = QtGui.QPushButton(Dialog)
		self.speedVarButton.setGeometry(QtCore.QRect(350, 90, 121, 28))
		self.speedVarButton.setObjectName("speedVarButton")
		self.connect(self.speedVarButton, QtCore.SIGNAL("clicked()"), self.editSpeedVariation)
		
		self.vertRangeButton = QtGui.QPushButton(Dialog)
		self.vertRangeButton.setGeometry(QtCore.QRect(231, 120, 111, 28))
		self.vertRangeButton.setObjectName("vertRangeButton")
		self.connect(self.vertRangeButton, QtCore.SIGNAL("clicked()"), self.editVerticalRange)
		
		self.horRangeButton = QtGui.QPushButton(Dialog)
		self.horRangeButton.setGeometry(QtCore.QRect(350, 120, 121, 28))
		self.horRangeButton.setObjectName("horRangeButton")
		self.connect(self.horRangeButton, QtCore.SIGNAL("clicked()"), self.editEmissionSpeed)
		
		self.gravButton = QtGui.QPushButton(Dialog)
		self.gravButton.setGeometry(QtCore.QRect(231, 150, 111, 28))
		self.gravButton.setObjectName("gravButton")
		self.connect(self.gravButton, QtCore.SIGNAL("clicked()"), self.editGravity)
		
		self.lifeButton = QtGui.QPushButton(Dialog)
		self.lifeButton.setGeometry(QtCore.QRect(350, 150, 121, 28))
		self.lifeButton.setObjectName("lifeButton")
		self.connect(self.lifeButton, QtCore.SIGNAL("clicked()"), self.editLifespan)
		
		self.eRateButton = QtGui.QPushButton(Dialog)
		self.eRateButton.setGeometry(QtCore.QRect(231, 180, 111, 28))
		self.eRateButton.setObjectName("eRateButton")
		self.connect(self.eRateButton, QtCore.SIGNAL("clicked()"), self.editEmissionRate)
		
		self.grav2Button = QtGui.QPushButton(Dialog)
		self.grav2Button.setGeometry(QtCore.QRect(350, 180, 121, 28))
		self.grav2Button.setObjectName("grav2Button")
		self.connect(self.grav2Button, QtCore.SIGNAL("clicked()"), self.editStrongGravity)
		
		self.eLengthButton = QtGui.QPushButton(Dialog)
		self.eLengthButton.setGeometry(QtCore.QRect(231, 210, 111, 28))
		self.eLengthButton.setObjectName("eLengthButton")
		self.connect(self.eLengthButton, QtCore.SIGNAL("clicked()"), self.editAreaLength)
		
		self.eWidthButton = QtGui.QPushButton(Dialog)
		self.eWidthButton.setGeometry(QtCore.QRect(350, 210, 121, 28))
		self.eWidthButton.setObjectName("eWidthButton")
		self.connect(self.eWidthButton, QtCore.SIGNAL("clicked()"), self.editAreaWidth)
		
		self.fColorButton = QtGui.QPushButton(Dialog)
		self.fColorButton.setGeometry(QtCore.QRect(230, 290, 92, 28))
		self.fColorButton.setObjectName("fColorButton")
		
		self.fOpacityButton = QtGui.QPushButton(Dialog)
		self.fOpacityButton.setGeometry(QtCore.QRect(330, 290, 92, 28))
		self.fOpacityButton.setObjectName("fOpacityButton")
		
		self.fIntensityButton = QtGui.QPushButton(Dialog)
		self.fIntensityButton.setGeometry(QtCore.QRect(230, 320, 92, 28))
		self.fIntensityButton.setObjectName("fIntensityButton")
		
		self.fUnkButton = QtGui.QPushButton(Dialog)
		self.fUnkButton.setGeometry(QtCore.QRect(330, 320, 92, 28))
		self.fUnkButton.setObjectName("fUnkButton")
		
		self.fSizeButton = QtGui.QPushButton(Dialog)
		self.fSizeButton.setGeometry(QtCore.QRect(430, 290, 92, 28))
		self.fSizeButton.setObjectName("fSizeButton")
		
		self.textureBox = QtGui.QComboBox(Dialog)
		self.textureBox.setGeometry(QtCore.QRect(10, 200, 85, 27))
		self.textureBox.setObjectName("textureBox")
		
		self.xEdit = QtGui.QLineEdit(Dialog)
		self.xEdit.setGeometry(QtCore.QRect(10, 260, 31, 26))
		self.xEdit.setObjectName("xEdit")
		
		self.yEdit = QtGui.QLineEdit(Dialog)
		self.yEdit.setGeometry(QtCore.QRect(50, 260, 31, 26))
		self.yEdit.setObjectName("yEdit")
		
		self.zEdit = QtGui.QLineEdit(Dialog)
		self.zEdit.setGeometry(QtCore.QRect(90, 260, 31, 26))
		self.zEdit.setObjectName("zEdit")
		
		self.boneBox = QtGui.QComboBox(Dialog)
		self.boneBox.setGeometry(QtCore.QRect(120, 200, 85, 27))
		self.boneBox.setObjectName("boneBox")
		
		self.typeBox = QtGui.QComboBox(Dialog)
		self.typeBox.setGeometry(QtCore.QRect(130, 260, 85, 27))
		self.typeBox.setObjectName("typeBox")
		self.typeBox.addItem("")
		self.typeBox.addItem("")
		self.typeBox.addItem("")
		
		self.htBox = QtGui.QComboBox(Dialog)
		self.htBox.setGeometry(QtCore.QRect(10, 300, 85, 27))
		self.htBox.setObjectName("htBox")
		self.htBox.addItem("")
		self.htBox.addItem("")
		self.htBox.addItem("")
		
		self.particleColorBox = QtGui.QComboBox(Dialog)
		self.particleColorBox.setGeometry(QtCore.QRect(110, 300, 85, 27))
		self.particleColorBox.setObjectName("particleColorBox")
		self.particleColorBox.addItem("")
		self.particleColorBox.addItem("")
		self.particleColorBox.addItem("")
		self.particleColorBox.addItem("")
		
		self.mFileLabel = QtGui.QLabel(Dialog)
		self.mFileLabel.setGeometry(QtCore.QRect(10, 80, 111, 18))
		self.mFileLabel.setObjectName("mFileLabel")
		
		self.pFileLabel = QtGui.QLabel(Dialog)
		self.pFileLabel.setGeometry(QtCore.QRect(10, 140, 131, 18))
		self.pFileLabel.setObjectName("pFileLabel")
		
		self.posLabel = QtGui.QLabel(Dialog)
		self.posLabel.setGeometry(QtCore.QRect(10, 240, 81, 18))
		self.posLabel.setObjectName("posLabel")

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
		self.eSpeedButton.setText(QtGui.QApplication.translate("Dialog", "EmissionSpeed", None, QtGui.QApplication.UnicodeUTF8))
		self.speedVarButton.setText(QtGui.QApplication.translate("Dialog", "SpeedVariation", None, QtGui.QApplication.UnicodeUTF8))
		self.vertRangeButton.setText(QtGui.QApplication.translate("Dialog", "Vertical Range", None, QtGui.QApplication.UnicodeUTF8))
		self.horRangeButton.setText(QtGui.QApplication.translate("Dialog", "Horizontal Range", None, QtGui.QApplication.UnicodeUTF8))
		self.gravButton.setText(QtGui.QApplication.translate("Dialog", "Gravity", None, QtGui.QApplication.UnicodeUTF8))
		self.lifeButton.setText(QtGui.QApplication.translate("Dialog", "Lifespan", None, QtGui.QApplication.UnicodeUTF8))
		self.eRateButton.setText(QtGui.QApplication.translate("Dialog", "EmissionRate", None, QtGui.QApplication.UnicodeUTF8))
		self.grav2Button.setText(QtGui.QApplication.translate("Dialog", "Strong Gravity", None, QtGui.QApplication.UnicodeUTF8))
		self.eLengthButton.setText(QtGui.QApplication.translate("Dialog", "Area Length", None, QtGui.QApplication.UnicodeUTF8))
		self.eWidthButton.setText(QtGui.QApplication.translate("Dialog", "Area Width", None, QtGui.QApplication.UnicodeUTF8))
		self.fColorButton.setText(QtGui.QApplication.translate("Dialog", "Color", None, QtGui.QApplication.UnicodeUTF8))
		self.fOpacityButton.setText(QtGui.QApplication.translate("Dialog", "Opacity", None, QtGui.QApplication.UnicodeUTF8))
		self.fIntensityButton.setText(QtGui.QApplication.translate("Dialog", "Intensity", None, QtGui.QApplication.UnicodeUTF8))
		self.fUnkButton.setText(QtGui.QApplication.translate("Dialog", "Unknown", None, QtGui.QApplication.UnicodeUTF8))
		self.fSizeButton.setText(QtGui.QApplication.translate("Dialog", "Size", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Plane", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Sphere", None, QtGui.QApplication.UnicodeUTF8))
		self.typeBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Spline (exists?)", None, QtGui.QApplication.UnicodeUTF8))
		self.htBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Head", None, QtGui.QApplication.UnicodeUTF8))
		self.htBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Tail", None, QtGui.QApplication.UnicodeUTF8))
		self.htBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Both", None, QtGui.QApplication.UnicodeUTF8))
		self.particleColorBox.setItemText(0, QtGui.QApplication.translate("Dialog", "None", None, QtGui.QApplication.UnicodeUTF8))
		self.particleColorBox.setItemText(1, QtGui.QApplication.translate("Dialog", "One (11)", None, QtGui.QApplication.UnicodeUTF8))
		self.particleColorBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Two (12)", None, QtGui.QApplication.UnicodeUTF8))
		self.particleColorBox.setItemText(3, QtGui.QApplication.translate("Dialog", "Three (13)", None, QtGui.QApplication.UnicodeUTF8))
		self.mFileLabel.setText(QtGui.QApplication.translate("Dialog", "ModelFileName:", None, QtGui.QApplication.UnicodeUTF8))
		self.pFileLabel.setText(QtGui.QApplication.translate("Dialog", "ParticleFileName:", None, QtGui.QApplication.UnicodeUTF8))
		self.posLabel.setText(QtGui.QApplication.translate("Dialog", "Position:", None, QtGui.QApplication.UnicodeUTF8))



	def finalizeMe(self):
		self.saveOld()
		self.accept()

	def setCurrentEditing(self,i):
		self.chooseBox.setCurrentIndex(i)
		self.changeEdit()

	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		for i in range(len(self.m2.particle_emitters)):
			self.chooseBox.addItem(str(i))

		for i in range(len(self.m2.textures)):
			self.textureBox.addItem(str(i) + ": " + TextureTypes[self.m2.textures[i].type] + " " + str(self.m2.textures[i].name))
			
		for i in range(len(self.m2.bones)+1):
			if i == 0:
				self.boneBox.addItem("None "+str(i-1))
			else:
				self.boneBox.addItem("Bone: "+str(i-1)+" "+KeyBoneTypes[self.m2.bones[i-1].KeyBoneId])
				
		self.changeEdit()
		
		
	def addParticle(self,parbone = 0):
		l = m2.Particle()
		l.bone = parbone
		l.emission_speed.type = m2.DATA_FLOAT
		l.speed_var.type = m2.DATA_FLOAT
		l.vert_range.type = m2.DATA_FLOAT
		l.hor_range.type = m2.DATA_FLOAT
		l.gravity.type = m2.DATA_FLOAT
		l.lifespan.type = m2.DATA_FLOAT
		l.emission_rate.type = m2.DATA_FLOAT
		l.emission_area_len.type = m2.DATA_FLOAT
		l.emission_area_width.type = m2.DATA_FLOAT
		l.gravity2.type = m2.DATA_FLOAT

		self.m2.particle_emitters.append(l)
		
		self.chooseBox.addItem(str(self.m2.hdr.particle_emitters.count))
		self.m2.hdr.particle_emitters.count += 1

	def saveOld(self):
		if (self.last == -1):
			return	
			
		p = self.m2.particle_emitters[self.last]
		p.Pos.x = float(self.xEdit.text())
		p.Pos.y = float(self.yEdit.text())
		p.Pos.z = float(self.zEdit.text())
		
		
		name = str(self.modelEdit.text())
		p.ModelName = makeZeroTerminated(name)
		p.lenModel = len(p.ModelName)
		
		name = str(self.particleEdit.text())
		p.ParticleName =makeZeroTerminated(name)
		p.lenParticle = len(p.ParticleName)
		
		p.bone = self.boneBox.currentIndex()-1
		p.texture = self.textureBox.currentIndex()
		cdbc = self.particleColorBox.currentIndex()
		p.color_dbc = cdbc if (cdbc == 0) else cdbc+10
		p.head_or_tail = self.htBox.currentIndex()
		p.particletype = self.typeBox.currentIndex()
		
		self.m2.particle_emitters[self.last] = p
			
			
	def changeEdit(self):
		self.saveOld()
		self.last = self.chooseBox.currentIndex()
		p = self.m2.particle_emitters[self.last]
		self.boneBox.setCurrentIndex(p.bone+1)
		self.textureBox.setCurrentIndex(p.texture)
		self.particleColorBox.setCurrentIndex(p.color_dbc-10 if( p.color_dbc in (11,12,13)) else 0)
		self.htBox.setCurrentIndex(p.head_or_tail)
		self.typeBox.setCurrentIndex(p.particletype)
		
		self.xEdit.setText(str(p.Pos.x))
		self.yEdit.setText(str(p.Pos.y))
		self.zEdit.setText(str(p.Pos.z))
		
		self.modelEdit.setText(p.ModelName)
		self.particleEdit.setText(p.ParticleName)
		
	

	def editEmissionSpeed(self):		
		temp = self.chooseBox.currentIndex()
		self.eSpeedEditor = AnimEditor()
		self.eSpeedEditor.setAnimBlock(self.m2.particle_emitters[temp].emission_speed,self.m2.gSequ)
		self.eSpeedEditor.show()
		self.connect(self.eSpeedEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setEmissionSpeed)

	def setEmissionSpeed(self):
		self.m2.particle_emitters[self.chooseBox.currentIndex()].emission_speed = self.eSpeedEditor.getAnimBlock()
		
	

	def editSpeedVariation(self):		
		temp = self.chooseBox.currentIndex()
		self.eSpeedVarEditor = AnimEditor()
		self.eSpeedVarEditor.setAnimBlock(self.m2.particle_emitters[temp].speed_var,self.m2.gSequ)
		self.eSpeedVarEditor.show()
		self.connect(self.eSpeedVarEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setSpeedVariation)

	def setSpeedVariation(self):
		self.m2.particle_emitters[self.chooseBox.currentIndex()].speed_var = self.eSpeedVarEditor.getAnimBlock()
		
	

	def editVerticalRange(self):		
		temp = self.chooseBox.currentIndex()
		self.VertRangeEditor = AnimEditor()
		self.VertRangeEditor.setAnimBlock(self.m2.particle_emitters[temp].vert_range,self.m2.gSequ)
		self.VertRangeEditor.show()
		self.connect(self.VertRangeEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setVerticalRange)

	def setVerticalRange(self):
		self.m2.particle_emitters[self.chooseBox.currentIndex()].vert_range = self.VertRangeEditor.getAnimBlock()
		
	

	def editHorizontalRange(self):		
		temp = self.chooseBox.currentIndex()
		self.HorRangeEditor = AnimEditor()
		self.HorRangeEditor.setAnimBlock(self.m2.particle_emitters[temp].hor_range,self.m2.gSequ)
		self.HorRangeEditor.show()
		self.connect(self.HorRangeEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setHorizontalRange)

	def setHorizontalRange(self):
		self.m2.particle_emitters[self.chooseBox.currentIndex()].hor_range = self.HorRangeEditor.getAnimBlock()
		
	

	def editGravity(self):		
		temp = self.chooseBox.currentIndex()
		self.GravEditor = AnimEditor()
		self.GravEditor.setAnimBlock(self.m2.particle_emitters[temp].gravity,self.m2.gSequ)
		self.GravEditor.show()
		self.connect(self.GravEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setGravity)

	def setGravity(self):
		self.m2.particle_emitters[self.chooseBox.currentIndex()].gravity = self.GravEditor.getAnimBlock()
		
	

	def editLifespan(self):		
		temp = self.chooseBox.currentIndex()
		self.lifespanEditor = AnimEditor()
		self.lifespanEditor.setAnimBlock(self.m2.particle_emitters[temp].lifespan,self.m2.gSequ)
		self.lifespanEditor.show()
		self.connect(self.lifespanEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setLifespan)

	def setLifespan(self):
		self.m2.particle_emitters[self.chooseBox.currentIndex()].lifespan = self.lifespanEditor.getAnimBlock()
		
	

	def editEmissionRate(self):		
		temp = self.chooseBox.currentIndex()
		self.eRateEditor = AnimEditor()
		self.eRateEditor.setAnimBlock(self.m2.particle_emitters[temp].emission_rate,self.m2.gSequ)
		self.eRateEditor.show()
		self.connect(self.eRateEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setEmissionRate)

	def setEmissionRate(self):
		self.m2.particle_emitters[self.chooseBox.currentIndex()].emission_rate = self.eRateEditor.getAnimBlock()
		
	

	def editAreaLength(self):		
		temp = self.chooseBox.currentIndex()
		self.eAreaLengthEditor = AnimEditor()
		self.eAreaLengthEditor.setAnimBlock(self.m2.particle_emitters[temp].emission_area_len,self.m2.gSequ)
		self.eAreaLengthEditor.show()
		self.connect(self.eAreaLengthEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setAreaLength)

	def setAreaLength(self):
		self.m2.particle_emitters[self.chooseBox.currentIndex()].emission_area_len = self.eAreaLengthEditor.getAnimBlock()
		
	

	def editAreaWidth(self):		
		temp = self.chooseBox.currentIndex()
		self.eAreaWidthEditor = AnimEditor()
		self.eAreaWidthEditor.setAnimBlock(self.m2.particle_emitters[temp].emission_area_width,self.m2.gSequ)
		self.eAreaWidthEditor.show()
		self.connect(self.eAreaWidthEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setAreaWidth)

	def setAreaWidth(self):
		self.m2.particle_emitters[self.chooseBox.currentIndex()].emission_area_width = self.eAreaWidthEditor.getAnimBlock()
		
	

	def editStrongGravity(self):		
		temp = self.chooseBox.currentIndex()
		self.strongGravEditor = AnimEditor()
		self.strongGravEditor.setAnimBlock(self.m2.particle_emitters[temp].gravity2,self.m2.gSequ)
		self.strongGravEditor.show()
		self.connect(self.strongGravEditor,QtCore.SIGNAL("AnimBlockEdited()"),self.setStrongGravity)

	def setStrongGravity(self):
		self.m2.particle_emitters[self.chooseBox.currentIndex()].gravity2 = self.strongGravEditor.getAnimBlock()
		
		
		

