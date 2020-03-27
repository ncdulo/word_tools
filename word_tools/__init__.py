# This will be run if `import word_tools` is called, so we
# should import anything we want as part of the `word_tools`
# namespace here, or run any initialization code that may
# be required.
from .lookup import urban_dictionary, merriam_webster, wikipedia
from .transform import stoopid
