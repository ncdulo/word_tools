# word_tools
[![PyPI version shields.io](https://img.shields.io/pypi/v/word_tools.svg)](https://pypi.python.org/pypi/word_tools/) [![PyPI status](https://img.shields.io/pypi/status/word_tools.svg)](https://pypi.python.org/pypi/word_tools/) [![Build Status](https://travis-ci.com/ncdulo/word_tools.svg?branch=master)](https://travis-ci.com/ncdulo/word_tools) [![codecov](https://codecov.io/gh/ncdulo/word_tools/branch/master/graph/badge.svg)](https://codecov.io/gh/ncdulo/word_tools) [![Percentage of issues still open](http://isitmaintained.com/badge/open/ncdulo/word_tools.svg)](http://isitmaintained.com/project/ncdulo/word_tools "Percentage of issues still open") [![PyPI pyversions](https://img.shields.io/pypi/pyversions/word_tools.svg)](https://pypi.python.org/pypi/word_tools/) [![Feature Request](https://img.shields.io/badge/feature%20requests-welcome-green.svg)](https://github.com/ncdulo/word_tools/issues/new/choose) [![made-with-vim](https://img.shields.io/badge/made%20with-Vim-1f425f.svg)](https://www.vim.org/)

Utilities for performing actions on words, or collections of words. This is a slowly
expanding library of functions, conversions, and lookups added to as I see fit.
Mostly intended for fun, or convenience. Not sure what it will grow into, but it's
a nice laid back project.

# Installation & Use
Recommended to install into a virtual environment of your desired flavor. I currently
recommend `virtualenvwrapper`, but am using the stock `venv` module in the example
below for simplicity. Save the user on configuring a dependency if they don't have to

```bash
# Clone the repo
git clone https://github.com/ncdulo/word_tools.git
cd word_tools

# Create a new virtual environment, and enable it
python -m venv .env
source .env/bin/activate

# Update Pip & friends. Optional, but recommended
pip install --upgrade pip

# Install dependencies and create executable
pip install .
# If you receive errors about "No module named 'word_tools'", try this
pip install --editable .

# With venv active, the path will already be in path
# Otherwise, the path to executables will be
# .env/bin/wt.{urban,merriam,wikipedia}
wt.urban WORD [LIMIT=0]
wt.merriam hacker 2
wt.wikipedia python 1

# Deactivate the virtual environment when finished
deactivate
