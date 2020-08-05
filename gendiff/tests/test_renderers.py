from gendiff.gen_diff import generate_difference_deep
from gendiff.render import nested_renderer, json_renderer, plain_renderer
from gendiff import io

before_dict = io.load_file("./gendiff/tests/fixtures/before.json")
after_dict = io.load_file("./gendiff/tests/fixtures/after.json")
diff = generate_difference_deep(before_dict, after_dict)


def test_plain_renderer():
    result = plain_renderer.render(diff).strip()
    with open("./gendiff/tests/fixtures/plain_text") as f:
        test_string = f.read()
    assert result == test_string


def test_nested_renderer():
    result = nested_renderer.render(diff).replace(" ", "")
    with open("./gendiff/tests/fixtures/nested_text") as f:
        test_string = f.read().replace(" ", "")
    assert result == test_string


def test_json_renderer():
    result = json_renderer.render(diff)
    with open("./gendiff/tests/fixtures/json_text") as f:
        test_string = f.read()
    assert result == test_string
