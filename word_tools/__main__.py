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
@click.argument('word')
def main(provider, word):
    # How would we inject custom arguments for unit tests?
    #if args is None:
    #    args = sys.argv[1:]
    print('we got word_tools!')
    print(f'provider: {provider}')
    print(f'word: {word}')

    # Differentiate between a lookup or transform, or any other provider
    # type

    # Create the provider object accordingly

    # Run it's action function (convert/lookup)

    # Loop over result(s)


# This isn't really needed. Extra bit of sanity checking.
if __name__ == '__main__':
    main()
