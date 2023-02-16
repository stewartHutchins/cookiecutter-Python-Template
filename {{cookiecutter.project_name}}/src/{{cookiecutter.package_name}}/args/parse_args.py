from argparse import ArgumentParser


def create_arg_parser() -> ArgumentParser:
    """
    Create the argument parser for the program
    :return: The argument parser
    """
    parser = ArgumentParser(
        prog="{{cookiecutter.project_name}}", description="{{cookiecutter.description}}"
    )
    return parser
