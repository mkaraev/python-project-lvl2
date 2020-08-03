from gendiff.constants import CHANGED, UNCHANGED, NESTED, ADDED, REMOVED

constants_map = {
    CHANGED: "was changed. From '{0}' to '{1}'",
    ADDED: "was added with value: '{0}'",
    REMOVED: "was removed",
    UNCHANGED: ""
}


def render(diff: dict, path=''):
    rendered_lines = []
    template_str = "Property '{path}' {line}\n"
    for key, value in diff.items():
        state = value[0]
        if state == NESTED:
            rend_line = render(value[1], path + f"{key}.")
            rendered_lines.append(rend_line)
        elif state == UNCHANGED:
            continue
        else:
            temp_value = affected_values(value[1:])
            rend_line = constants_map[state].format(*temp_value)
            rendered_lines.append(
                template_str.format(path=path + f'{key}', line=rend_line)
            )
    return ''.join(rendered_lines)


def affected_values(values: tuple):
    new_list = []
    for v in values:
        if isinstance(v, dict):
            v = 'complex value'
        new_list.append(v)
    return new_list
