from gendiff.file_parser import get_dict


def get_data(filepath):
    extencion = filepath[-4:]
    with open(filepath) as f:
        obj = f.read()
    return get_dict(obj, extencion)
