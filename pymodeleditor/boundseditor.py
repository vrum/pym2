# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui

class BoundsEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
		self.last = -1
		
	def setupUi(self, BoxEditor):
		BoxEditor.setObjectName("BoxEditor")
		BoxEditor.resize(400, 167)
		self.buttonBox = QtGui.QDialogButtonBox(BoxEditor)
		self.buttonBox.setGeometry(QtCore.QRect(50, 110, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		
		self.maxX = QtGui.QLineEdit(BoxEditor)
		self.maxX.setGeometry(QtCore.QRect(70, 20, 41, 20))
		self.maxX.setObjectName("maxX")
		
		self.maxY = QtGui.QLineEdit(BoxEditor)
		self.maxY.setGeometry(QtCore.QRect(120, 20, 41, 20))
		self.maxY.setObjectName("maxY")
		
		self.maxZ = QtGui.QLineEdit(BoxEditor)
		self.maxZ.setGeometry(QtCore.QRect(170, 20, 41, 20))
		self.maxZ.setObjectName("maxZ")
		
		self.minX = QtGui.QLineEdit(BoxEditor)
		self.minX.setGeometry(QtCore.QRect(70, 50, 41, 20))
		self.minX.setObjectName("minX")
		
		self.minY = QtGui.QLineEdit(BoxEditor)
		self.minY.setGeometry(QtCore.QRect(120, 50, 41, 20))
		self.minY.setObjectName("minY")
		
		self.minZ = QtGui.QLineEdit(BoxEditor)
		self.minZ.setGeometry(QtCore.QRect(170, 50, 41, 20))
		self.minZ.setObjectName("minZ")
		
		self.label = QtGui.QLabel(BoxEditor)
		self.label.setGeometry(QtCore.QRect(10, 20, 46, 13))
		self.label.setObjectName("label")
		
		self.label_2 = QtGui.QLabel(BoxEditor)
		self.label_2.setGeometry(QtCore.QRect(10, 50, 46, 13))
		self.label_2.setObjectName("label_2")
		
		self.label_3 = QtGui.QLabel(BoxEditor)
		self.label_3.setGeometry(QtCore.QRect(10, 80, 46, 13))
		self.label_3.setObjectName("label_3")
		
		self.lineEdit = QtGui.QLineEdit(BoxEditor)
		self.lineEdit.setGeometry(QtCore.QRect(70, 80, 41, 20))
		self.lineEdit.setObjectName("lineEdit")

		self.retranslateUi(BoxEditor)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.finalizeMe)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), BoxEditor.reject)
		QtCore.QMetaObject.connectSlotsByName(BoxEditor)

	def retranslateUi(self, BoxEditor):
		BoxEditor.setWindowTitle(QtGui.QApplication.translate("BoxEditor", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("BoxEditor", "Maximum:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate("BoxEditor", "Minimum:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setText(QtGui.QApplication.translate("BoxEditor", "Radius:", None, QtGui.QApplication.UnicodeUTF8))

		
	def finalizeMe(self):
		self.bounds.Radius = float(self.lineEdit.text())
		self.bounds.minExtends.x = float(self.minX.text())
		self.bounds.minExtends.y = float(self.minY.text())
		self.bounds.minExtends.z = float(self.minZ.text())
		self.bounds.maxExtends.x = float(self.maxX.text())
		self.bounds.maxExtends.y = float(self.maxY.text())
		self.bounds.maxExtends.z = float(self.maxZ.text())
		self.accept()
		
		
	
	def setBounds(self,bounds):
		self.bounds = bounds
		self.lineEdit.setText(str(self.bounds.Radius))
		self.minX.setText(str(self.bounds.minExtends.x))
		self.minY.setText(str(self.bounds.minExtends.y))
		self.minZ.setText(str(self.bounds.minExtends.z))
		self.maxX.setText(str(self.bounds.maxExtends.x))
		self.maxY.setText(str(self.bounds.maxExtends.y))
		self.maxZ.setText(str(self.bounds.maxExtends.z))
