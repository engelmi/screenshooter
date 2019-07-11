import json

def read_json_config(path_to_json):
    """
    Reads a json config file and returns a python dict.
    :param path_to_json: Path to the json config file.
    :return: A python dict representation of the config.
    """
    with open(path_to_json) as jfile:
        return json.load(jfile)
