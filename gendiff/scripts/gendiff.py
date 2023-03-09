#!/usr/bin/env python3

from gendiff.gendiff import generate_diff
from gendiff.parser_args import get_parsed_data


def main():
    data1, data2, format_type = get_parsed_data()
    print(generate_diff(data1, data2, format_type))


if __name__ == '__main__':
    main()
