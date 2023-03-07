#!/usr/bin/env python3

import argparse
import json
import yaml
from yaml.loader import SafeLoader
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json_format
from gendiff.gendiff import generate_diff
from gendiff.gendiff import get_parsed_data


def main():
    data1, data2, format_type = get_parsed_data()
    diff_list = generate_diff(arg1, arg2)
    if format_type == "stylish":
        print(get_stylish(diff_list))
    if format_type == "plain":
        print(get_plain(diff_list))
    if format_type == "json":
        print(get_json_format(diff_list))


if __name__ == '__main__':
    main()
