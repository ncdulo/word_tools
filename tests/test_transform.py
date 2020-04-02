import word_tools

import pytest


def test_stoopid_output():
    '''
    Assert stupid provides the proper output
    '''
    known_values = (
            ('python', 'PyThOn'),
            ('word tools', 'WoRd tOoLs'),
            ('programming', 'PrOgRaMmInG'),
            ('try some longer output', 'TrY SoMe lOnGeR OuTpUt'),
            ('Example', 'ExAmPlE'),
            ('MiXeD', 'MiXeD'),
            ('sWoRdS', 'SwOrDs'),
            ('RUN LOW ON IDEAS', 'RuN LoW On iDeAs'),
            ('install gentoo.', 'InStAlL GeNtOo.'),
            ('Punc-tu-a-tion... Test!', 'PuNc-tU-A-TiOn... TeSt!'),
        )
    stoopid = word_tools.transform.get('stoopid')
    for word, result in known_values:
        assert stoopid.convert(word) == result
    # TODO: This should also check functionality of the `extra` output.


def test_stoopid_bad_input():
    '''
    Assert stoopid raises a TypeError when given bad input words
    '''
    bad_input = [
            12345,
            36.0,
            ['bad', 'inputs', ],
            {'key': 'value', },
            (1, 'two'),
        ]
    stoopid = word_tools.transform.get('stoopid')
    for arg in bad_input:
        pytest.raises(TypeError,
                      stoopid.convert,
                      arg)
