import click

from word_tools import lookup
from word_tools import transform


def display_results(results):
    for index, result in enumerate(results, start=1):
        print('')
        print(f'{index}: {result}')


@click.command()
@click.argument('word')
@click.argument('limit', default=0)
def lookup_merriam(word, limit):
    results = lookup.merriam_webster(word, limit)
    display_results(results)


@click.command()
@click.argument('word')
@click.argument('limit', default=0)
def lookup_urban(word, limit):
    results = lookup.urban_dictionary(word, limit)
    display_results(results)

@click.command()
@click.argument('word')
@click.argument('limit', default=0)
def lookup_wikipedia(word, limit):
    results = lookup.wikipedia(word, limit)
    display_results(results)

@click.command()
@click.argument('word')
# TODO: Properly implement extra-stoopid mode.
#@click.argument('extra', default=None)
def transform_stoopid(word):
    print(transform.stoopid(word))


def main():
    lookup_urban('python', 2)
    lookup_merriam('python', 2)
