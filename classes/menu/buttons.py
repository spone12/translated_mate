from PyQt6.QtWidgets import QApplication
from classes.translate.googleTranslator import *
from classes.translate.TranslationResources.lang import Lang

class Buttons():
    """
        Main program buttons
    """

    def __init__(self, ui):
        self.ui = ui

    def clearTranslate(self, eve):
        self.ui.translateBox.clear()
        self.ui.inputBox.clear()

    def copyToClipboard(self, eve):
        
        QApplication.clipboard().setText(self.ui.translateBox.toPlainText())
