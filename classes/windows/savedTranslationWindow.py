# Save translation window
import sqlite3
from classes.logger import *
from PyQt6 import QtWidgets


class SavedTranslationWindow():
    """
        Translation window
    """

    columnsWidth = [120, 120, 345, 345, 50]
    headerLabels = ['From', 'To', 'Native', 'Translate', 'Delete']

    def __init__(self, ui):
        self.ui = ui
    
    def renderSavedTable(self) -> None:
        """
            Render a saved translation table
        """

        savedTranslations = self.ui.db.getSavedTranslate()
        self.ui.savedTranslateWidget.setRowCount(len(savedTranslations))
        self.ui.savedTranslateWidget.setColumnCount(5)

        self.ui.savedTranslateWidget.setHorizontalHeaderLabels(self.headerLabels)
        for ind, width in enumerate(self.columnsWidth):
            self.ui.savedTranslateWidget.setColumnWidth(ind, width)

        rowIndex = 0
        for translation in savedTranslations:
            for j in range (1, 5):
                self.ui.savedTranslateWidget.setItem(
                    rowIndex, (j - 1), QtWidgets.QTableWidgetItem(translation[j])
                )
            rowIndex += 1 

    def changeWindow(self) -> None:
        """
            Change the window to "saved translations", or back to translator
        """
        
        if self.ui.stackedWidget.currentIndex() == 0:
            
            self.renderSavedTable()
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
