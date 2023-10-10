# Save translation window
import sqlite3
from classes.logger import *


class SaveTranslationWindow():
    """
        Save translation window class
    """

    def __init__(self, ui):
        self.ui = ui

    def changeWindow(self) -> None:
        """
            Change the window to "saved translations", or back to translator
        """
        
        if self.ui.stackedWidget.currentIndex() == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
