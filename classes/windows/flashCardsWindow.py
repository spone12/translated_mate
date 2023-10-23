# Save translation window
from classes.logger import *
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QStyledItemDelegate, QPushButton


class FlashCardsWindow():
    """
        Flash cards window
    """

    QSindex = 2

    def __init__(self, ui):
        self.ui = ui

    def changeWindow(self) -> None:
        """
            Change the window to "flash cards"
        """
        
        self.ui.stackedWidget.setCurrentIndex(self.QSindex)
    