from .lookup_provider import LookupProvider


class WikiProvider(LookupProvider):
    '''Concrete provider which provides web results from Wikipedia.
    '''
    def lookup(self, word, limit=0):
        return ['some', 'results', 'here']

class WikiBuilder:
    '''Builder class which maintains a single instance of `WikiProvider`,
    returning it when called, creating it if necessary.
    '''
    def __init__(self):
        self._instance = None

    def __call__(self):
        if not self._instance:
            self._instance = WikiProvider()
        return self._instance
