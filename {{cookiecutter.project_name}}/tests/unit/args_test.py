from argparse import ArgumentParser

import pytest

from {{cookiecutter.package_name}}.args import create_arg_parser


@pytest.fixture
def argparser() -> ArgumentParser:
    return create_arg_parser()
