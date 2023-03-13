#!/usr/bin/env python3

from gendiff.gendiff import generate_diff
from gendiff.parser_args import get_parsed_args


def main():
    filepath1, filepath2, format_type = get_parsed_args()
    print(generate_diff(filepath1, filepath2, format_type))


if __name__ == '__main__':
    main()
