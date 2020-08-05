from gendiff import io
from gendiff.constants import (ADDED, CHANGED, NESTED, REMOVED, UNCHANGED)
from collections import OrderedDict


def generate_difference_deep(before_dict: dict, after_dict: dict) -> dict:
    diff = {}

    before_dict_keys = set(before_dict.keys())
    after_dict_keys = set(after_dict.keys())

    removed_keys = before_dict_keys.difference(after_dict)
    for key in removed_keys:
        diff[key] = (REMOVED, before_dict[key])

    added_keys = after_dict_keys.difference(before_dict_keys)
    for key in added_keys:
        diff[key] = (ADDED, after_dict[key])

    for key in before_dict_keys.intersection(after_dict_keys):
        old_value = before_dict[key]
        new_value = after_dict[key]
        nested = isinstance(old_value, dict) and isinstance(new_value, dict)
        if nested:
            diff[key] = (
                NESTED,
                generate_difference_deep(old_value, new_value)
            )
        elif new_value == old_value:
            diff[key] = (UNCHANGED, old_value)
        else:
            diff[key] = (CHANGED, old_value, new_value)

    return OrderedDict(sorted(diff.items(), key=lambda k: k))


def generate_diff(
        path_to_before,
        path_to_after,
        output_renderer
) -> str:
    before_dict = io.load_file(path=path_to_before)
    after_dict = io.load_file(path=path_to_after)
    diff = generate_difference_deep(before_dict, after_dict)
    return output_renderer.render(diff)
