import json
import yaml
from yaml.loader import SafeLoader


def get_object(obj, extention):
    if extention == 'json':
        result = json.loads(obj)
    else:
        result = yaml.load(obj, Loader=SafeLoader)
    return result
