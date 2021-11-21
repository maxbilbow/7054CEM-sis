import yaml

_config = None


def load_config(config_file: str):
    with open(config_file) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        global _config
        _config = yaml.load(file, Loader=yaml.FullLoader)


def get(path: str):
    global _config
    if not _config:
        raise ReferenceError("Config was not initialised")
    parts = path.split(".")
    result = _config
    for part in parts:
        result = result[part]

    return result
