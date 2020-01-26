import sys
from PyQt4 import QtGui

app = QtGui.QApplication([])

window = QtGui.QWidget()
window.setGeometry(50,50,500,500)
window.setWindowTitle("PyQt Tutorial")

window.show()
sys.exit(app.exec_())
