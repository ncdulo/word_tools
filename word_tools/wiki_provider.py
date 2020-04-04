from .lookup_provider import LookupProvider

from mediawiki import MediaWiki

class WikiProvider(LookupProvider):
    '''Concrete provider which provides web results from Wikipedia.
    '''
    def __init__(self):
        self._wiki = MediaWiki(user_agent= \
            "word_tools (https://github.com/ncdulo/word_tools")
        LookupProvider.__init__(self)

    def lookup(self, word, limit=1):
        for result in self._wiki.opensearch(word, results=limit):
            title, _, url = result
            summary = self._wiki.page(title).summarize(chars=200)
            output = title + ' (' + url + ')\n' + summary
            yield output

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
