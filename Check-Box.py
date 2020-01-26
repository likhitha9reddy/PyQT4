import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("PyQt Tutorial")
        self.setWindowIcon(QtGui.QIcon('techbox.png'))

        extractAction = QtGui.QAction("&GET TO ISRO!", self)
        extractAction.setShortcut("Ctrl + Q")
        extractAction.setStatusTip("Leave the Application")
        extractAction.triggered.connect(self.close_application())

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)

        self.home()

        self.show()

    def home(self):
        btn = QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application())

        self.show()
        btn.resize(100,100)
        btn.move(100,100)

        #toolbar
        extractAction = QtGui.QAction(QtGui.QIcon('techbox.png'),'Flee the Scene',self)
        extractAction.triggered.connect(self.close_application())

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        #check-box
        checkBox = QtGui.QCheckBox('Enlarge Window', self)
        checkBox.move(100,25)
        checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window())

        self.show()

    def enlarge_window(self,state):
        if state == QtCore.QtChecked :
            self.setGeometry(50,50,1000,600)
        else :
            self.setGeometry(50,50,500,300)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self,'Extract!',"Get into ISRO",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes :
            print("Extracting")
            sys.exit()
        else :
            pass

def run():
    app = QtGui.QApplication([])
    GUI = Window()
    sys.exit(app.exec_())

run()
