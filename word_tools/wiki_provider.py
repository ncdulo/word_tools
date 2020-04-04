from .lookup_provider import LookupProvider

from mediawiki import MediaWiki, exceptions

class WikiProvider(LookupProvider):
    '''Concrete provider which provides web results from Wikipedia.
    '''
    def __init__(self):
        self._wiki = MediaWiki(user_agent= \
            "word_tools (https://github.com/ncdulo/word_tools")
        LookupProvider.__init__(self)

    def lookup(self, word, limit=0):
        # Default to a limit of three results. Once the re-write of CLI
        # is complete, this should be updated, and likely removed
        if limit == 0:
            limit = 3

        try:
            for result in self._wiki.opensearch(word, results=limit):
                title, _, url = result
                summary = self._wiki.page(title).summarize(chars=200)
                output = title + ' (' + url + ')\n' + summary
                yield output
        except exceptions.DisambiguationError as e:
            print(
                '''Search term disambiguous. There are some issues in the way
results are returned. Wikipedia suggests the following page
names. These may not be correct. This is a known issue.
                ''')
            print(e)

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
