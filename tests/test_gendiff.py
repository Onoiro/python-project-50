from gendiff.gendiff import generate_diff
import json
import yaml
from yaml.loader import SafeLoader

with open('tests/fixtures/file1.json') as f:
    data1 = json.load(f)
with open('tests/fixtures/file2.json') as f:
    data2 = json.load(f)
with open('tests/fixtures/filepath1.yml') as f:
    data3 = yaml.load(f, Loader=SafeLoader)
with open('tests/fixtures/filepath2.yml') as f:
    data4 = yaml.load(f, Loader=SafeLoader)
with open('tests/fixtures/result.txt') as f:
    right_result = f.read()


def test_generate_diff():
    assert generate_diff(data1, data2) == right_result
    assert generate_diff(data3, data4) == right_result
