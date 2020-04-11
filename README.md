# word_tools
[![PyPI version shields.io](https://img.shields.io/pypi/v/word_tools.svg)](https://pypi.python.org/pypi/word_tools/) [![PyPI status](https://img.shields.io/pypi/status/word_tools.svg)](https://pypi.python.org/pypi/word_tools/) [![Build Status](https://travis-ci.com/ncdulo/word_tools.svg?branch=master)](https://travis-ci.com/ncdulo/word_tools) [![codecov](https://codecov.io/gh/ncdulo/word_tools/branch/master/graph/badge.svg)](https://codecov.io/gh/ncdulo/word_tools) [![Percentage of issues still open](http://isitmaintained.com/badge/open/ncdulo/word_tools.svg)](http://isitmaintained.com/project/ncdulo/word_tools "Percentage of issues still open") [![PyPI pyversions](https://img.shields.io/pypi/pyversions/word_tools.svg)](https://pypi.python.org/pypi/word_tools/) [![Feature Request](https://img.shields.io/badge/feature%20requests-welcome-green.svg)](https://github.com/ncdulo/word_tools/issues/new/choose) [![made-with-vim](https://img.shields.io/badge/made%20with-Vim-1f425f.svg)](https://www.vim.org/)

Utilities for performing actions on words, or collections of words. This is a
slowly expanding library of functions, conversions, and lookups added to as I
see fit. Mostly intended for fun, or convenience. Not sure what it will grow
into, but it's a nice laid back project.

We are most in need of ideas for new providers! What can `word_tools` do for
*you*?

Note that many of the things in this repo, and in the code are a little out of
proportion compared to what the code actually does. That is perfectly fine. I
set up a lot of these extra features, simply to try them out. Having had an
interest in them for some time but never actually using them. Bringing us to
basically the same purpose behind this project. To expand my knowledge, and
grow further as a developer. Also, I just *really* like the badges.

# Requirements
Direct dependencies of this project are `requests`, `beautifulsoup4`, `click`,
`pymediawiki`, and their dependencies. If installing through Pip, or
`setup.py`, they will be installed automatically. A `requirements{,_dev}.txt`
files have been included for a more exact listing of the full requirements,
and their version numbers. However, there may be some issues with version
numbers on a couple packages that I have not fully worked out yet. The pip
and `setup.py` installation should not encounter these version mismatches.

# Installation & Use
Recommended to install into a virtual environment of your desired flavor. I
currently recommend `virtualenvwrapper`, but am using the stock `venv` module
in the example below for simplicity. Save the user on configuring a dependency
if they don't have to. If using another method to handle your venvs, modify
the below to suit.

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

# With venv active, the executable location will be included in your $PATH
# Otherwise, the path to executable will be
# .env/bin/wt
wt [OPTIONS] PROVIDER WORD
wt --help
wt urbandictionary python --limit 2
wt -l 2 wikipedia python

# Deactivate the virtual environment when finished
deactivate
```

# Contributing
Contributions to `word_tools` are always very welcome, and very much
appreciated. Thank you for the interest in helping out! There are a few
guidelines that I try to follow when working on this project. Laid out in the
[CONTRIBUTING.md](https://github.com/ncdulo/word_tools/blob/master/CONTRIBUTING.md)
file. I admit that I got a little carried away when writing it, and it looks
for worse than it actually is. Simply, they are just guidelines. I tried to
include the relevant information to get a development environment set up,
a breakdown of the project structure, and some basic conventions for coding
and submitting your content.

tldr: If you are only submitting an issue of some sort, or a small change, you
only need look into the very first section of the
[contributing guidelines](https://github.com/ncdulo/word_tools/blob/master/CONTRIBUTING.md).

# Development Goals
This project does not have a strict end-game in sight. It's just something I
have been putting together during my free time, in sporadic bursts of interst.
There are some additions that I have in mind, but in general, it is very
open-ended. Some of these features, or things I would like to learn with this
project include:
- [ ] Additional Providers
  - [ ] Thesaurus Lookup.
  - [ ] StackOverflow Search.
  - [ ] GitHub Search.
- [ ] Testing
  - [ ] Integration tests.
  - [ ] More testing specific to core classes (`GenericProvider`,
  `ObjectFactory`, etc).
  - [ ] Parametrize current tests. Eliminate some of those loops.
  - [ ] Are fixtures applicable anywhere?
- [ ] Command Line Interface
  - [ ] Finalize argument specification.
  - [ ] Tidy up, verbose-ify `--help` text.
- [ ] Documentation
  - [ ] Write API docs. Probably Sphinx.
  - [ ] We're gonna need a `man` page too.
  - [ ] Go all in with `readthedocs.io` support as well?

In the end, this is just something that I intend to grow over time. Trying
out new things as I learn them. Or adding other features as I think them up,
or find a need for them. So far, it's been a lot of fun, and I have had the
opportunity to try many new things on my own. 10/10, would `wt` again.
