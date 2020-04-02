from .lookup_provider import LookupProvider


class UrbanProvider(LookupProvider):
    def lookup(self, word, limit=0):
        soup = self.url_to_soup(
                f'https://www.urbandictionary.com/define.php?term={word}'
            )
        for meaning in soup.find_all('div', class_='meaning', limit=limit):
            yield meaning.get_text()


class UrbanBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self):
        if not self._instance:
            self._instance = UrbanProvider()
        return self._instance
