from .generic_provider import GenericProvider

from abc import ABCMeta, abstractmethod


class TransformProvider(GenericProvider):
    @abstractmethod
    def convert(self, word, extra=None):
        pass
