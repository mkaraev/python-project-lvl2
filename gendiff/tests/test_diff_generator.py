from gendiff.constants import (
    UNCHANGED,
    CHANGED,
    ADDED,
    REMOVED,
    NESTED
)
from gendiff import io
from gendiff.gen_diff import generate_difference_deep

before_dict = io.load_file("./gendiff/tests/fixtures/before.json")
after_dict = io.load_file("./gendiff/tests/fixtures/after.json")


def test_generate_diff():
    result = generate_difference_deep(before_dict, after_dict)

    assert result == {
        "common": (NESTED, {
            "setting1": (UNCHANGED, "Value 1"),
            "setting2": (REMOVED, "200"),
            "setting3": (UNCHANGED, True),
            "setting4": (ADDED, "blah blah"),
            "setting5": (ADDED, {"key5": "value5"}),
            "setting6": (REMOVED, {"key": "value"})
        }),
        "group1": (NESTED, {
            "baz": (CHANGED, "bas", "bars"),
            "foo": (UNCHANGED, "bar")
        }),
        "group2": (REMOVED, {"abc": "12345"}),
        "group3": (ADDED, {"fee": "100500"})
    }
