# word_tools [![Build Status](https://travis-ci.com/ncdulo/word_tools.svg?branch=master)](https://travis-ci.com/ncdulo/word_tools) [![codecov](https://codecov.io/gh/ncdulo/word_tools/branch/master/graph/badge.svg)](https://codecov.io/gh/ncdulo/word_tools)
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
