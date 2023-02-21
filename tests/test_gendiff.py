from gendiff.gendiff import generate_diff

def test_generate_diff():
    assert generate_diff({
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  },
  {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
  }) == (
        '{\n  - follow: False'
        '\n    host: hexlet.io'
        '\n  - proxy: 123.234.53.22'
        '\n  - timeout: 50'
        '\n  + timeout: 20'
        '\n  + verbose: True'
        '\n}'
  )
