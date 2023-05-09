import sys
import ui
from classes.translate.googleTranslator import *
from classes.translate.TranslationResources.googleTranslateLanguages import *
from PyQt6 import QtCore, QtGui, QtWidgets


class TranslateMate(QtWidgets.QMainWindow, QtWidgets.QWidget, ui.Ui_MainWindow):


    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.translateLabel.mousePressEvent = self.translate
        self.actionExit.triggered.connect(self.exitProgramm)
        self.loadLangArrays()
    
    def loadLangArrays(self):
        self.fromLang.addItems(googleLanguages.values())
        self.toLang.addItems(googleLanguages.values())


    def translate(self, eve):

        self.translateBox.clear()
        text = self.inputBox.toHtml()

        translated = GoogleTranslator().translate(
            text, 
            self.getKeyLang(self.toLang.currentText()),
            self.getKeyLang(self.fromLang.currentText())
        )
        self.translateBox.insertHtml(translated)

    def getKeyLang(self, value):

        for k, v in googleLanguages.items():
            if (isinstance(v, list) and value in v) or value == v:
                return k
        else:
            print(f'Cant find value {value}')
    
    def exitProgramm(self):
        sys.exit(app.exec())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
