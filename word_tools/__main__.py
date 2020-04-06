'''
Main entry point of word_tools CLI mode
'''
import sys
import click

import word_tools


def display_results(results):
    for index, result in enumerate(results, start=1):
        print('')
        print(f'{index}: {result}')


@click.command()
@click.argument('provider')
@click.option('-l', '--limit', default=0, type=int)
@click.argument('word')
def main(provider, word, limit):
    # This can be done so much better, I'm sure. Have not determined
    # exactly how, just yet.

    # TODO: I think we can do this better by placing all providers into
    # `word_tools.providers.get(KEY)` and then using the actual provider's
    # `__call__` method to perform the lookup/transform.
    try:
        main_prov = word_tools.lookup.get(provider)
        display_results(main_prov.lookup(word, limit))
    except ValueError:
        try:
            main_prov = word_tools.transform.get(provider)
            print(main_prov.convert(word))
        except ValueError:
            print(f'Error: provider ({provider}) specified was not found!')
            print('Please check the spelling and try again.')


# This isn't really needed. Extra bit of sanity checking.
if __name__ == '__main__':
    main()
