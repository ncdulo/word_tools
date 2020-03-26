from word_tools import transform

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

    for word,result in known_values:
        assert transform.stoopid(word) == result
    # TODO: This should also check functionality of the `extra` output.


def test_stoopid_bad_input():
    '''
    Assert stoopid fails when given bad input words
    '''
    pass
