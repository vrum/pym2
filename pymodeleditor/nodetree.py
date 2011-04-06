# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui
from attachmenteditor import *
from boneeditor import *
from lighteditor import *
from particleeditor import *
from stuff import *

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
		elif self.treeWidget.currentItem().NodeType == "Light":
			self.editLights()
		elif self.treeWidget.currentItem().NodeType == "Particle":
			self.editParticles()

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

	def editLights(self):
		self.lightEditor = LightEditor()
		self.lightEditor.setModel(self.m2,self.skin)
		self.lightEditor.show()
		self.lightEditor.setCurrentEditing(self.treeWidget.currentItem().Id)
		QtCore.QObject.connect(self.lightEditor, QtCore.SIGNAL("accepted()"), self.setLights)

	def setLights(self):
		self.m2 = self.lightEditor.m2
		self.updateTree()

	def editParticles(self):
		self.particleEditor = ParticleEditor()
		self.particleEditor.setModel(self.m2,self.skin)
		self.particleEditor.show()
		self.particleEditor.setCurrentEditing(self.treeWidget.currentItem().Id)
		QtCore.QObject.connect(self.particleEditor, QtCore.SIGNAL("accepted()"), self.setParticles)

	def setParticles(self):
		self.m2 = self.particleEditor.m2
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
	
