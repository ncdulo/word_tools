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
    Assert that url_to_soup throws an HTTPError when returning a bad request.
    '''
    urls = [
            'https://httpstat.us/401',  # Unauthorized
            'https://httpstat.us/404',  # Not Found
            'https://httpstat.us/503',  # Service Unavailable
        ]

    for url in urls:
        pytest.raises(requests.HTTPError,
                lookup.url_to_soup,
                url)

def test_lookup_limit():
    '''
    Assert we receive a StopIteration exception when reaching past limit.
    '''
    assert 1 == 0


def test_urban_dictionary():
    '''
    Assert we recieve valid results from Urban Dictionary.
    '''
    words = {
            'phate': [2, 'Gosu', 'predetermines',],
            'python': [3, 'interpreted', 'algorithms', 'Hogan',],
            'unit test': [1, 'package',],
        }

    for word,fragments in words.items():
        results = lookup.urban_dictionary(word, fragments[0])
        for index,result in enumerate(results,start=1):
            assert fragments[index] in result


def test_merriam_webster():
    '''
    Assert we recieve valid results from Merriam-Webster's Dictionary.
    '''
    words = {
            'python': [2, 'constricting', 'wrapping',],
            'functional': [3, 'connected', 'organic', 'development',],
            'hacker': [1, 'One that hacks',],
        }

    for word,fragments in words.items():
        results = lookup.merriam_webster(word, fragments[0])
        for index,result in enumerate(results,start=1):
            assert fragments[index] in result


def test_wikipedia():
    '''
    Assert we recieve valid results from Wikipedia.
    '''
    words = {
            'python': [2, 'Guido', 'sketch comedy',],
            'vim': [3, 'Bill Joy', 'Vimentin', 'VIM Airlines',],
            'linux': [1, 'open source Unix-like operating system',],
        }

    for word,fragments in words.items():
        results = lookup.wikipedia(word, fragments[0])
        for index,result in enumerate(results,start=1):
            assert fragments[index] in result[1]
