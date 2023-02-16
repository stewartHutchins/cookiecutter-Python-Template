from {{cookiecutter.package_name}}.args.parse_args import create_arg_parser


def main(args: list[str] | None = None) -> None:
    parser = create_arg_parser()
    _ = parser.parse_args(args)
    print("Hello World!")


if __name__ == "__main__":
    main()
