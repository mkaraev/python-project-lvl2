import json
import yaml


def load_file(path: str) -> dict:
    with open(path) as f:
        if path.endswith('.yaml') or path.endswith('.yml'):
            return yaml.safe_load(f)
        return json.load(f)


if __name__ == '__main__':
    dd = load_file("/home/mkaraev/PycharmProjects/python-project-lvl2/sample.yaml")
    print(dd)
