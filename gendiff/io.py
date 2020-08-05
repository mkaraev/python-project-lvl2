import json
import yaml


def load_file(path: str) -> dict:
    with open(path) as f:
        if path.endswith('.yaml') or path.endswith('.yml'):
            return yaml.safe_load(f)
        return json.load(f)
