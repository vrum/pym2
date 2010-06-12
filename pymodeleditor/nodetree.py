# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui
from attachmenteditor import *
from boneeditor import *

KeyBoneTypes = { 0 :"ArmL", 1: "ArmR", 2 :"ShoulderL", 3 :"ShoulderR", 4: "SpineLow", 5: "Waist", 6: "Head", 7 :"Jaw", 8: "IndexFingerR", 9: "MiddleFingerR", 10: "PinkyFingerR", 11:"RingFingerR", 12 :"ThumbR", 13 :"IndexFingerL", 14 :"MiddleFingerL", 15 :"PinkyFingerL", 16: "RingFingerL", 17: "ThumbL", 18: "$BTH", 19: "$CSR", 20: "$CSL", 21: "_Breath", 22 :"_Name", 23 :"_NameMount", 24 :"$CHD", 25 :"$CCH", 26 :"Root", 27 :"Wheel1", 28 :"Wheel2", 29 :"Wheel3", 30 :"Wheel4", 31 :"Wheel5", 32: "Wheel6", 33: "Wheel7", 34: "Wheel8" }

attachment_types = { 0:"Mountpoint/Left Wrist", 1:"Right Palm", 2:"Left Palm", 3:"Right Elbow", 4:"Left Elbow", 5:"Right Shoulder", 6:"Left Shoulder",
7:"Right Knee", 8:"Left Knee", 9:"Unk1",10:"Unk2",11:"Helmet",12:"Back",13:"Unk3",14:"Unk4",15:"Bust1",16:"Bust2",17:"Breath",18:"Name",19:"Ground",
20:"Top of Head",21:"Left Palm 2", 22:"Right Palm 2",23:"Unk5",24:"Unk6",25:"Unk7",26:"Right Back Sheath",27:"Left Back Sheath",28:"Middle Back Sheath",
29:"Belly",30:"Left Back",31:"Right Back",32:"Left Hip Sheath",33:"Right Hip Sheath",34:"Bust3",35:"Right Palm 3",36:"Unk8",37:"demolishervehicle1",
38:"demolishervehicle2",39:"vehicle seat 1",40:"vehicle seat 2",41:"vehicle seat 3",42:"vehicle seat 4",43:"Unk9",44:"Unk10",45:"Unk11",46:"Unk12",
47:"Unk13",48:"Unk14",49:"Unk15"}

class Node(QtGui.QTreeWidgetItem):
	def setId(self,i):
		self.Id = i
	def setNodeType(self,i):
		self.NodeType = i
	
