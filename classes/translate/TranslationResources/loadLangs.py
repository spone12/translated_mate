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
        if not event.isChecked():
            event.setChecked(True)
            return

        # Remove active translators     
        for i in self.ui.chooseTranslator.actions():
            if i.text() != event.text() and i.isChecked():
                i.setChecked(False)

        self.ui.currentTranslator = event.text()
        self.loadLangArrays(event.text())
        
    def loadLangArrays(self, translator = 'Deepl') -> None:
        """
            Change of translator and loading of language arrays
        """

        languageValues = []

        self.ui.fromLang.clear()
        self.ui.toLang.clear()
        
        match translator:
            case 'Google':
                languageValues = list(googleLanguages.values())
            case 'Deepl':
                languageValues = list(deeplLanguages.values())

        self.ui.fromLang.addItems(languageValues)
        self.ui.fromLang.setCurrentIndex(languageValues.index('English'))
        
        self.ui.toLang.addItems(languageValues)
        
        if translator == 'Google':
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
