from hello_cli.cli import parse_args

def main() -> int:
    args = parse_args()
    print(args)
    return 0


if __name__ == "__main__":
    exit(main())
