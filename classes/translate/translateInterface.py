# Main Interface translations API
from abc import ABC, ABCMeta, abstractmethod


class TranslateInterface(ABC):

    @abstractmethod
    def translate(self, text, toLang, fromLang=''): raise NotImplementedError

    @abstractmethod
    def translateIternal(self, formatedUrl): raise NotImplementedError

