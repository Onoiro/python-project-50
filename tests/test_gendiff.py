from gendiff.gendiff import generate_diff
import json

'''with open('tests/fixtures/file1.json') as f:
    data1 = json.load(f)
with open('tests/fixtures/file2.json') as f:
    data2 = json.load(f)
with open('tests/fixtures/result.txt') as f:
    right_result = f.read()'''

data1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  }
data2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
  }
right_result = (
        '{\n  - follow: False'
        '\n    host: hexlet.io'
        '\n  - proxy: 123.234.53.22'
        '\n  - timeout: 50'
        '\n  + timeout: 20'
        '\n  + verbose: True'
        '\n}'
  )


def test_generate_diff():
    assert generate_diff(data1, data2) == right_result
