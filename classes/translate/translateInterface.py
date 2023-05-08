# Main Interface translations API
from abc import ABC, ABCMeta, abstractmethod


class TranslateInterface(ABC):

    @abstractmethod
    def translate(self, text: str, toLang: str, fromLang = '') -> str: raise NotImplementedError

    @abstractmethod
    def translateIternal(self, formatedUrl: str): raise NotImplementedError

