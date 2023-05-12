# 
import requests
from requests.exceptions import HTTPError
from classes.logger import *
from classes.translate.TranslationResources.googleTranslateLanguages import *
from classes.translate.TranslationResources.deeplTranslateLanguages import *


class LoadingLangs():
    """
        Load lang
    """

    def __init__(self, ui):
        self.ui = ui
        self.loadLangArrays()
        
    def chooseTranslator(self, event):
        """
            Choose the translaor
        """
        translators = ['Google', 'Deepl']
        self.loadLangArrays(event.text())
        
    def loadLangArrays(self, translator = 'Google') -> None:
        """
            Change of translator and loading of language arrays
        """

        languageValues = []

        match translator:
            case 'Google':
                languageValues = list(googleLanguages.values())
            case 'Deepl':
                languageValues = list(deeplLanguages.values())
        
        self.ui.fromLang.clear()
        self.ui.toLang.clear()

        self.ui.fromLang.addItems(languageValues)
        self.ui.fromLang.setCurrentIndex(languageValues.index('English'))
        
        self.ui.toLang.addItems(languageValues)
        self.ui.toLang.model().item(0).setEnabled(False)
        self.ui.toLang.setCurrentIndex(languageValues.index('Russian'))

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
