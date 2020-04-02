from .lookup_provider import LookupProvider


class UrbanProvider(LookupProvider):
    '''Concrete provider which provides web results from Urban Dictionary.
    '''
    def lookup(self, word, limit=0):
        '''Yield str results for `word` up to `limit`. When `limit == 0`,
        return all results. These results will be limited to the first
        page only. We do not search further back.
        '''
        soup = self.url_to_soup(
                f'https://www.urbandictionary.com/define.php?term={word}'
            )
        for meaning in soup.find_all('div', class_='meaning', limit=limit):
            yield meaning.get_text()


class UrbanBuilder:
    '''Builder class which maintains a single instance of `UrbanProvider`,
    returning it when called, creating it if necessary.
    '''
    def __init__(self):
        self._instance = None

    def __call__(self):
        if not self._instance:
            self._instance = UrbanProvider()
        return self._instance
