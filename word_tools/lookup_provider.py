from .generic_provider import GenericProvider

from abc import abstractmethod
from bs4 import BeautifulSoup
import requests


class LookupProvider(GenericProvider):
    '''Provides an interface to be implemented by the concrete providers.
    This class is not intended to be used directly by the user, but expanded
    upon for adding new providers which scrape web results.
    '''

    # TODO: Below should be a `__call__` so that we can simplify calling
    # and make the CLI a little easier to work with. Need to put some thought
    # into how we do this, or if we should do this before making a final call.
    @abstractmethod
    def lookup(self, url, limit):
        '''Abstract method representing the concrete provider's implementation
        for returning results.
        '''
        pass

    def url_to_soup(self, url):
        '''Return a BeautifulSoup object when provided a URL. Raises
        exceptions upon bad requests. This is a helper function intended
        for use when a derived class implements their `lookup` method.
        '''
        response = requests.get(url)
        # If we encounter a 4xx, or 5xx response code something went wrong
        # Raise an exception. Let the caller determine how to handle it.
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
