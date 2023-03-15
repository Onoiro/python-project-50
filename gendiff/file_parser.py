import json
import yaml
from yaml.loader import SafeLoader


def get_dict(obj, extencion):
    if extencion == 'json':
        result_dict = json.loads(obj)
    else:
        result_dict = yaml.load(obj, Loader=SafeLoader)
    return result_dict
