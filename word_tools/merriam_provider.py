from .lookup_provider import LookupProvider


class MerriamProvider(LookupProvider):
    '''Concrete provider which provides web results from Merriam-Webster
    dictionary.
    '''
    def lookup(self, word, limit=0):
        '''Yield str results for `word` up to `limit`. When `limit == 0`,
        return all results. These results will be limited to the first
        page only. We do not search further back.
        '''
        soup = self.url_to_soup(
                f'http://www.merriam-webster.com/dictionary/{word}'
            )
        for definition in soup.find_all('span', class_='dt', limit=limit):
            yield definition.get_text()[2:].capitalize()


class MerriamBuilder:
    '''Builder class which maintains a single instance of `MerriamProvider`,
    returning it when called, creating it if necessary.
    '''
    def __init__(self):
        self._instance = None

    def __call__(self):
        if not self._instance:
            self._instance = MerriamProvider()
        return self._instance
