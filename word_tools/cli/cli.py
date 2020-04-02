import click

import word_tools


def display_results(results):
    for index, result in enumerate(results, start=1):
        print('')
        print(f'{index}: {result}')


@click.command()
@click.argument('word')
@click.argument('limit', default=0)
def lookup_merriam(word, limit):
    merriam = word_tools.lookup.get('merriamwebster')
    results = merriam.lookup(word, limit)
    display_results(results)


@click.command()
@click.argument('word')
@click.argument('limit', default=0)
def lookup_urban(word, limit):
    urban = word_tools.lookup.get('urbandictionary')
    results = urban.lookup(word, limit)
    display_results(results)


@click.command()
@click.argument('word')
@click.argument('limit', default=0)
def lookup_wikipedia(word, limit):
    wiki = word_tools.lookup.get('wikipedia')
    results = wiki.lookup(word, limit)
    display_results(results)


@click.command()
@click.argument('word')
# TODO: Properly implement extra-stoopid mode.
# @click.argument('extra', default=None)
def transform_stoopid(word):
    print(word_tools.stoopid(word))


def main():
    lookup_urban('python', 2)
    lookup_merriam('python', 2)
