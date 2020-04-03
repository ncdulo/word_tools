from .generic_provider import GenericProvider

from abc import abstractmethod


class TransformProvider(GenericProvider):
    '''Provides an interface to be implemented by the concrete providers.
    This class is not intended to be used directly by the user, but expanded
    upon for adding new providers which scrape web results.
    '''
    @abstractmethod
    def convert(self, word):
        '''Abstract method representing the concrete provider's implementation
        for transforming the input `word`.
        '''
        pass
