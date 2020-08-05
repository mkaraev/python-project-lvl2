from gendiff import io


def test_io_reads_yaml():
    test_dict = io.load_file("./gendiff/tests/fixtures/test_yaml.yaml")
    sample_dict = {
        "common": {
            "setting1": "Value 1",
            "setting2": "200",
            "setting3": True,
            "setting6": {
                "key": "value"
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar"
        },
        "group2": {
            "abc": "12345"
        }
    }
    assert test_dict == sample_dict


def test_io_reads_json():
    test_dict = io.load_file("./gendiff/tests/fixtures/before.json")
    sample_dict = {
        "common": {
            "setting1": "Value 1",
            "setting2": "200",
            "setting3": True,
            "setting6": {
                "key": "value"
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar"
        },
        "group2": {
            "abc": "12345"
        }
    }
    assert test_dict == sample_dict
