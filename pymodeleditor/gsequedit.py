

from PyQt4 import QtCore, QtGui
from m2 import *

class GSequEditor(QtGui.QDialog):
	def __init__(self): 
		QtGui.QDialog.__init__(self) 
		self.setupUi(self)

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(540, 373)

		self.textEdit = QtGui.QTextEdit(Dialog)
		self.textEdit.setGeometry(QtCore.QRect(10, 10, 511, 251))
		self.textEdit.setObjectName("textEdit")

		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(310, 320, 206, 34))
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.finalizeMe) 
		self.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Global Sequence Editor", None, QtGui.QApplication.UnicodeUTF8))
		self.textEdit.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


	def setModel(self,m2,skin):
		self.m2 = m2
		self.skin = skin
		s = ""
		for i in m2.gSequ:
			s += str(i.Timestamp)+"\n"

		self.textEdit.setPlainText(s)

	def finalizeMe(self):
		self.saveMe()
		self.accept()

	def saveMe(self):
		t= self.textEdit.toPlainText().split("\n")
		c = 0
		gsequ = []
		for i in t:
			if (i!=""):
				g = GlobalSequence()
				g.Timestamp = int(i)
				gsequ.append(g)
				c += 1

		self.m2.hdr.global_sequences.count = c
		self.m2.gSequ = gsequ
