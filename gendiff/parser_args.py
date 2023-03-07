import argparse
import json

def get_parsed_data():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    if args.first_file[-4:] == 'json' and args.second_file[-4:] == 'json':
        data1 = json.load(open(args.first_file))
        data2 = json.load(open(args.second_file))
    else:
        with open(args.first_file) as f:
            data1 = yaml.load(f, Loader=SafeLoader)
        with open(args.second_file) as f:
            data2 = yaml.load(f, Loader=SafeLoader)
    return data1, data2, args.format
