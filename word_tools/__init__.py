# This will be run if `import word_tools` is called, so we
# should import anything we want as part of the `word_tools`
# namespace here, or run any initialization code that may
# be required.

from .lookup_provider import LookupProvider
from .transform_provider import TransformProvider
from .urban_provider import UrbanBuilder
from .merriam_provider import MerriamBuilder
from .stoopid_provider import StoopidBuilder


lookup = LookupProvider()
lookup.register_provider('MerriamWebster', MerriamBuilder())
lookup.register_provider('UrbanDictionary', UrbanBuilder())

transform = TransformProvider()
transform.register_provider('Stoopid', StoopidBuilder())
