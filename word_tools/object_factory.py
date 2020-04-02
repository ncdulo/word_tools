class ObjectFactory:
    '''Generic object factory. Maintains a dictionary of provider objects,
    which can be created and returned on demand.
    '''
    def __init__(self):
        self._providers = {}

    def register_provider(self, key, provider):
        '''Register a new provider for future use. The `key` value is case-
        insensitive. `provider` is a callable object which returns an
        instance of the class associated with `key`.
        '''
        self._providers[key.lower()] = provider

    def create(self, key, **kwargs):
        '''Call a provider builder, and return the instance created. The
        provider builder is determined based on the `key` provided, and
        it will be called with `**kwargs` passed in to it.
        '''
        provider = self._providers.get(key.lower())
        if not provider:
            raise ValueError(key)
        return provider(**kwargs)
