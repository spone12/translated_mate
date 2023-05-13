# Deepl translate
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import urllib.parse
from classes.translate.translateInterface import *
from classes.logger import *
import time
import math
from textwrap import wrap


class DeeplTranslator(TranslateInterface):
    """
        Deepl translate class
    """

    def translate(self, text: str, toLang: str, fromLang = 'auto') -> str:
        
        translatedText = ''
        return translatedText

    
    def translateIternal(self, formatedUrl: str):
        pass
