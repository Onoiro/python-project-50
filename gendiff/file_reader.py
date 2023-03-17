from gendiff.file_parser import get_dict


def get_data(filepath):
    extention = filepath.split('.')[-1]
    with open(filepath) as f:
        obj = f.read()
    return get_dict(obj, extention)
