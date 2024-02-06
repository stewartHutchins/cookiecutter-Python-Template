from argparse import ArgumentParser

import pytest

from {{cookiecutter.package_name}}.args import create_arg_parser


@pytest.fixture(name="arg_parser")
def arg_parser_fixture() -> ArgumentParser:
    return create_arg_parser()
