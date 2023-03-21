from gendiff.file_parser import get_object


def get_data(filepath):
    extention = filepath.split('.')[-1]
    with open(filepath) as f:
        obj = f.read()
    return get_object(obj, extention)
