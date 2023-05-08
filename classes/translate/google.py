# Google translate
import requests
from bs4 import BeautifulSoup
import urllib.parse
from classes.translate.translateInterface import *


class Google(TranslateInterface):

    def translate(self, text, toLang, fromLang=''):

       _baseUrl = "https://translate.google.com/m?hl=ru&sl={}&tl={}&ie=UTF-8&prev=_m&q={}"
       formateUrl = _baseUrl.format(toLang, fromLang, urllib.parse.quote(text, safe=""))

       headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent':'Opera/9.80 (Android; Opera Mini/11.0.1912/37.7549; U; pl) Presto/2.12.423 Version/12.16',
            'Accept-Language': 'en-US;q=0.5,en;q=0.3',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
       }
       
       try:
           
          request = requests.get(formateUrl, headers=headers)
          answer = BeautifulSoup(request.text, 'html.parser')
          parse = answer.find('div', class_='result-container').text
          
          return parse
       except: 
          print('error')  
    
    def translateIternal(self, formatedUrl):
        pass