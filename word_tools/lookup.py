from bs4 import BeautifulSoup
import requests


def url_to_soup(url):
    response = requests.get(url)
    # If we encounter a 4xx, or 5xx response code something went wrong
    # Raise an exception. Let the caller determine how to handle it.
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def urban_dictionary(word, limit=0):
    '''
    Return a list of definitions of 'word' from UrbanDictionary,
    up to 'limit' results returned. A limit of 0 will return all
    results, a negative limit will return the top single result,
    any other positive integer will return up to that many results.

    Raises exception through 'requests' upon HTTP-related errors.
    TODO: Document which exceptions

    There is no safety-check on input. Use with caution. Can this even
    be exploited? Figure that out.
    '''
    soup = url_to_soup(f'https://www.urbandictionary.com/define.php?term={word}')
    for meaning in soup.find_all('div', class_='meaning', limit=limit):
        yield meaning.get_text()


def merriam_webster(word, limit=0):
    '''
    Return a list of definitions of 'word' from Merriam-Webster,
    up to 'limit' results returned. A limit of 0 will return all
    results, a negative limit will return the top single result,
    any other positive integer will return up to that many results.

    Raises exception through 'requests' upon HTTP-related errors.
    TODO: Document which exceptions

    There is no safety-check on input. Use with caution. Can this even
    be exploited? Figure that out.

    '''
    soup = url_to_soup(f'http://www.merriam-webster.com/dictionary/{word}')
    for definition in soup.find_all('span', class_='dt', limit=limit):
        yield definition.get_text()[2:].capitalize()


if __name__ == '__main__':
    # Define a helper function to test each lookup function
    def test_lookup(func, word, limit):
        print(func.__name__)
        result = func(word, limit)
        total = len(result)
        for value in result:
            print(value)
            print('----')
        print(f'{total} results ({word}, {limit})')

    # Test the lookup functions using the above. Good work.
    test_lookup(urban_dictionary, 'python', 2)
    print('') # Newline
    test_lookup(merriam_webster, 'python', 2)
