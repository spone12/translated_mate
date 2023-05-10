# 
import requests
from requests.exceptions import HTTPError
from classes.logger import *
from classes.translate.TranslationResources.googleTranslateLanguages import *


class Lang():
    """
        Load lang
    """

    def __init__(self, ui):
        self.ui = ui
        self.loadLangArrays()
        
    def loadLangArrays(self, translator = 'google') -> None:
        """
            Change of translator and loading of language arrays
        """

        languageValues = []

        match translator:
            case 'google':
                languageValues = list(googleLanguages.values())

        self.ui.fromLang.addItems(languageValues)
        self.ui.fromLang.setCurrentIndex(languageValues.index('English'))
        
        self.ui.toLang.addItems(languageValues)
        self.ui.toLang.model().item(0).setEnabled(False)
        self.ui.toLang.setCurrentIndex(languageValues.index('Russian'))
    
    def reverseTranslations(self, eve) -> None:
        """
            Flip the translations around
        """
        
        currentToIndex = self.ui.toLang.currentIndex()
        currentFromIndex = self.ui.fromLang.currentIndex()
        inputText = self.ui.inputBox.toHtml()
        translateBox = self.ui.translateBox.toHtml()
        
        self.ui.translateBox.clear()
        self.ui.inputBox.clear()
        self.ui.translateBox.insertHtml(inputText)
        self.ui.inputBox.insertHtml(translateBox)
        self.ui.toLang.setCurrentIndex(currentFromIndex)
        self.ui.fromLang.setCurrentIndex(currentToIndex)

    def getKeyLang(self, value) -> str:
        """
            Get country code by full language name
        """

        for k, v in googleLanguages.items():
            if (isinstance(v, list) and value in v) or value == v:
                return k
        else:
            Logger().log(self.__class__.__name__, f"Cant find language: {value}")
            return 'auto'
