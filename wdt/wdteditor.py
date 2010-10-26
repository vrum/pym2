# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui
import sys

from wowfile import *
from wdt import *

class WDTEditor(QtGui.QMainWindow):
	def __init__(self): 
		QtGui.QMainWindow.__init__(self) 
		self.setupUi(self)		
		self.getLastDir()
		self.wdt = WDTFile()
		
	def setupUi(self, MainWindow):
		self.lastDir = QtCore.QDir.currentPath()
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.tabWidget = QtGui.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(20, 0, 780, 570))
		self.tabWidget.setObjectName("tabWidget")
		
		self.terrTab = QtGui.QWidget()
		self.terrTab.setObjectName("terrTab")
		
		self.scrollArea = QtGui.QScrollArea(self.terrTab)
		self.scrollArea.setGeometry(QtCore.QRect(10, 50, 700, 490))
		#self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		#self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		#self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		
		self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 970, 970))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
		
		self.terrCheck = []
		for x in xrange(64):
			for y in xrange(64):
				t = QtGui.QCheckBox(self.scrollAreaWidgetContents)
				t.setGeometry(QtCore.QRect(x*15, y*15, 15, 15))
				t.setText("")
				t.setObjectName("terrainCheck "+str(x)+" "+str(y))
				t.setToolTip(str(x)+"/"+str(y))
				self.terrCheck.append(t)
				
		
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		
		
		self.vertexCheck = QtGui.QCheckBox(self.terrTab)
		self.vertexCheck.setGeometry(QtCore.QRect(10, 0, 121, 17))
		self.vertexCheck.setObjectName("vertexCheck")
		
		self.alphaCheck = QtGui.QCheckBox(self.terrTab)
		self.alphaCheck.setGeometry(QtCore.QRect(10, 20, 91, 17))
		self.alphaCheck.setObjectName("alphaCheck")
		
		self.tabWidget.addTab(self.terrTab, "")
		self.wmoTab = QtGui.QWidget()
		self.wmoTab.setObjectName("wmoTab")
		
		self.filenameEdit = QtGui.QLineEdit(self.wmoTab)
		self.filenameEdit.setGeometry(QtCore.QRect(10, 30, 531, 20))
		self.filenameEdit.setObjectName("filenameEdit")
		
		self.label = QtGui.QLabel(self.wmoTab)
		self.label.setGeometry(QtCore.QRect(20, 10, 51, 16))
		self.label.setObjectName("label")
		
		self.doodadBox = QtGui.QComboBox(self.wmoTab)
		self.doodadBox.setGeometry(QtCore.QRect(10, 80, 69, 22))
		self.doodadBox.setObjectName("doodadBox")
		
		self.nameBox = QtGui.QComboBox(self.wmoTab)
		self.nameBox.setGeometry(QtCore.QRect(100, 80, 69, 22))
		self.nameBox.setObjectName("nameBox")
		
		self.oriA = QtGui.QDoubleSpinBox(self.wmoTab)
		self.oriA.setGeometry(QtCore.QRect(10, 150, 62, 22))
		self.oriA.setMaximum(360.0)
		self.oriA.setObjectName("oriA")
		
		self.oriB = QtGui.QDoubleSpinBox(self.wmoTab)
		self.oriB.setGeometry(QtCore.QRect(80, 150, 62, 22))
		self.oriB.setMaximum(360.0)
		self.oriB.setObjectName("oriB")
		
		self.oriC = QtGui.QDoubleSpinBox(self.wmoTab)
		self.oriC.setGeometry(QtCore.QRect(150, 150, 62, 22))
		self.oriC.setMaximum(360.0)
		self.oriC.setObjectName("oriC")
		
		self.label_2 = QtGui.QLabel(self.wmoTab)
		self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 16))
		self.label_2.setObjectName("label_2")
		
		self.label_3 = QtGui.QLabel(self.wmoTab)
		self.label_3.setGeometry(QtCore.QRect(100, 60, 61, 16))
		self.label_3.setObjectName("label_3")
		
		self.label_4 = QtGui.QLabel(self.wmoTab)
		self.label_4.setGeometry(QtCore.QRect(10, 130, 71, 16))
		self.label_4.setObjectName("label_4")
		
		self.xPos = QtGui.QLineEdit(self.wmoTab)
		self.xPos.setGeometry(QtCore.QRect(10, 210, 61, 20))
		self.xPos.setObjectName("xPos")
		
		self.yPos = QtGui.QLineEdit(self.wmoTab)
		self.yPos.setGeometry(QtCore.QRect(80, 210, 61, 20))
		self.yPos.setObjectName("yPos")
		
		self.zPos = QtGui.QLineEdit(self.wmoTab)
		self.zPos.setGeometry(QtCore.QRect(150, 210, 61, 20))
		self.zPos.setObjectName("zPos")
		
		self.label_5 = QtGui.QLabel(self.wmoTab)
		self.label_5.setGeometry(QtCore.QRect(10, 190, 46, 13))
		self.label_5.setObjectName("label_5")
		
		self.tabWidget.addTab(self.wmoTab, "")
		
		MainWindow.setCentralWidget(self.centralwidget)
		
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 21))
		self.menubar.setObjectName("menubar")
		
		self.menuFile = QtGui.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		
		MainWindow.setMenuBar(self.menubar)
		self.actionNew = QtGui.QAction(MainWindow)
		self.actionNew.setObjectName("actionNew")
		
		self.actionOpen = QtGui.QAction(MainWindow)
		self.actionOpen.setObjectName("actionOpen")		
		self.connect(self.actionOpen, QtCore.SIGNAL("triggered()"), self.openFile)
		
		self.actionSave = QtGui.QAction(MainWindow)
		self.actionSave.setObjectName("actionSave")
		self.connect(self.actionSave, QtCore.SIGNAL("triggered()"), self.saveFile)
		
		self.actionClose = QtGui.QAction(MainWindow)
		self.actionClose.setObjectName("actionClose")
		
		self.menuFile.addAction(self.actionNew)
		self.menuFile.addAction(self.actionOpen)
		self.menuFile.addAction(self.actionSave)
		self.menuFile.addAction(self.actionClose)
		self.menubar.addAction(self.menuFile.menuAction())

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(1)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.MainWindow = MainWindow

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
		self.vertexCheck.setText(QtGui.QApplication.translate("MainWindow", "Use Vertex Shading", None, QtGui.QApplication.UnicodeUTF8))
		self.alphaCheck.setText(QtGui.QApplication.translate("MainWindow", "Has Big Alpha", None, QtGui.QApplication.UnicodeUTF8))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.terrTab), QtGui.QApplication.translate("MainWindow", "Terrain", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("MainWindow", "Filename:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Doodadset:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Nameset:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Orientation:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Position:", None, QtGui.QApplication.UnicodeUTF8))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.wmoTab), QtGui.QApplication.translate("MainWindow", "World Model Object", None, QtGui.QApplication.UnicodeUTF8))
		self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
		self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
		self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
		self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
	
	def getLastDir(self):
		conf = open("WDTEditor.conf","a+")
		path = conf.readline()
		conf.close()
		if len(path) > 2:
			self.lastDir = path
		else:
			self.lastDir = QtCore.QDir.currentPath()
			
	def saveLastDir(self):
		conf = open("WDTEditor.conf","w+")
		conf.write(self.lastDir)
		conf.close()	

	
	def openFile(self):
		filename = QtGui.QFileDialog().getOpenFileName(self,"Open File",self.lastDir)
		self.MainWindow.setWindowTitle(filename)
		self.wdt.read(filename)
		for x in xrange(64):
			for y in xrange(64):
				if self.wdt.main.hasADT(x,y):
					self.terrCheck[y+x*64].setCheckState(2)
				else:
					self.terrCheck[y+x*64].setCheckState(0)
					
		if self.wdt.mphd.hasBigAlpha():
			self.alphaCheck.setCheckState(2)
		else:
			self.alphaCheck.setCheckState(0)	
			
		if self.wdt.mphd.hasVertexShading():
			self.vertexCheck.setCheckState(2)
		else:
			self.vertexCheck.setCheckState(0)
			
		self.filenameEdit.setText(self.wdt.getWMOName())
		pos = self.wdt.getWMOPosition()
		self.xPos.setText(str(pos.x))
		self.yPos.setText(str(pos.y))
		self.zPos.setText(str(pos.y))
		
		ori = self.wdt.getWMOOrientation()
		self.oriA.setValue(ori.x)
		self.oriB.setValue(ori.y)
		self.oriC.setValue(ori.z)
				
		
		filename = str(filename)
		last = filename.rfind("/")
		self.lastDir = filename[0:last]		
		self.saveLastDir()
		
			
	def saveFile(self):		
		filename = QtGui.QFileDialog().getSaveFileName(self,"Save File",self.lastDir)
		
		hasTerr = False
		for x in xrange(64):
			for y in xrange(64):
				if (self.terrCheck[y+x*64].checkState() == 2):
					self.wdt.checkTile(x,y)		
					hasTerr = True
				else:
					self.wdt.uncheckTile(x,y)
					
		if (hasTerr == True):
			self.wdt.setTerrain()
		else:
			self.wdt.unsetTerrain()
		
		print self.alphaCheck.checkState()
		if (self.alphaCheck.checkState() == 2):
			self.wdt.setBigAlpha()
		else:
			self.wdt.unsetBigAlpha()
					
		if (self.vertexCheck.checkState() == 2):
			self.wdt.setVertexShading()
		else:
			self.wdt.unsetVertexShading()
			
		#if (hasTerr == False):	
		name = str(self.filenameEdit.text())
		name.encode("cp1252")
		
		self.wdt.setWMOName(name)	
		pos = Vec3()
		pos.x = float(self.xPos.text())
		pos.y = float(self.yPos.text())
		pos.z = float(self.zPos.text())
		self.wdt.setWMOPosition(pos)
			
		self.wdt.write(filename)
			
			
		filename = str(filename)
		last = filename.rfind("/")
		self.lastDir = filename[0:last]		
		self.saveLastDir()

		
app = QtGui.QApplication(sys.argv) 
dialog = WDTEditor() 
dialog.show() 
sys.exit(app.exec_())
