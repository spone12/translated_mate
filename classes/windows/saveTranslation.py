# Save translation window
import sqlite3
from classes.logger import *


class SaveTranslationWindow():
    """
        Save translation window class
    """

    def __init__(self, ui):
        self.ui = ui
        self.db = sqlite3.connect('translate.db')
        self.curs = self.db.cursor()
        self.createTranslateTable()

    def __del__(self):
        self.db.commit()
        self.db.close()

    def createTranslateTable(self) -> None:
        self.curs.execute('''
            CREATE TABLE IF NOT EXISTS Translate (
                id INTEGER PRIMARY KEY,
                trans_from TEXT NOT NULL,
                trans_to TEXT NOT NULL,
                text TEXT NOT NULL,
                knowledge SMALLINT DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    
    def selectTranslate(self, where = None):
        """
            Select Row
        """

        try:
            sql = "SELECT * FROM Translate"
            
            if where is not None:
                sql += " WHERE id=" + where

            self.curs.execute(sql)
            return self.curs.fetchall()
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Select error: {err}")

    def insertTranslate(self, trans_from, trans_to, text, knowledge = 1)  -> None:
        """
            Insert Row
        """

        try:
            self.curs.execute('INSERT INTO Translate (trans_from, trans_to, text, knowledge) VALUES (?, ?, ?, ?)',
                (trans_from, trans_to, text, knowledge)
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
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
