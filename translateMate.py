# Translate mate
# Version 0.6
import sys
import ui
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from classes.translate.googleTranslator import *
from classes.translate.TranslationResources.loadLangs import LoadingLangs
from classes.menu.menu import Menu
from classes.menu.buttons import Buttons
from classes.windows.savedTranslation import *


class TranslateMate(QtWidgets.QMainWindow, QtWidgets.QWidget, ui.Ui_MainWindow):
    """
        Main program launch class
    """

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('appico.ico'))
        self.currentTranslator = 'Google'
        
        self.loadLang = LoadingLangs(self)
        self.menu = Menu(self)
        self.buttons = Buttons(self)
        self.db = SavedTranslationWindow(self)
        print(self.db.getSavedTranslate())
        
        self.programEvents()
        
        
    def programEvents(self) -> None:
        """
            Loading program events
        """
        self.translateLabel.mousePressEvent = self.buttons.prepareTranslate
        self.saveTranslatedText.mousePressEvent = self.buttons.saveTranslatedText
        self.reverseTranslate.mousePressEvent = self.buttons.reverseTranslations
        self.clearInput.mousePressEvent = self.buttons.clearTranslate
        self.copyTranslate.mousePressEvent = self.buttons.copyToClipboard
        self.saveTranslationWindow.mousePressEvent = self.buttons.saveTranslationWindow
        self.actionExit.triggered.connect(self.menu.exitProgramm)
        self.chooseTranslator.triggered.connect(self.loadLang.chooseTranslator)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
