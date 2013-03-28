# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Mar 27 15:33:52 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_NotePad(object):
    def setupUi(self, NotePad):
        NotePad.setObjectName(_fromUtf8("NotePad"))
        NotePad.resize(738, 428)
        self.centralWidget = QtGui.QWidget(NotePad)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(73, 20, 481, 361))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.openFile = QtGui.QPushButton(self.centralWidget)
        self.openFile.setGeometry(QtCore.QRect(113, 40, 101, 21))
        self.openFile.setObjectName(_fromUtf8("openFile"))
        self.saveFile = QtGui.QPushButton(self.centralWidget)
        self.saveFile.setGeometry(QtCore.QRect(253, 40, 111, 21))
        self.saveFile.setObjectName(_fromUtf8("saveFile"))
        self.closeFile = QtGui.QPushButton(self.centralWidget)
        self.closeFile.setGeometry(QtCore.QRect(400, 40, 111, 21))
        self.closeFile.setAutoFillBackground(False)
        self.closeFile.setObjectName(_fromUtf8("closeFile"))
        NotePad.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(NotePad)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 738, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        NotePad.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(NotePad)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        NotePad.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(NotePad)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        NotePad.setStatusBar(self.statusBar)
        self.retranslateUi(NotePad)
        QtCore.QMetaObject.connectSlotsByName(NotePad)

    def retranslateUi(self, NotePad):
        NotePad.setWindowTitle(_translate("NotePad", "MainWindow", None))
        self.openFile.setText(_translate("NotePad", "Open File", None))
        self.saveFile.setText(_translate("NotePad", "Save File", None))
        self.closeFile.setText(_translate("NotePad", "Close File", None))

