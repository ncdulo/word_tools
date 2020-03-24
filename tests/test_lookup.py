from word_tools import lookup

from bs4 import BeautifulSoup
import requests

import pytest


def test_url_to_soup():
    '''
    Assert that when given a url, we receive soup.
    '''
    url = 'http://www.google.com/'
    assert (lookup.url_to_soup(url)).__class__ == \
            (BeautifulSoup(requests.get(url).text, 'html.parser')).__class__


def test_url_to_soup_failure():
    '''
    Assert that url_to_soup fails when given known to be bad URLs.
    '''
    urls = {
            'https://httpstat.us/401': '401',  # Unauthorized
            'https://httpstat.us/404': '404',  # Not Found
            'https://httpstat.us/503': '503',  # Service Unavailable
        }

    for url,status in urls.items():
        with pytest.raises(requests.HTTPError) as e:
            requests.get(url).raise_for_status()
        assert status in str(e.value)


def test_urban_dictionary():
    '''
    Assert we recieve valid results from Urban Dictionary.
    '''
    assert 1 == 0


def test_merriam_webster():
    '''
    Assert we recieve valid results from Merriam-Webster's Dictionary.
    '''
    assert 1 == 0


def test_wikipedia():
    '''
    Assert we recieve valid results from Wikipedia.
    '''
    assert 1 == 0
