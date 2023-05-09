# 
import requests
from requests.exceptions import HTTPError
from classes.logger import *
from classes.translate.TranslationResources.googleTranslateLanguages import *


class Lang():
    """
        Load lang
    """

    def __init__(self, objectUi):
        self.objectUi = objectUi
        self.loadLangArrays()
        
    def loadLangArrays(self, translator = 'google') -> None:

        languageValues = []

        match translator:
            case 'google':
                languageValues = list(googleLanguages.values())


        self.objectUi.fromLang.addItems(languageValues)

        self.objectUi.fromLang.setCurrentText('Russian')
        languageValues.remove('Automatic')
        
        self.objectUi.toLang.addItems(languageValues)
    
    def getKeyLang(self, value):

        for k, v in googleLanguages.items():
            if (isinstance(v, list) and value in v) or value == v:
                return k
        else:
            Logger().log(self.__class__.__name__, f"Cant find language: {value}")

