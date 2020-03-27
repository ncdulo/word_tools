from setuptools import setup,find_packages
from os import path

# Pull the current README
cwd = path.abspath(path.dirname(__file__))
with open(path.join(cwd, 'README.md'), 'r') as fh:
    long_description = fh.read()


setup(
        name='word_tools',
        packages=find_packages(), # What does this do?
        version='0.0.1',
        author='ncdulo',
        license='MIT',
        description='Utilities for performing actions on words, or collections of words.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/ncdulo/word_tools',
        keywords='word tools dictionary urbandictionary utility cli module',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Operating System :: POSIX :: Linux'
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Internet',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Text Processing',
            'Topic :: Text Processing :: Filters',
            'Topic :: Utilities',
            ],
        python_requires='>=3.6',
        py_modules=['cli'],
        install_requires=[
            'requests',
            'click',
            'beautifulsoup4',
        ],
        entry_points = {
                'console_scripts':
                    ['wt.urban=word_tools.cli.cli:lookup_urban',
                    'wt.merriam=word_tools.cli.cli:lookup_merriam',
                    'wt.wikipedia=word_tools.cli.cli:lookup_wikipedia',
                    'wt.stoopid=word_tools.cli.cli:transform_stoopid',],
            }
    )
