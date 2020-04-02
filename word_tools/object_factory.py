class ObjectFactory:
    def __init__(self):
        self._providers = {}

    def register_provider(self, key, provider):
        self._providers[key.lower()] = provider

    def create(self, key, **kwargs):
        provider = self._providers.get(key.lower())
        if not provider:
            raise ValueError(key)
        return provider(**kwargs)
