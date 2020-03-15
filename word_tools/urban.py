from bs4 import BeautifulSoup
import requests

def lookup(word, limit=0):
    '''
    Return a list of definitions of 'word' from UrbanDictionary,
    up to 'limit' results returned. A limit <= 0 will return
    all results.

    Raises exception through 'requests' upon HTTP-related errors.
    TODO: Document which exceptions

    There is no safety-check on input. Use with caution. Can this even
    be exploited? Figure that out.
    '''
    url = f'https://www.urbandictionary.com/define.php?term={word}'
    response = requests.get(url)
    result = []

    # If we encounter a 4xx, or 5xx response code something went wrong
    # Raise an exception. Let the caller determine how to handle it.
    response.raise_for_status()

    # Make some soup, look for meaning within ourself.
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='meaning')

    # TODO: The below can be greatly cleaned up, I feel. Try using
    # list slicing along with the limit to eliminate that for loop

    # If limit is not a positive integer, return everything
    if limit <= 0:
        limit = len(results)

    for index,meaning in enumerate(results):
        if index >= limit:
            break
        result.append(meaning.get_text())

    return result


if __name__ == '__main__':
    urbanize_me = lookup('python', 3)

    total = len(urbanize_me)
    for meaning in urbanize_me:
        print(meaning)
        print(' - - - -')

    print(f'Returned {total} results')
