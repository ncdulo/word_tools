from word_tools import __main__


def test_display_results(capsys):
    '''
    Assert display_results properly outputs.
    '''
    # We must pass the result argument as a list, otherwise
    # the display loop will iterate over each character.
    __main__.display_results(['result one', 'another', ])
    capture = capsys.readouterr()
    assert capture.out == '\n1: result one\n\n2: another\n'
