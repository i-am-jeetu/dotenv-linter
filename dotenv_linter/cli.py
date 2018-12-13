
# -*- coding: utf-8 -*-

"""
Usage
=====

Command reference
-----------------

.. click:: dotenv_linter.cli:main
  :prog: dotenv-linter
  :show-nested:

"""

# See also:
# https://click.palletsprojects.com/en/7.x/setuptools/#setuptools-integration
# https://click.palletsprojects.com/en/7.x/arguments/

from typing import NoReturn, Tuple

import click

from dotenv_linter.checker import DotenvFileChecker


@click.command()
@click.argument(
    'files',
    nargs=-1,
    required=True,
    type=click.Path(exists=True, dir_okay=False),
)
def main(files: Tuple[str, ...]) -> NoReturn:
    """Runs linting process for the given files."""
    checker = DotenvFileChecker(files)
    error_message = None
    try:
        checker.run()
    except Exception as ex:
        error_message = str(ex)
    finally:
        checker.finish(message=error_message)
