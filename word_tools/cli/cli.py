import click

from word_tools import lookup


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


def main():
    lookup_urban('python', 2)
    lookup_merriam('python', 2)
