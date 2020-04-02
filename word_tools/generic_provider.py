from .object_factory import ObjectFactory


class GenericProvider(ObjectFactory):
    def get(self, provider_id, **kwargs):
        return self.create(provider_id, **kwargs)
