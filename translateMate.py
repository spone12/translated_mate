import sys
import ui
from PyQt6 import QtCore, QtGui, QtWidgets


class TranslateMate(QtWidgets.QMainWindow, QtWidgets.QWidget, ui.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.translateLabel.mousePressEvent = self.translate

    def translate(self, eve):
        print("translate")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
