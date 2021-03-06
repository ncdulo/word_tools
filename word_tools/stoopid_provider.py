from .transform_provider import TransformProvider


class StoopidProvider(TransformProvider):
    def convert(self, word, extra=None):
        ''' Return a 'StUpId' rendition of word. Optional, `extra`argument to
        randomly flip case of a small proportion of letters after the first
        pass, for an 'EXtRa sTupID' final form.
        '''

        if not isinstance(word, str):
            raise TypeError(f'argument not recognized as string: {word}')

        new_word = ''
        for i, item in enumerate(word):
            if i % 2 == 0:
                new_word += item.upper()
            else:
                new_word += item.lower()

        if extra:
            # TODO: Extra pass, flipping a certain percentage of characters
            # and additional time.
            pass

        return new_word


class StoopidBuilder():
    '''Builder class which maintains a single instance of `StoopidProvider`,
    returning it when called, creating it if necessary.
    '''
    def __init__(self):
        self._instance = None

    def __call__(self):
        if not self._instance:
            self._instance = StoopidProvider()
        return self._instance
