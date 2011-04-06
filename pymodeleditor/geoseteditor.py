# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui

from glView import *
from stuff import *

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

		self.scaleslider = QtGui.QSlider(Dialog)
		self.scaleslider.setGeometry(QtCore.QRect(450,110,30,250))
		self.scaleslider.setRange(1,500)
		self.scaleslider.setSingleStep(10)
		self.scaleslider.setPageStep(50)
		self.scaleslider.setTickInterval(50)
		self.connect(self.scaleslider,QtCore.SIGNAL("valueChanged(int)"),self.GlView.setScale)

		self.lineEdit = QtGui.QLineEdit(Dialog)
		self.lineEdit.setGeometry(QtCore.QRect(450, 70, 91, 26))
		self.lineEdit.setObjectName("lineEdit")

		self.scaleEdit = QtGui.QLineEdit(Dialog)
		self.scaleEdit.setGeometry(QtCore.QRect(20, 370, 40, 26))
		self.scaleEdit.setObjectName("scaleEdit")
		self.scaleEdit.setText("1.0")
		

		self.scaleIcon = QtGui.QIcon("Icons/edit-scaling.png")
		self.scaleButton = QtGui.QPushButton(self.scaleIcon,"Rescale",self)
		self.scaleButton.setGeometry(QtCore.QRect(80, 370, 122, 27))
		self.scaleButton.setObjectName("scaleButton")
		self.connect(self.scaleButton, QtCore.SIGNAL("clicked()"), self.rescaleGeoset)
		

		self.duplicateIcon = QtGui.QIcon("Icons/edit-add.png")
		self.duplicateButton = QtGui.QPushButton(self.duplicateIcon,"Duplicate Geoset",self)
		self.duplicateButton.setGeometry(QtCore.QRect(200, 370, 122, 27))
		self.duplicateButton.setObjectName("duplicateButton")
		self.connect(self.duplicateButton, QtCore.SIGNAL("clicked()"), self.duplicateGeoset)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)


	def finalizeMe(self):
		self.saveOld()
		self.accept()
		
	def rescaleGeoset(self):
		scale = float(self.scaleEdit.text())
		s = 0	
		rescaled = []
		for i in self.skin.mesh:
			if s == self.comboBox.currentIndex():
				for t in range(i.num_tris/3):
					try:	
						if (self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[0]].Id not in rescaled):					
							v1 = self.m2.vertices[self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[0]].Id]
							v1.pos.x *= scale
							v1.pos.y *= scale
							v1.pos.z *= scale
							rescaled.append(self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[0]].Id)
						
						if (self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[1]].Id not in rescaled):
							v2 = self.m2.vertices[self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[1]].Id]
							v2.pos.x *= scale
							v2.pos.y *= scale
							v2.pos.z *= scale
							rescaled.append(self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[1]].Id)
						if (self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[2]].Id not in rescaled):
							v3 = self.m2.vertices[self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[2]].Id]
							v3.pos.x *= scale
							v3.pos.y *= scale
							v3.pos.z *= scale
							rescaled.append(self.skin.indices[self.skin.tri[i.tri_offset/3+ t].indices[2]].Id)

					except Exception, e:
						print e
						#print "Vertex: " + str(t) + " failed"
			s += 1
		
		self.GlView.setModel(self.m2,self.skin,self.comboBox.currentIndex())

	
	def duplicateGeoset(self):
		mesh = Mesh()
		mesh.mesh_id		= self.skin.mesh[self.comboBox.currentIndex()].mesh_id
		mesh.vert_offset	= self.skin.mesh[self.comboBox.currentIndex()].vert_offset
		mesh.num_verts		= self.skin.mesh[self.comboBox.currentIndex()].num_verts
		mesh.tri_offset		= self.skin.mesh[self.comboBox.currentIndex()].tri_offset
		mesh.num_tris		= self.skin.mesh[self.comboBox.currentIndex()].num_tris
		mesh.num_bones		= self.skin.mesh[self.comboBox.currentIndex()].num_bones
		mesh.start_bone		= self.skin.mesh[self.comboBox.currentIndex()].start_bone
		mesh.unknown		= self.skin.mesh[self.comboBox.currentIndex()].unknown
		mesh.rootbone		= self.skin.mesh[self.comboBox.currentIndex()].rootbone
		mesh.bound		= self.skin.mesh[self.comboBox.currentIndex()].bound
		self.skin.mesh.append(mesh)
		for i in self.skin.texunit:
			if (i.submesh == self.comboBox.currentIndex()):
				mat = Material()
				mat.flags         = i.flags
				mat.shading	   = i.shading
				mat.submesh       = self.skin.header.Submeshes.count
				mat.submesh2      = self.skin.header.Submeshes.count
				mat.color         = i.color
				mat.renderflag    = i.renderflag
				mat.texunit 	  = i.texunit
				mat.mode          = i.mode
				mat.texture       = i.texture
				mat.texunit2      = i.texunit2
				mat.transparency  = i.transparency
				mat.animation      = i.animation
				self.skin.texunit.append(mat)
				self.skin.header.TextureUnits.count += 1
		self.comboBox.addItem(str(self.skin.header.Submeshes.count)+": "+GeosetName(self.skin.mesh[self.skin.header.Submeshes.count].mesh_id))		
		self.skin.header.Submeshes.count += 1
			
				
	
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

