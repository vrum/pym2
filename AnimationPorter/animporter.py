#! /usr/bin/python

# -*- coding: utf-8 -*-

import sys 
from PyQt4 import QtCore, QtGui
from m2 import *
from skin import *
from animdbc import *

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

class AnimPorter(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(700, 650)
		self.treeM1 = QtGui.QTreeWidget(Form)
		self.treeM1.setGeometry(QtCore.QRect(10, 70, 320, 281))
		self.treeM1.setObjectName("treeM1")
		self.treeM1.headerItem().setText(0, "Bones")

		self.treeM2 = QtGui.QTreeWidget(Form)
		self.treeM2.setGeometry(QtCore.QRect(350, 70, 320, 281))
		self.treeM2.setObjectName("treeM2")
		self.treeM2.headerItem().setText(0, "Bones")

		self.animsm1Box = QtGui.QComboBox(Form)
		self.animsm1Box.setGeometry(QtCore.QRect(10, 40, 85, 27))
		self.animsm1Box.setObjectName("animsm1Box")

		self.animsm2Box = QtGui.QComboBox(Form)
		self.animsm2Box.setGeometry(QtCore.QRect(350, 40, 85, 27))
		self.animsm2Box.setObjectName("animsm2Box")

		self.openm1Button = QtGui.QPushButton(Form)
		self.openm1Button.setGeometry(QtCore.QRect(10, 10, 121, 28))
		self.openm1Button.setObjectName("openm1Button")
		self.connect(self.openm1Button, QtCore.SIGNAL("clicked()"), self.openModel1)

		self.savem1Button = QtGui.QPushButton(Form)
		self.savem1Button.setGeometry(QtCore.QRect(150, 10, 121, 28))
		self.savem1Button.setObjectName("savem1Button")
		self.connect(self.savem1Button, QtCore.SIGNAL("clicked()"), self.saveModel1)

		self.openm2Button = QtGui.QPushButton(Form)
		self.openm2Button.setGeometry(QtCore.QRect(350, 10, 121, 28))
		self.openm2Button.setObjectName("openm2Button")
		self.connect(self.openm2Button, QtCore.SIGNAL("clicked()"), self.openModel2)

		self.bonesM1 = QtGui.QTextEdit(Form)
		self.bonesM1.setGeometry(QtCore.QRect(10, 370, 320, 111))
		self.bonesM1.setObjectName("bonesM1")

		self.bonesM2 = QtGui.QTextEdit(Form)
		self.bonesM2.setGeometry(QtCore.QRect(350, 370, 320, 111))
		self.bonesM2.setObjectName("bonesM2")

		self.singleM1 = QtGui.QTextEdit(Form)
		self.singleM1.setGeometry(QtCore.QRect(10, 490, 320, 80))
		self.singleM1.setObjectName("singleM1")

		self.singleM2 = QtGui.QTextEdit(Form)
		self.singleM2.setGeometry(QtCore.QRect(350, 490, 320, 80))
		self.singleM2.setObjectName("singleM2")

		self.portselectedButton = QtGui.QPushButton(Form)
		self.portselectedButton.setGeometry(QtCore.QRect(10, 580, 181, 28))
		self.portselectedButton.setObjectName("portselectedButton")
		self.connect(self.portselectedButton, QtCore.SIGNAL("clicked()"), self.portSelected)

		self.portallButton = QtGui.QPushButton(Form)
		self.portallButton.setGeometry(QtCore.QRect(210, 580, 181, 28))
		self.portallButton.setObjectName("portallButton")
		self.connect(self.portallButton, QtCore.SIGNAL("clicked()"), self.portAll)

		self.pushButton = QtGui.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(420, 580, 181, 28))
		self.pushButton.setObjectName("pushButton")
		self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.addAnim)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "Animation Porter", None, QtGui.QApplication.UnicodeUTF8))
		self.openm1Button.setText(QtGui.QApplication.translate("Form", "Open Model1", None, QtGui.QApplication.UnicodeUTF8))
		self.savem1Button.setText(QtGui.QApplication.translate("Form", "Save Model1", None, QtGui.QApplication.UnicodeUTF8))
		self.openm2Button.setText(QtGui.QApplication.translate("Form", "Open Model2", None, QtGui.QApplication.UnicodeUTF8))
		self.portselectedButton.setText(QtGui.QApplication.translate("Form", "Port Selected Animation", None, QtGui.QApplication.UnicodeUTF8))
		self.portallButton.setText(QtGui.QApplication.translate("Form", "Port All Animations", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton.setText(QtGui.QApplication.translate("Form", "Add Animation", None, QtGui.QApplication.UnicodeUTF8))


	def openModel1(self):
		openname = QtGui.QFileDialog().getOpenFileName(self,"Open File",QtCore.QDir.currentPath())
		self.m1 = M2File(openname)
		skinname = openname[0:len(openname)-3]+"00.skin"
		self.skin = SkinFile(skinname)
		self.updateTree(self.m1,self.treeM1)
		self.updateAnimBox(self.m1,self.animsm1Box)


	def saveModel1(self):
		savename = QtGui.QFileDialog().getSaveFileName(self,"Save File",QtCore.QDir.currentPath())
		self.m1.write(savename)
		skinname = savename[0:len(savename)-3]+"00.skin"
		self.skin.write(skinname)

	def openModel2(self):
		openname = QtGui.QFileDialog().getOpenFileName(self,"Open File",QtCore.QDir.currentPath())
		self.m2 = M2File(openname)
		self.updateTree(self.m2,self.treeM2)
		self.updateAnimBox(self.m2,self.animsm2Box)

	def getBones(self):
		t= self.bonesM1.toPlainText().split("\n")
		bone = []
		for i in t:
			if (i!=""):
				g = int(i)
				bone.append(g)

		
		t= self.bonesM2.toPlainText().split("\n")
		btwo = []
		for i in t:
			if (i!=""):
				g = int(i)
				btwo.append(g)

		###fix this!!####
		#if len(bone) != len(btwo):
		#	if len(bone) > len(btwo):
				

		return (bone,btwo)
		
	def getSingleBones(self):
		t= self.singleM1.toPlainText().split("\n")
		bone = []
		for i in t:
			if (i!=""):
				g = int(i)
				bone.append(g)

		
		t= self.singleM2.toPlainText().split("\n")
		btwo = []
		for i in t:
			if (i!=""):
				g = int(i)
				btwo.append(g)

		###fix this!!####
		#if len(bone) != len(btwo):
		#	if len(bone) > len(btwo):
				

		return (bone,btwo)

	def portAll(self):
		(bone,btwo) = self.getBones()
		for c in range(len(bone)):
			ic = 0
			for i in self.m1.bones:
				jc = 0
				for j in self.m2.bones:
					if (Dependent(i,self.m1,bone[c],ic) & Dependent(j,self.m2,btwo[c],jc)) & (Depth(i,self.m1) == Depth(j,self.m2)):
						PortAll(i,j,self.m1,self.m2)
						break
					jc += 1
				ic += 1
				
		
		(bone,btwo) = self.getSingleBones()
		for c in range(len(bone)):
			PortAll(self.m1.bones[bone[c]],self.m2.bones[btwo[c]],self.m1,self.m2)

	def portSelected(self):
		(bone,btwo) = self.getBones()		
		anim2 = self.m2.animations[self.animsm2Box.currentIndex()]
		anim1 = self.m1.animations[self.animsm1Box.currentIndex()]
		for c in range(len(bone)):
			ic = 0
			for i in self.m1.bones:
				jc = 0
				for j in self.m2.bones:
					if (Dependent(i,self.m1,bone[c],ic) & Dependent(j,self.m2,btwo[c],jc)) & (Depth(i,self.m1) == Depth(j,self.m2)):
						PortSelected(i,j,self.m1,self.m2,anim1.animId,anim2.animId,anim1.subId,anim2.subId)
						break
					jc += 1
				ic += 1
				
		
		(bone,btwo) = self.getSingleBones()
		for c in range(len(bone)):
			PortSelected(self.m1.bones[bone[c]],self.m2.bones[btwo[c]],self.m1,self.m2,anim1.animId,anim2.animId,anim1.subId,anim2.subId)

	def addAnim(self):
		anim = self.m2.animations[self.animsm2Box.currentIndex()]
		(canim,tmp) = getAnim(anim.animId,anim.subId,self.m1,self.m2)
		(bone,btwo) = self.getBones()
		for c in range(len(bone)):
			ic = 0
			for i in self.m1.bones:
				jc = 0
				for j in self.m2.bones:
					if (Dependent(i,self.m1,bone[c],ic) & Dependent(j,self.m2,btwo[c],jc)) & (Depth(i,self.m1) == Depth(j,self.m2)):
						AddAnim(i,j,canim)
						break
					jc += 1	
				ic += 1
			
		(bone,btwo) = self.getSingleBones()
		for c in range(len(bone)):
			AddAnim(self.m1.bones[bone[c]],self.m2.bones[btwo[c]],canim)
		
		self.updateAnimBox(self.m1,self.animsm1Box)

	def updateAnimBox(self,model,box):
		for i in model.animations:
			box.addItem(giveAnimName(i.animId)+"["+str(i.subId)+"]")


	def updateTree(self,model,tree):
		tree.clear()
		c = 0
		for i in (model.bones):
       			icon = QtGui.QIcon()
        		icon.addPixmap(QtGui.QPixmap("Icons/edit-Bone.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
			if i.parent == -1:
				item = Node(tree)
				item.setId(c)
			else:
				j = -1
				for n in range(tree.topLevelItemCount()):
					j = iterateThroughChildren(tree.topLevelItem(n),i.parent) 
					if j != -1:
						item = Node(j)				
						item.setId(c)
						break
				if j == -1:
					print ("Unable to find parent of Bone " + str(c) +" which is: " + str(i.parent))
					item = Node(tree)				
					item.setId(c)
			if i.KeyBoneId != -1:
				item.setText(0,"Bone: "+str(item.Id)+" "+KeyBoneTypes[i.KeyBoneId])
			else:
				item.setText(0,"Bone "+str(item.Id))
			item.setIcon(0, icon)
			item.setNodeType("Bone")
			c += 1
		c = 0
		for i in (model.attachments):
       			icon = QtGui.QIcon()
        		icon.addPixmap(QtGui.QPixmap("Icons/edit-attachment.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
			if i.bone == -1:
				item = Node(tree)
				item.setId(c)
			else:
				for n in range(tree.topLevelItemCount()):
					j = iterateThroughChildren(tree.topLevelItem(n),i.bone) 
					if j != -1:
						item = Node(j)				
						item.setId(c)
						break
				if j == -1:
					print ("Unable to find bone of Attachment " + str(c) +" which is: " + str(i.bone))
					item = Node(tree)				
					item.setId(c)
			item.setText(0,"Attachment: "+str(item.Id)+" "+attachment_types[i.Id])
			item.setIcon(0, icon)
			item.setNodeType("Attachment")
			c += 1
		c = 0
		for i in (model.events):
       			icon = QtGui.QIcon()
        		icon.addPixmap(QtGui.QPixmap("Icons/edit-event.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
			if i.Bone == -1:
				item = Node(tree)
				item.setId(c)
			else:
				for n in range(tree.topLevelItemCount()):
					j = iterateThroughChildren(tree.topLevelItem(n),i.Bone) 
					if j != -1:
						item = Node(j)				
						item.setId(c)
						break
				if j == -1:
					print ("Unable to find bone of Event " + str(c) +" which is: " + str(i.Bone))
					item = Node(tree)				
					item.setId(c)
			item.setText(0,"Event: "+str(item.Id)+" "+str(i.Id))
			item.setIcon(0, icon)
			item.setNodeType("Event")
			c += 1



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


def CheckAnimFile(anim,animfile,output):
#	print animfile
	a_name = output.filename[0:len(output.filename)-3]
	first = str(anim.animId)
	while len(first) < 4:
		first = "0" +first
	scnd  = str(anim.subId)
	while len(scnd) < 2:
		scnd = "0" +scnd
	fname = a_name + first + "-" + scnd + ".anim"
	print (animfile[0],fname)
	return (animfile[0],fname)


def getAnim(canim,sId,om2,im2):
	canimId = []
	n = 0
	for i in im2.animations:
		if (i.animId == canim) & (i.subId == sId):
			canimId.append(i.index)
			om2.animations.append(i)
			om2.hdr.animations.count += 1
			pos = len(om2.animations)-1
			om2.animations[pos].index = pos
			apos = len(om2.anim_files)-1
			om2.anim_files.append(CheckAnimFile(i,im2.anim_files[n],om2))
			if i.next != -1:
				sId += 1
				(tmp,om2.animations[pos].next) = getAnim(canim,sId,om2,im2)
				canimId.extend(tmp)
				
			while om2.hdr.anim_lookup.count <= canim:
				om2.hdr.anim_lookup.count +=1
				t = Lookup()
				t.Id = -1
				om2.anim_lookup.append(t)
			t = Lookup()
			t.Id = om2.animations[pos].index
			om2.anim_lookup[canim] = t
			
			return (canimId,om2.animations[pos].index)
		n += 1

def AddAnim(i,j,canimId):
	diffVec = j.pivot - i.pivot # c = b - a, c is the vector from the bone getting the animations to the bone containg them
	for n in canimId:
		if ( j.translation.nTimes > n):
			i.translation.interpolation = j.translation.interpolation#change interpolation values
			i.translation.nTimes += 1
			i.translation.nKeys += 1
			i.translation.TimeSubs.append(j.translation.TimeSubs[n]) #change timestamps
			i.translation.KeySubs.append(j.translation.KeySubs[n]) #change values
			for v in i.translation.KeySubs[len(i.translation.KeySubs)-1].values:
				v = v - diffVec #translation values should be changed to fit the other bone
			#so it what we do here is: v = v - c 
			#the value gets a new position, relative to the new bone 
		if ( j.rotation.nTimes > n):		
			i.rotation.interpolation = j.rotation.interpolation
			i.rotation.nTimes += 1
			i.rotation.nKeys += 1
			i.rotation.TimeSubs.append(j.rotation.TimeSubs[n])
			i.rotation.KeySubs.append(j.rotation.KeySubs[n])
	
		if ( j.scaling.nTimes > n):			
			i.scaling.interpolation = j.scaling.interpolation
			i.scaling.nTimes += 1
			i.scaling.nKeys += 1
			i.scaling.TimeSubs.append(j.scaling.TimeSubs[n])
			i.scaling.KeySubs.append(j.scaling.KeySubs[n])


def PortAll(i, j,om2,im2):
	diffVec = j.pivot - i.pivot # c = b - a, c is the vector from the bone getting the animations to the bone containg them
	for k in om2.animations:
		for n in im2.animations:
			if (k.animId == n.animId) & (k.subId == n.subId):#if it's the same animation, change the values
			
				if (i.translation.nTimes > k.index) & ( j.translation.nTimes > n.index):
					i.translation.interpolation = j.translation.interpolation#change interpolation values
					i.translation.TimeSubs[k.index] = j.translation.TimeSubs[n.index] #change timestamps
					i.translation.KeySubs[k.index] = j.translation.KeySubs[n.index] #change values
					for v in i.translation.KeySubs[k.index].values:
						v = v - diffVec #translation values should be changed to fit the other bone
						#so it what we do here is: v = v - c 
						#the value gets a new position, relative to the new bone 
				
				if (i.rotation.nTimes > k.index) & ( j.rotation.nTimes > n.index):
					i.rotation.interpolation = j.rotation.interpolation
					i.rotation.TimeSubs[k.index] = j.rotation.TimeSubs[n.index]
					i.rotation.KeySubs[k.index] = j.rotation.KeySubs[n.index]
				
				if (i.scaling.nTimes > k.index) & ( j.scaling.nTimes > n.index):
					i.scaling.interpolation = j.scaling.interpolation
					i.scaling.TimeSubs[k.index] = j.scaling.TimeSubs[n.index]
					i.scaling.KeySubs[k.index] = j.scaling.KeySubs[n.index]


def PortSelected(i, j,om2,im2,anim1,anim2,sub1,sub2):
	diffVec = j.pivot - i.pivot # c = b - a, c is the vector from the bone getting the animations to the bone containg them
	for k in om2.animations:
		for n in im2.animations:
			if (k.animId == anim1) & (n.animId == anim2) &(k.subId == sub1) & (n.subId == sub2):#if it's the  animation, change the values
			
				if (i.translation.nTimes > k.index) & ( j.translation.nTimes > n.index):
					i.translation.interpolation = j.translation.interpolation#change interpolation values
					i.translation.TimeSubs[k.index] = j.translation.TimeSubs[n.index] #change timestamps
					i.translation.KeySubs[k.index] = j.translation.KeySubs[n.index] #change values
					for v in i.translation.KeySubs[k.index].values:
						v = v - diffVec #translation values should be changed to fit the other bone
						#so it what we do here is: v = v - c 
						#the value gets a new position, relative to the new bone 
				
				if (i.rotation.nTimes > k.index) & ( j.rotation.nTimes > n.index):
					i.rotation.interpolation = j.rotation.interpolation
					i.rotation.TimeSubs[k.index] = j.rotation.TimeSubs[n.index]
					i.rotation.KeySubs[k.index] = j.rotation.KeySubs[n.index]
				
				if (i.scaling.nTimes > k.index) & ( j.scaling.nTimes > n.index):
					i.scaling.interpolation = j.scaling.interpolation
					i.scaling.TimeSubs[k.index] = j.scaling.TimeSubs[n.index]
					i.scaling.KeySubs[k.index] = j.scaling.KeySubs[n.index]


#get the depth of a bone
def Depth(bone,file):
	ret = 0
	
	while (bone.parent != -1):
		ret += 1
		bone = file.bones[bone.parent]
		
	return ret
#check if it "hangs" on that bone, or is it	
def Dependent(bone,file,id,ego):
	if ego == id:
		return True
	while (bone.parent != -1):
		if (bone.parent == id):
			return True
		bone = file.bones[bone.parent]
	return False




app = QtGui.QApplication(sys.argv) 
dialog = AnimPorter() 
dialog.show() 
sys.exit(app.exec_())

