import json


def load_file(path) -> dict:
    return json.load(path)


if __name__ == '__main__':
    with open("../data/before.json") as f:
        print(f)
        print(load_file(f))
