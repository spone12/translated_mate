# Save translation window
from classes.logger import *
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QStyledItemDelegate, QPushButton


class FlashCardsWindow():
    """
        Flash cards window
    """

    def __init__(self, ui):
        self.ui = ui

    def changeWindow(self) -> None:
        """
            Change the window to "flash cards", or back to translator
        """
        
        if self.ui.stackedWidget.currentIndex() == 0:
            
            self.ui.stackedWidget.setCurrentIndex(2)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
    