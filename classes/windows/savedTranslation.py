# Save translation window
import sqlite3
from classes.logger import *
from PyQt6 import QtWidgets


class SavedTranslationWindow():
    """
        Translation save window DB class
    """

    columnsWidth = [120, 120, 345, 345, 50]
    headerLabels = ['From', 'To', 'Native', 'Translate', 'Delete']

    def __init__(self, ui):
        self.ui = ui
        self.conn = sqlite3.connect('translate.db')
        self.curs = self.conn.cursor()
        self.createTranslateTable()

    def __del__(self):
        self.conn.commit()
        self.conn.close()
    
    def renderSavedTable(self) -> None:
        """
            Render a saved translation
        """

        savedTranslations = self.getSavedTranslate()
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

    def createTranslateTable(self) -> None:
        self.curs.execute('''
            CREATE TABLE IF NOT EXISTS Translate (
                id INTEGER PRIMARY KEY,
                trans_from TEXT NOT NULL,
                trans_to TEXT NOT NULL,
                text_from TEXT NOT NULL,
                text_to TEXT NOT NULL,
                knowledge SMALLINT DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    
    def getSavedTranslate(self, where = None):
        """
            Get saved translated rows
        """

        try:
            sql = "SELECT * FROM Translate"
            
            if where is not None:
                sql += " WHERE id=" + where

            self.curs.execute(sql)
            return self.curs.fetchall()
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Select error: {err}")

    def insertTranslate(self, trans_from, trans_to, text_from, text_to, knowledge = 1)  -> None:
        """
            Insert Row
        """

        try:
            self.curs.execute('INSERT INTO Translate (trans_from, trans_to, text_from, text_to, knowledge) VALUES (?, ?, ?, ?, ?)',
                (trans_from, trans_to, text_from, text_to, knowledge)
            )
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Insert error: {err}")

    def updateTranslate(self, id, text)  -> None:
        """
            Update Row
        """

        try:
           self.curs.execute('UPDATE Translate SET text = ? WHERE id = ?', (text, id))
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Update error: {err}")

    def deleteTranslate(self, id)  -> None:
        """
            Delete Row
        """

        try:
           self.curs.execute('DELETE FROM Translate WHERE id = ?', (id))
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Delete error: {err}")        

    def changeWindow(self) -> None:
        """
            Change the window to "saved translations", or back to translator
        """
        
        if self.ui.stackedWidget.currentIndex() == 0:
            
            self.renderSavedTable()
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
