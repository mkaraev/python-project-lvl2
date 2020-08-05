from gendiff.constants import (NESTED, UNCHANGED, REMOVED, ADDED, CHANGED)

operator = {
    ADDED: "{ws}+ {k}: {v}\n",
    REMOVED: "{ws}- {k}: {v}\n",
    UNCHANGED: "{ws}  {k}: {v}\n",
    CHANGED: "{ws}- {k}: {v1}\n{ws}+ {k}: {v2}\n",
    NESTED: "  {ws}{k}: {op_br}\n{v}{cl_br}\n"
}


def render(diff: dict) -> str:
    result = do_rendering(diff, indent=2)
    return "{\n" + result + "}"


def render_value(value, indent) -> str:
    if isinstance(value, dict):
        temp = []
        whitespaces = "".rjust(indent + 4)
        for k, v in value.items():
            line = f"{whitespaces}{k}: {v}\n"
            temp.append(line)
        return "{\n" + ''.join(temp) + "}".rjust(indent + 3)
    else:
        return value


def do_rendering(diff: dict, indent=1):
    rendered_lines = []
    ws = ''.rjust(indent)
    for key, value in diff.items():
        state = value[0]
        if state == NESTED:
            rend_line = do_rendering(value[1], indent + 4)
            rend_line = operator[state].format(
                ws=ws,
                k=key,
                op_br='{',
                v=rend_line,
                cl_br='}'.rjust(indent + 3)
            )

        elif state == CHANGED:
            before = render_value(value[1], indent)
            after = render_value(value[2], indent)
            rend_line = operator[state].format(
                ws=ws,
                k=key,
                v1=before,
                v2=after
            )
        else:
            new_value = render_value(value[1], indent)
            rend_line = operator[state].format(ws=ws, k=key, v=new_value)

        rendered_lines.append(rend_line)
    return ''.join(rendered_lines)
