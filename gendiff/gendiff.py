from gendiff.get_diff import get_diffs
from gendiff.file_reader import get_data
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json_format


def generate_diff(filepath1, filepath2, format_type="stylish"):
    dict1 = get_data(filepath1)
    dict2 = get_data(filepath2)
    diff_list = get_diffs(dict1, dict2)
    if format_type == "stylish":
        return get_stylish(diff_list)
    if format_type == "plain":
        return get_plain(diff_list)
    if format_type == "json":
        return get_json_format(diff_list)
