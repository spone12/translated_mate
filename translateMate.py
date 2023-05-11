# Translate mate
# Version 0.3
import sys
import ui
from classes.translate.googleTranslator import *
from classes.translate.TranslationResources.lang import Lang
from classes.menu.menu import Menu
from classes.menu.buttons import Buttons
from PyQt6 import QtCore, QtGui, QtWidgets


class TranslateMate(QtWidgets.QMainWindow, QtWidgets.QWidget, ui.Ui_MainWindow):


    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('appico.ico'))
        
        self.lang = Lang(self)
        self.menu = Menu(self)
        self.buttons = Buttons(self)
        self.translateLabel.mousePressEvent = self.translate
        self.reverseTranslate.mousePressEvent = self.lang.reverseTranslations
        self.clearInput.mousePressEvent = self.buttons.clearTranslate
        self.copyTranslate.mousePressEvent = self.buttons.copyToClipboard
        self.actionExit.triggered.connect(self.menu.exitProgramm)
    

    def translate(self, eve) -> None:
        """
           Preparation before the translation 
        """

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