class BoneView(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(522, 405)
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(180, 370, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")

		self.treeWidget = QtGui.QTreeWidget(Dialog)
		self.treeWidget.setGeometry(QtCore.QRect(10, 10, 501, 351))
		self.treeWidget.setObjectName("treeWidget")
		self.treeWidget.headerItem().setText(0, "Bones")
		self.connect(self.treeWidget, QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*, int)"), self.editNode)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Node Editor", None, QtGui.QApplication.UnicodeUTF8))


	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		self.updateTree()

	def updateTree(self):
		self.treeWidget.clear()
		c = 0
		for i in (self.m2.bones):
       			icon = QtGui.QIcon()
        		icon.addPixmap(QtGui.QPixmap("Icons/edit-Bone.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
			if i.parent == -1:
				item = Node(self.treeWidget)
				item.setId(c)
			else:
				j = -1
				for n in range(self.treeWidget.topLevelItemCount()):
					j = iterateThroughChildren(self.treeWidget.topLevelItem(n),i.parent) 
					if j != -1:
						item = Node(j)				
						item.setId(c)
						break
				if j == -1:
					print ("Unable to find parent of Bone " + str(c) +" which is: " + str(i.parent))
					item = Node(self.treeWidget)				
					item.setId(c)
			if i.KeyBoneId != -1:
				item.setText(0,"Bone: "+str(item.Id)+" "+KeyBoneTypes[i.KeyBoneId])
			else:
				item.setText(0,"Bone "+str(item.Id))
			item.setIcon(0, icon)
			item.setNodeType("Bone")
			c += 1
		c = 0
		for i in (self.m2.attachments):
       			icon = QtGui.QIcon()
        		icon.addPixmap(QtGui.QPixmap("Icons/edit-attachment.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
			if i.bone == -1:
				item = Node(self.treeWidget)
				item.setId(c)
			else:
				for n in range(self.treeWidget.topLevelItemCount()):
					j = iterateThroughChildren(self.treeWidget.topLevelItem(n),i.bone) 
					if j != -1:
						item = Node(j)				
						item.setId(c)
						break
				if j == -1:
					print ("Unable to find bone of Attachment " + str(c) +" which is: " + str(i.bone))
					item = Node(self.treeWidget)				
					item.setId(c)
			item.setText(0,"Attachment: "+str(item.Id)+" "+attachment_types[i.Id])
			item.setIcon(0, icon)
			item.setNodeType("Attachment")
			c += 1
		c = 0
		for i in (self.m2.events):
       			icon = QtGui.QIcon()
        		icon.addPixmap(QtGui.QPixmap("Icons/edit-event.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
			if i.Bone == -1:
				item = Node(self.treeWidget)
				item.setId(c)
			else:
				for n in range(self.treeWidget.topLevelItemCount()):
					j = iterateThroughChildren(self.treeWidget.topLevelItem(n),i.Bone) 
					if j != -1:
						item = Node(j)				
						item.setId(c)
						break
				if j == -1:
					print ("Unable to find bone of Event " + str(c) +" which is: " + str(i.Bone))
					item = Node(self.treeWidget)				
					item.setId(c)
			item.setText(0,"Event: "+str(item.Id)+" "+str(i.Id))
			item.setIcon(0, icon)
			item.setNodeType("Event")
			c += 1
		c = 0
		for i in (self.m2.lights):
       			icon = QtGui.QIcon()
        		icon.addPixmap(QtGui.QPixmap("Icons/edit-light.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
			if i.Bone == -1:
				item = Node(self.treeWidget)
				item.setId(c)
			else:
				for n in range(self.treeWidget.topLevelItemCount()):
					j = iterateThroughChildren(self.treeWidget.topLevelItem(n),i.Bone) 
					if j != -1:
						item = Node(j)				
						item.setId(c)
						break
				if j == -1:
					print ("Unable to find bone of Light " + str(c) +" which is: " + str(i.Bone))
					item = Node(self.treeWidget)				
					item.setId(c)
			item.setText(0,"Light: "+str(c))
			item.setIcon(0, icon)
			item.setNodeType("Light")
			c += 1
		c = 0
		for i in (self.m2.particle_emitters):
       			icon = QtGui.QIcon()
        		icon.addPixmap(QtGui.QPixmap("Icons/edit-particles.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
			if i.bone == -1:
				item = Node(self.treeWidget)
				item.setId(c)
			else:
				for n in range(self.treeWidget.topLevelItemCount()):
					j = iterateThroughChildren(self.treeWidget.topLevelItem(n),i.bone) 
					if j != -1:
						item = Node(j)				
						item.setId(c)
						break
				if j == -1:
					print ("Unable to find bone of Particle " + str(c) +" which is: " + str(i.bone))
					item = Node(self.treeWidget)				
					item.setId(c)
			item.setText(0,"Particle: "+str(c))
			item.setIcon(0, icon)
			item.setNodeType("Particle")
			c += 1
		c = 0
		for i in (self.m2.ribbon_emitters):
       			icon = QtGui.QIcon()
        		icon.addPixmap(QtGui.QPixmap("Icons/edit-ribbons.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
			if i.Bone == -1:
				item = Node(self.treeWidget)
				item.setId(c)
			else:
				for n in range(self.treeWidget.topLevelItemCount()):
					j = iterateThroughChildren(self.treeWidget.topLevelItem(n),i.Bone) 
					if j != -1:
						item = Node(j)				
						item.setId(c)
						break
				if j == -1:
					print ("Unable to find bone of Ribbon " + str(c) +" which is: " + str(i.Bone))
					item = Node(self.treeWidget)				
					item.setId(c)
			item.setText(0,"Ribbon: "+str(c))
			item.setIcon(0, icon)
			item.setNodeType("Ribbon")
			c += 1

	def editNode(self):
		if self.treeWidget.currentItem().NodeType == "Bone":
			self.editBones()
		elif self.treeWidget.currentItem().NodeType == "Attachment":
			self.editAttachments()

	def editAttachments(self):
		self.attEditor = AttachmentEditor()
		self.attEditor.setModel(self.m2,self.skin)
		self.attEditor.show()
		self.attEditor.setCurrentEditing(self.treeWidget.currentItem().Id)
		QtCore.QObject.connect(self.attEditor, QtCore.SIGNAL("accepted()"), self.setAttachments)

	def setAttachments(self):
		self.m2 = self.attEditor.m2
		self.updateTree()

	def editBones(self):
		self.boneEditor = BoneEditor()
		self.boneEditor.setModel(self.m2,self.skin)
		self.boneEditor.show()
		self.boneEditor.setCurrentEditing(self.treeWidget.currentItem().Id)
		QtCore.QObject.connect(self.boneEditor, QtCore.SIGNAL("accepted()"), self.setBones)

	def setBones(self):
		self.m2 = self.boneEditor.m2
		self.updateTree()
		
def iterateThroughChildren(item,Id):
	if item.NodeType != "Bone":	
		return -1
	if item.Id == Id:
		return item
	for i in range(item.childCount()):
		if item.child(i).Id == Id:
			return item.child(i)
		j = iterateThroughChildren(item.child(i),Id)
		if j != -1:
			return j
	return -1
	
