'''from gendiff.gendiff import generate_diff

def test_generate_diff():
    assert generate_diff({
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": false
  },
  {
    "timeout": 20,
    "verbose": true,
    "host": "hexlet.io"
  }) == '''