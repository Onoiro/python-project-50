from gendiff.get_diff import get_diffs
from gendiff.file_parser import get_dict
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json_format


def generate_diff(filepath1, filepath2, format_type="stylish"):
    data1 = get_dict(filepath1)
    data2 = get_dict(filepath2)
    diff_list = get_diffs(data1, data2)
    if format_type == "stylish":
        return get_stylish(diff_list)
    if format_type == "plain":
        return get_plain(diff_list)
    if format_type == "json":
        return get_json_format(diff_list)
