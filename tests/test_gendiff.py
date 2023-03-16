from gendiff.gendiff import generate_diff
import pytest


with open('tests/fixtures/expected_stylish_1.txt') as f:
    expected_stylish_result_1 = f.read()
with open('tests/fixtures/expected_stylish_2.txt') as f:
    expected_stylish_result_2 = f.read()
with open('tests/fixtures/expected_plain_1.txt') as f:
    expected_plain_result_1 = f.read()
with open('tests/fixtures/expected_plain_2.txt') as f:
    expected_plain_result_2 = f.read()


@pytest.mark.parametrize(
    "file1, file2, expected, format_type",
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', expected_stylish_result_1, 'stylish'),
        ('tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yml', expected_stylish_result_1, 'stylish'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', expected_stylish_result_2, 'stylish'),
        ('tests/fixtures/filepath3.yml', 'tests/fixtures/filepath4.yml', expected_stylish_result_2, 'stylish'),
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', expected_plain_result_1, 'plain'),
        ('tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yml', expected_plain_result_1, 'plain'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', expected_plain_result_2, 'plain'),
        ('tests/fixtures/filepath3.yml', 'tests/fixtures/filepath4.yml', expected_plain_result_2, 'plain')
    ]
)
def test_generate_diff(file1, file2, expected, format_type):
    assert generate_diff(file1, file2, format_type) == expected
