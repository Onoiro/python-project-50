#!/usr/bin/env python3

import argparse
import json
import yaml
from yaml.loader import SafeLoader
from gendiff.format_diff import format_diff
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    if args.first_file[-4:] == 'json' and args.second_file[-4:] == 'json':
        arg1 = json.load(open(args.first_file))
        arg2 = json.load(open(args.second_file))
    else:
        with open(args.first_file) as f:
            arg1 = yaml.load(f, Loader=SafeLoader)
        with open(args.second_file) as f:
            arg2 = yaml.load(f, Loader=SafeLoader)
    diff_list = generate_diff(arg1, arg2)
    print(format_diff(diff_list))


if __name__ == '__main__':
    main()
