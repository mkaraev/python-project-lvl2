import argparse
from gendiff.render import json_renderer, plain_renderer, nested_renderer
from gendiff.gen_diff import generate_diff


def main():
    renderer_map = {
        "json": json_renderer,
        "plain": plain_renderer,
        "nested": nested_renderer
    }
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("before")
    parser.add_argument("after")
    parser.add_argument("-f", "--format",
                        dest="format",
                        help="set format of output",
                        default="nested"
                        )
    args = parser.parse_args()
    print(
        generate_diff(args.before, args.after, renderer_map[args.format])
    )


if __name__ == '__main__':
    main()
