from mainwindow import Ui_NotePad
from PyQt4 import QtGui, QtCore
import sys


class StartQt4(QtGui.QMainWindow):
    """
        # slots --> UI objects like buttons, text edit etc.
        # signals --> user prompt actions
    """
    def __init__(self, parent=None):
        """

        :param parent:
        """
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_NotePad()
        self.ui.setupUi(self)
        # connecting slot openFile button to signal
        # openFile --> button (slot) | clicked() --> SIGNAL | fileOpen --> action method
        QtCore.QObject.connect(self.ui.openFile, QtCore.SIGNAL('clicked()'), self.fileOpen)
        QtCore.QObject.connect(self.ui.saveFile, QtCore.SIGNAL('clicked()'), self.fileSave)
        #QtCore.QObject.connect(self.ui.closeFile, QtCore.SIGNAL('clicked()'), self.fileClose())

    def fileOpen(self):
        """
            open a txt file and display its contents on to the text edit

        """
        self.ui.textEdit.setText("Fuzzy Brain")  # shows up as soon as we click the file open button
        f = QtGui.QFileDialog(self)
        self.file_name = f.getOpenFileName()
        from os.path import isfile
        if isfile(self.file_name):
            #import codecs
            s = open(self.file_name, 'r').read()
            self.ui.textEdit.setPlainText(s)  # read file is displayed on to the text editor

    def fileSave(self):
        """
            make changes to the text file displayed and save it

        """
        from os.path import isfile
        if isfile(self.file_name):
            import codecs
            s = codecs.open(self.file_name, 'w', 'utf-8')
            s.write(unicode(self.ui.textEdit.toPlainText()))
            s.close()

    def fileClose(self):
        """
            close and exit file

        """
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_app = StartQt4()
    my_app.show()
    sys.exit(app.exec_())



