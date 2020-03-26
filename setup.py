from setuptools import setup


setup(
        name='word_tools',
        version='0.0.1',
        py_modules=['cli'],
        install_requires=[
            'requests',
            'click',
            'bs4',
        ],
        entry_points = {
                'console_scripts':
                    ['wt.urban=word_tools.cli.cli:lookup_urban',
                    'wt.merriam=word_tools.cli.cli:lookup_merriam',
                    'wt.wikipedia=word_tools.cli.cli:lookup_wikipedia',
                    'wt.stoopid=word_tools.cli.cli:transform_stoopid',],
            }
    )
