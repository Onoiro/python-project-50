from gendiff.file_parser import get_object


def get_extention(filepath):
    extention = filepath.split('.')[-1]
    return extention


def get_data(filepath):
    with open(filepath) as f:
        data = f.read()
    return get_object(data, get_extention(filepath))
