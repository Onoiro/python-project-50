from gendiff.get_diff import get_diffs
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
import json
import yaml
from yaml.loader import SafeLoader
import pytest


with open('tests/fixtures/file1.json') as f:
    json_data_1 = json.load(f)
with open('tests/fixtures/file2.json') as f:
    json_data_2 = json.load(f)
with open('tests/fixtures/filepath1.yml') as f:
    yaml_data_1 = yaml.load(f, Loader=SafeLoader)
with open('tests/fixtures/filepath2.yml') as f:
    yaml_data_2 = yaml.load(f, Loader=SafeLoader)
with open('tests/fixtures/file3.json') as f:
    json_data_3 = json.load(f)
with open('tests/fixtures/file4.json') as f:
    json_data_4 = json.load(f)
with open('tests/fixtures/filepath3.yml') as f:
    yaml_data_3 = yaml.load(f, Loader=SafeLoader)
with open('tests/fixtures/filepath4.yml') as f:
    yaml_data_4 = yaml.load(f, Loader=SafeLoader)
with open('tests/fixtures/expected_stylish_1.txt') as f:
    expected_stylish_result_1 = f.read()
with open('tests/fixtures/expected_stylish_2.txt') as f:
    expected_stylish_result_2 = f.read()
with open('tests/fixtures/expected_plain_1.txt') as f:
    expected_plain_result_1 = f.read()
with open('tests/fixtures/expected_plain_2.txt') as f:
    expected_plain_result_2 = f.read()
diff_list_json_1 = get_diffs(json_data_1, json_data_2)
diff_list_yaml_1 = get_diffs(yaml_data_1, yaml_data_2)
diff_list_json_2 = get_diffs(json_data_3, json_data_4)
diff_list_yaml_2 = get_diffs(yaml_data_3, yaml_data_4)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (diff_list_json_1, expected_stylish_result_1),
        (diff_list_yaml_1, expected_stylish_result_1),
        (diff_list_json_2, expected_stylish_result_2),
        (diff_list_yaml_2, expected_stylish_result_2)
        ]
        )
def test_get_stylish(test_input, expected):
    assert get_stylish(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (diff_list_json_1, expected_plain_result_1),
        (diff_list_yaml_1, expected_plain_result_1),
        (diff_list_json_2, expected_plain_result_2),
        (diff_list_yaml_2, expected_plain_result_2)
        ]
        )
def test_get_plain(test_input, expected):
    assert get_plain(test_input) == expected
