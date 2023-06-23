from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow): # QDialog vient de widget.class dans .ui
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/main.ui', self) # Load the .ui file
        self.show() # Show the GUI

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()