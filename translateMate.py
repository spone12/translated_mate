import sys
import ui
from classes.translate.googleTranslator import *
from classes.translate.TranslationResources.lang import Lang
from PyQt6 import QtCore, QtGui, QtWidgets


class TranslateMate(QtWidgets.QMainWindow, QtWidgets.QWidget, ui.Ui_MainWindow):


    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('appico.ico'))
        
        self.lang = Lang(self)
        self.translateLabel.mousePressEvent = self.translate
        self.actionExit.triggered.connect(self.exitProgramm)
    

    def translate(self, eve) -> None:

        if not self.inputBox.toPlainText():
            return

        self.translateBox.clear()
        text = self.inputBox.toHtml()

        translated = GoogleTranslator().translate(
            text, 
            self.lang.getKeyLang(self.toLang.currentText()),
            self.lang.getKeyLang(self.fromLang.currentText())
        )
        self.translateBox.insertHtml(translated)

    
    def exitProgramm(self):

        sys.exit(app.exec())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
