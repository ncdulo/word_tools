from .generic_provider import GenericProvider

from abc import ABCMeta, abstractmethod

from bs4 import BeautifulSoup
import requests

class LookupProvider(GenericProvider):
    @abstractmethod
    def lookup(self, url, limit):
        pass

    def url_to_soup(self, url):
        response = requests.get(url)
        # If we encounter a 4xx, or 5xx response code something went wrong
        # Raise an exception. Let the caller determine how to handle it.
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
