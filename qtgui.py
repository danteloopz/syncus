from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class SyncusQt(QMainWindow):
    def __init__(self):
        super(SyncusQt, self).__init__()
        self.setGeometry(300,300,400,500)
        self.setWindowTitle("Syncus")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello from label")
        self.label.move(50,50)

def window():
    app = QApplication([])
    win = SyncusQt()
    win.show()
    app.exec()


window()