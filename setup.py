import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
        name='word_tools',
        version='0.0.1',
        author='ncdulo',
        description='Utilities for performing actions on words, or collections of words.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/ncdulo/word_tools',
        packages=setuptools.find_packages(), # What does this do?
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independant',
            ],
        python_requires='>=3.6',
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
