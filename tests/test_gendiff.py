from gendiff.gendiff import generate_diff
from gendiff.stylish import format_diff
import json
import yaml
from yaml.loader import SafeLoader

with open('tests/fixtures/file1.json') as f:
    json_data_1 = json.load(f)
with open('tests/fixtures/file2.json') as f:
    json_data_2 = json.load(f)
with open('tests/fixtures/filepath1.yml') as f:
    yaml_data_1 = yaml.load(f, Loader=SafeLoader)
with open('tests/fixtures/filepath2.yml') as f:
    yaml_data_2 = yaml.load(f, Loader=SafeLoader)
with open('tests/fixtures/expected_result_1.txt') as f:
    expected_result_1 = f.read()
with open('tests/fixtures/file3.json') as f:
    json_data_3 = json.load(f)
with open('tests/fixtures/file4.json') as f:
    json_data_4 = json.load(f)
with open('tests/fixtures/filepath3.yml') as f:
    yaml_data_3 = yaml.load(f, Loader=SafeLoader)
with open('tests/fixtures/filepath4.yml') as f:
    yaml_data_4 = yaml.load(f, Loader=SafeLoader)
with open('tests/fixtures/expected_result_2.txt') as f:
    expected_result_2 = f.read()
'''with open('fixtures/file3.json') as f:
    json_data_3 = json.load(f)
with open('fixtures/file4.json') as f:
    json_data_4 = json.load(f)'''


def test_generate_diff():
    diff_list_json_1 = generate_diff(json_data_1, json_data_2)
    diff_list_yaml_1 = generate_diff(yaml_data_1, yaml_data_2)
    diff_list_json_2 = generate_diff(json_data_3, json_data_4)
    diff_list_yaml_2 = generate_diff(yaml_data_3, yaml_data_4)
    assert format_diff(diff_list_json_1) == expected_result_1
    assert format_diff(diff_list_yaml_1) == expected_result_1
    assert format_diff(diff_list_json_2) == expected_result_2
    assert format_diff(diff_list_yaml_2) == expected_result_2

'''diff_list = generate_diff(json_data_3, json_data_4)
print(format_diff(diff_list))'''
