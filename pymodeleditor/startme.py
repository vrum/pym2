#! /usr/bin/python

import sys 
from PyQt4 import QtGui, QtCore 
from pymodeleditor import PyModelEditor as Editor



class PyModelEditor(QtGui.QDialog, Editor): 
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)




app = QtGui.QApplication(sys.argv) 
dialog = PyModelEditor() 
dialog.show() 
sys.exit(app.exec_())
