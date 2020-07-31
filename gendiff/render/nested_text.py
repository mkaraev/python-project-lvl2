from gendiff.gendiff import State

TAB = "\t"
NEWLINE = "\n"
operator = {
    State.ADDED: "+",
    State.REMOVED: "-",
    State.UNCHANGED: " ",
}


def render(diff: dict, indent=1) -> str:
    pass

