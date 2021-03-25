import sys, shutil, os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("./ui/sort.ui", self)
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.browse.clicked.connect(self.browsefiles)
        self.sort.clicked.connect(self.sorter)
        self.console.setReadOnly(True)
        self.sort.setEnabled(False)

    def browsefiles(self):
        self.fname = QFileDialog.getExistingDirectory(self, "Choose directory", "D:/")
        self.filename.setText(self.fname)
        if self.fname == "":
            pass
        else:
            self.sort.setEnabled(True)

    def sorter(self, fname):
        if self.fname == "":
            pass
        else:
            self.console.clear()
            cwd = self.fname
            stuff = [x for x in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, x))]
            na = []
            ex = []
            for l in stuff:
                name, ext = os.path.splitext(l)
                if len(ext) <= 6 and len(ext) >= 3:
                    na.append(name.lower())
                    ex.append(ext.lower())
            self.console.append("These files will be sorted: ")
            for n, e in zip(na,ex):
                self.console.append(f"{cwd}/{(n.lower())+(e.lower())}")
            self.console.append("*************************************")
            for e in set(ex):
                if not os.path.exists(os.path.join(cwd, e.upper())):
                    os.mkdir(os.path.join(self.fname, e.upper()))
                else:
                    pass
            for n, e in zip(na,ex):
                shutil.move((os.path.join(cwd, (n+e))), (os.path.join(cwd, e.upper())))
                self.console.append("{} -> {}".format((cwd+"/"+n.lower()+e.lower()), (cwd+"/"+e.upper())))
            self.console.append("\nSorting Completed!")
            


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(400)
widget.setFixedWidth(650)
widget.show()
sys.exit(app.exec_())

