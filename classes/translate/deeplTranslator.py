# Deepl translate
import requests
from requests.exceptions import HTTPError
from classes.translate.translateInterface import *
from classes.logger import *
import time
import math
from textwrap import wrap
import random
import calendar
import json
import datetime


class DeeplTranslator(TranslateInterface):
    """
        Deepl translate class
    """

    deeplApiUrl = 'https://www2.deepl.com/jsonrpc'
    _DeepLId    = 0

    def translate(self, text: str, toLang: str, fromLang = 'auto') -> str:
        
        translatedText = ''
        self.generateDeeplId()
        translatedText = self.translateIternal(self.deeplApiUrl, text, toLang, fromLang)

        return translatedText

    def generateDeeplId(self) -> None:

        baseIdMult = 10000
        currentTime = time.strptime(str(datetime.datetime.now().time()).split('.')[0], '%H:%M:%S')
        totalSeconds = datetime.timedelta(
            hours   = currentTime.tm_hour,
            minutes = currentTime.tm_min,
            seconds = currentTime.tm_sec).total_seconds() * 1000
        Rnd = random.Random(totalSeconds)
        self._DeepLId = baseIdMult * round(baseIdMult * Rnd.random())
        

    def translateIternal(self, formatedUrl: str, text: str, toLang, fromLang) -> str:

        headers = {
            'Accept': '*/*',
            'Referer': 'https://www.deepl.com/translator',
            'Content-type': 'application/json',
            'Cache-Control': 'no-cache',
            'Accept-Language': 'en-US;q=0.5,en;q=0.3',
            'DNT': '1',
            'TE': 'Trailers'
        }

        body = {
            "id": self._DeepLId,
            "jsonrpc": "2.0",
            "method": "LMT_handle_jobs",
            "params": {
                "jobs": [
                    {
                        "kind": "default",
                        "preferred_num_beams": 4,
                        "quality": "fast",
                        "raw_en_context_after": [],
                        "raw_en_context_before": [],
                        "sentences": [
                            {
                                "id": 0,
                                "prefix": "",
                                "text": text
                            }
                        ]
                    }
                ],
                "lang": {
                    "source_lang_user_selected": fromLang.upper(),
                    "target_lang": toLang.upper()
                },
                "priority": -1,
                "timestamp": calendar.timegm(time.gmtime())
            }
        }

        parsedAnswer = ''

        try:
            request = requests.post(self.deeplApiUrl, data=json.dumps(body), headers = headers)
            request.raise_for_status()
        except HTTPError as http_err:
            Logger().log(self.__class__.__name__, f"HTTP error occurred: {http_err}")
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Other error occurred: {err}")
        else:

            anserDecode = json.loads(request.text)
            for item in anserDecode['result']['translations'][0]['beams']:
                parsedAnswer = item['sentences'][0]['text']
                break
        
        return parsedAnswer
