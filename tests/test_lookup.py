import word_tools

from bs4 import BeautifulSoup
import requests

import pytest


def test_url_to_soup():
    '''
    Assert that when given a url, we receive soup.
    '''
    provider = word_tools.LookupProvider()
    url = 'http://www.google.com/'
    assert (provider.url_to_soup(url)).__class__ == \
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
    provider = word_tools.LookupProvider()
    for url in urls:
        pytest.raises(requests.HTTPError,
                      provider.url_to_soup,
                      url)


def test_lookup_limit():
    '''
    Assert we receive a StopIteration exception when reaching past limit.
    '''
    urban = word_tools.lookup.get('urbandictionary')
    merriam = word_tools.lookup.get('merriamwebster')
    #wikipedia = word_tools.lookup.get('wikipedia')
    lookup_funcs = {
            urban.lookup: 1,
            merriam.lookup: 3,
            #wikipedia.lookup: 10,
        }
    # TODO: Handle 'limit=0' -- all results to be returned.
    # I was working to test that case in this commit, but it was proving
    # to be much harder than I anticipated. One thing we need to account
    # for in this case -- how many results does the API return per page.
    # Being that we only grab from the first page of results, we need
    # to make sure we aren't grabbing more than what's on the page.
    # Otherwise, the 'limit' wont match real results, and the test will
    # be invalid.

    # For each function in our list of functions
    for func, limit in lookup_funcs.items():
        # Call the function, then loop over it 'limit' times
        # to ensure we receive a StopIteration on the final call.
        result = func('python', limit)
        while limit >= 0:
            # Check if we have reached the end of 'limit', if so,
            # grab one more result and ensure we receive StopIteration.
            if limit == 0:
                pytest.raises(StopIteration, result.__next__)
            else:
                result.__next__()
            limit = limit - 1


def test_urban_dictionary():
    '''
    Assert we recieve valid results from Urban Dictionary.
    '''
    urban = word_tools.lookup.get('urbandictionary')
    words = {
            'phate': [2, 'Gosu', 'predetermines', ],
            'python': [3, 'interpreted', 'algorithms', 'Hogan', ],
            'unit test': [1, 'package', ],
        }

    for word, fragments in words.items():
        results = urban.lookup(word, fragments[0])
        for index, result in enumerate(results, start=1):
            assert fragments[index] in result


def test_merriam_webster():
    '''
    Assert we recieve valid results from Merriam-Webster's Dictionary.
    '''
    merriam = word_tools.lookup.get('merriamwebster')
    words = {
            'python': [2, 'constricting', 'wrapping', ],
            'functional': [3, 'connected', 'organic', 'development', ],
            'hacker': [1, 'One that hacks', ],
        }

    for word, fragments in words.items():
        results = merriam.lookup(word, fragments[0])
        for index, result in enumerate(results, start=1):
            assert fragments[index] in result


# Issue #2 -- intermittent failure when wikipedia search results re-order
# This will extend to the other lookup providers above, should their
# results re-order as well.
#
# Planned fix is pending a refactor of `word_tools.lookup`, and re-write
# of this test.
@pytest.mark.xfail()
def test_wikipedia():
    '''
    Assert we recieve valid results from Wikipedia.
    '''
    wiki = word_tools.lookup.get('wikipedia')
    words = {
            'fraction': [2, 'common usage', 'number of equal parts', ],
            'vim': [3, 'Bill Joy', 'Vimentin', 'VIM Airlines', ],
            'linux': [1, 'open source Unix-like operating system', ],
        }

    for word, fragments in words.items():
        results = wiki.lookup(word, fragments[0])
        for index, result in enumerate(results, start=1):
            assert fragments[index] in result[1]
