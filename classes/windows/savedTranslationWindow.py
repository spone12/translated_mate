# Save translation window
from classes.logger import *
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStyledItemDelegate, QPushButton


class SavedTranslationWindow():
    """
        Translation window
    """

    columnsWidth = [100, 100, 350, 350, 50]
    headerLabels = ['From', 'To', 'Native', 'Translate', 'Delete']

    def __init__(self, ui):
        self.ui = ui
    
    def renderSavedTable(self) -> None:
        """
            Render a saved translation table
        """

        savedTranslations = self.ui.db.getSavedTranslate()

        # Set row and columns count
        self.ui.savedTranslateWidget.setRowCount(len(savedTranslations))
        self.ui.savedTranslateWidget.setColumnCount(5)

        # Set name header columns
        self.ui.savedTranslateWidget.setHorizontalHeaderLabels(self.headerLabels)

        # Set column width
        for ind, width in enumerate(self.columnsWidth):
            self.ui.savedTranslateWidget.setColumnWidth(ind, width)

        # Set read-only for name language columns
        delegate = ReadOnlyDelegate(self.ui.savedTranslateWidget)
        self.ui.savedTranslateWidget.setItemDelegateForColumn(0, delegate)
        self.ui.savedTranslateWidget.setItemDelegateForColumn(1, delegate)

        # Render table
        rowIndex = 0
        for translation in savedTranslations:
            for j in range (1, 6):
                if j == 5:
                    btn = QPushButton("Delete")
                    self.ui.savedTranslateWidget.setCellWidget(rowIndex, (j - 1), btn)
                else:
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


class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return 
