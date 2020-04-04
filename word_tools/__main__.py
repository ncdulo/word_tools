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


@click.group()
def main():
    # Is there anything we need to do here?
    # Probably a way to collect the provider, word, limit values
    # here and pass them along in a context. Or possibly a way to
    # determine the super-classes of provider to grab the proper
    # lookup or transform. Advanced stuff, filed under 'someday'.
    pass


@main.command()
@click.argument('provider')
@click.argument('word')
@click.argument('limit', default=0)
def lookup(provider, word, limit):
    provider = word_tools.lookup.get(provider)
    display_results(provider.lookup(word, limit))

@main.command()
@click.argument('provider')
@click.argument('word')
def transform(provider, word):
    provider = word_tools.transform.get(provider)
    result = provider.convert(word)
    print(result)


# This isn't really needed. Extra bit of sanity checking.
if __name__ == '__main__':
    main()
