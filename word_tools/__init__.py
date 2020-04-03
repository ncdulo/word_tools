'''
`word_tools`

Utilities for performing actions on words, or collections of words.
----
This module provides acess to it's functions through an object
factory. To utilize a provider, you must create an instance of it
before calling it's activation functions. Two simple use cases are
laid out below for demonstration.

```
import word_tools

merriam = word_tools.lookup.get('merriamwebster')
limit = 2
hacker = merriam.lookup('hacker', limit)
for result in hacker:
    print(result)

stoopid = word_tools.transform.get('stoopid')
phrase = 'word_tools are best tools'
print(stoopid.convert(phrase))
```
'''

# This will be run if `import word_tools` is called, so we
# should import anything we want as part of the `word_tools`
# namespace here, or run any initialization code that may
# be required.

# Full setup of the module requires us to load our base providers
# and the builders used during registration.
from .lookup_provider import LookupProvider
from .transform_provider import TransformProvider
from .urban_provider import UrbanBuilder
from .merriam_provider import MerriamBuilder
from .stoopid_provider import StoopidBuilder


# When adding new submodules, or providers, follow the
# below format. Variables defined here will available in
# the `word_tools.<name>` format. Provider name argument
# is *not* case-sensitive.
lookup = LookupProvider()
lookup.register_provider('MerriamWebster', MerriamBuilder())
lookup.register_provider('UrbanDictionary', UrbanBuilder())

transform = TransformProvider()
transform.register_provider('Stoopid', StoopidBuilder())
