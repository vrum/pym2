#! /usr/bin/python
 
from PyQt4 import QtGui, QtCore 
from pymodeleditor import PyModelEditor as Editor
import sys


class PyModelEditor(QtGui.QDialog, Editor): 
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)
		self.getLastDir()




app = QtGui.QApplication(sys.argv) 
dialog = PyModelEditor() 
dialog.show() 
sys.exit(app.exec_())
