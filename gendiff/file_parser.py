import json
import yaml
from yaml.loader import SafeLoader


def get_dict(filepath):
    if filepath[-4:] == 'json':
        data = json.load(open(filepath))
    else:
        with open(filepath) as f:
            data = yaml.load(f, Loader=SafeLoader)
    return data
