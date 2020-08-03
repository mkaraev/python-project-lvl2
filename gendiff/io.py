import json


def load_file(path) -> dict:
    with open(path) as f:
        return json.load(f)


if __name__ == '__main__':
    with open("/gendiff/tests/fixtures/before.json") as f:
        print(f)
        print(load_file(f))
