from .object_factory import ObjectFactory


class GenericProvider(ObjectFactory):
    '''Generic interface to be used as a base class when creating new
    providers.
    '''
    def get(self, provider_id, **kwargs):
        '''Return an instance of the provider that is registered to
        this object.
        '''
        return self.create(provider_id, **kwargs)
