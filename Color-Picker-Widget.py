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

        #progress bar
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn = QtGui.QPushButton("Download",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        #drop-down
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("Windows Vista",self)
        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("WindowsVista")

        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style-choice)

        #calendar
        cal = QtGui.QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)

        self.show()
        #font-widget
        fontChoice = QtGui.QAction('Font',self)
        fontChoice.triggered.connect(self.font-choice)
        #self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

        #color picker widget
        color = QtGui.QColor(0,0,0)
        fontColor = QtGui.QAction('Font bg color', self)
        fontColor.triggered.connect(self.color-picker)
        self.toolBar.addAction(fontColor)

        self.show()
    def color-picker(self) :
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyle("QWidget(background-color:%s)" %color.name())
    def font-choice():
        font,valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def style-choice(self,Text) :
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))


    def download(self) :
        self.completed = 0
        while self.completed < 100 :
            self.completed += 0.0001
            self.progress.setValue(self.completed)

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
