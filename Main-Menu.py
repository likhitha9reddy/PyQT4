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

    def close_application(self):
        print("Customize")
        sys.exit()

def run():
    app = QtGui.QApplication([])
    GUI = Window()
    sys.exit(app.exec_())

run()
