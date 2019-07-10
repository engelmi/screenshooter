import json

def read_json_config(path_to_json):
    with open(path_to_json) as jfile:
        return json.load(jfile)
