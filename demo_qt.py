from PyQt5 import QtWidgets, uic
import sys

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/my_dialog.ui', self)

class Ui(QtWidgets.QMainWindow): # QDialog vient de widget.class dans .ui
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/main.ui', self) # Load the .ui file
        self.label.setText("toto")
        self.show() # Show the GUI
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.dialog = MyDialog()

    def pushButton_clicked(self):
        self.lineEdit.setText("Hello")
        self.dialog.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()