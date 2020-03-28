# Contributing
Thank you for your interest in contributing to `word_tools`! In order to
help you contribute, and to help me bring your changes into `word_tools`. I
ask that you please keep these guidelines in mind when submitting your work.

This document covers far more ground than originally planned. It is meant to
function as an overview of our standard development process, and guidelines.
This is not meant to be a solid, strict set of rules to follow. But more an
introduction and overview of how to best contribute to this project.

#### TODO: How about a table of contents, or directory listing?

## How do I submit ..?

**Pull request**
  - The pull request template has not yet been completed. However, I would
  ask that pull requests be based into topic branches following the suggestions
  detailed below. Please also include a description of your changes, if they
  have been tested, and the reasoning behind your changes.
  - [How to submit a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)

**Bug report**
  - The suggested format for submitting a bug report is detailed in the issue
  template. While not a strict guideline, following it's format will ease the
  work towards resolving the issue. The more information you can include
  relevant to the issue, the better.
  - [Submit bug report](https://github.com/ncdulo/word_tools/issues/new?assignees=ncdulo&labels=bug&template=bug-report.md&title=%5BBUG%5D)

**Feature request**
  - The suggested format for submitting a feature request is detailed in the
  issue template. While not a strict guideline, following it's format will
  help us more clearly understand what you are looking for. Please be clear
  in the feature, when possible. Like above, the more detailed a description
  of the feature, the better.
  - [Submit feature request](https://github.com/ncdulo/word_tools/issues/new?assignees=ncdulo&labels=enhancement&template=feature-request.md&title=%5BFeature+Request%5D)

**General discussion**
  - Any general comments, questions, concerns, criticism, or praise can be
  directed towards our issue board. Just create a new issue, and speak your
  mind. Just include the 'Discussion' tag on the issue so it is clear your
  intention.
  - [Speak your mind](https://github.com/ncdulo/word_tools/issues/new?assignees=&labels=discussion&template=blank.md&title=%5BDiscussion%5D)

## Development
This section assumes you have a prior knowledge of Python, virtual
environments, and utilizing tools such as `pytest` and `setuptools`. I do my
best to explain the structure and setup of the development environment.

For now, this is not as fleshed out as I would like it to be. Due to the very
early status of this project, and the fact that it can still rapidly change,
I will keep this relatively simple.

### Code style
This project attempts to follow the [PEP 8](https://pep8.org/) source code
formatting conventions and guidelines. At the time of this writing (Mar 2020),
there is no enforcement and several source files are not in compliance. This
is remedied currently by running periodic compliance checks where I simply
run `pep8/flake8`, fix the issues and commit.

This loose enforcement helps me to develop without being hung up on formatting
issues that appear at the wrong time. As long as you keep the guidelines in
mind while you develop, there should be no issues. If the formatting is very
far off, I may ask you to revise the code before it can be merged. For simple
issues like extra newlines, I have no problem correcting it as part of the
period checks I run.

Worth noting that I have been considering adding a `flake8` git hook into this
repoository. That would implement a more strict approach to following Pep 8
conventions. The idea is still being debated thus discussion is welcome.

### Commit messages
The commit message is key towards maintaining a complete development history.
This is something important to me, so I ask that you include at least a
sentence or two describing the changes. The message doesn't need to break
everything down line by line. But should provide enough of a summary that
the commit's purpose can be discerned by reading the `git log` entry.

### Branches
Taking advantage of git's ability to utilize globbing, and of working with
branches in general, I try to keep the bulk of work on topic branches. What
this means is that features, bug fixes, documentation, and just about
everything else should be committed into a branch. This allows development
work to remain separate from `master`, and allows for a more complete history
when looking back in time. It also allows for greater control over how the
source code is applied, or otherwise worked with.

Most of the topic branches can fall into one of two categories -- features,
and issues. Thus, I split development up into branches following either
`feature/*` or `issue/<issue_number>` formats. Minor changes that don't fit
into a dedicated stage of work may go directly to master. This includes things
such as README updates, or version number increments. May also include minor
tweaks or bug fixes to the code that may not warrant opening a full issue on
GitHub.

If you are working towards a feature, or bug fix, please follow the branch
naming conventions. This makes work either for everyone involved.

### Environment setup
It is currently recommended to use `virtualenvwrapper` for managing your venvs
however whichever solution you prefer is perfectly fine. Generally, you will
want to clone into the repo, then set up your virtual environment and activate
it. You will also want to update your modules, and install a couple extras.
```bash
# Initial bootstrap
git clone https://github.com/ncdulo/word_tools.git
cd word_tools
mkvirtualenv -a /full/path/to/repo word_tools_dev

# Update pip and setuptools
pip install -U pip
pip install -U setuptools

# Install package (do this in a venv!)
pip install --editable .
# To install the same versions as master development environment
pip install -r requirements_dev.txt

# Otherwise install packages as specified below..

# Running unit tests
pip install pytest
# If you will be testing TravisCI locally
pip install pycov codecov
# If you will be creating packages, or uploading to PyPi
pip install wheel
pip install twine

# Executables will be located in..
/path/to/virtual/env/bin/wt.*
# Default location with virtualenvwrapper is
~/.virtualenvs/word_tools_dev/wt.*
```
### Project structure
At first glance, things can be a bit confusing or hard to find. Familiarity
with similar projects will help. Some of us need a little direction, such as
myself. I've laid out a short run-down of the repo structure to help you get
your bearings.

This file heirarchy is based off of a freshly cloned repository, with some
additions to reflect paths that may be created during development. Those
added paths are denoted by an `*`.
```bash
$ tree -da word_tools
word_tools
├── *build      # Build files generated by `setup.py`
├── *dist       # Packages generated by `setup.py`
├── .git
│   └── hooks   # Git Hooks may be coming soon (flake8, etc)
├── .github     # GitHub specific files
│   └── ISSUE_TEMPLATE
├── tests       # Unit tests (and maybe integration tests someday)
├── word_tools  # Module sources
│   └── cli     # CLI submodule
└── *word_tools.egg-info    # Generated during `pip install`
```

## In conclusion
I very much appreciate, and thank you for wanting to contribue. And I thank
for taking the time to read these guidelines. Feel free to fork, contribute,
or otherwise enjoy this software! Much work and care has gone into putting
`word_tools` together, I hope you can find use in it!
