from .lookup_provider import LookupProvider


class MerriamProvider(LookupProvider):
    def lookup(self, word, limit=0):
        soup = self.url_to_soup(
                f'http://www.merriam-webster.com/dictionary/{word}'
            )
        for definition in soup.find_all('span', class_='dt', limit=limit):
            yield definition.get_text()[2:].capitalize()


class MerriamBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self):
        if not self._instance:
            self._instance = MerriamProvider()
        return self._instance
