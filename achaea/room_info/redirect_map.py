from client import c, echo

from ..state import s

# --- Area 121: Mhaldor -------
#
#                         [_]
#
#     [ ]-[_]-[ ]         [=]
#
#         [=]             [^]
#          |             / | \
#     [ ]-[ ]-[+]      /  [$]
#          |         /
#         [ ]- - -[ ]
#                /
#             [_]
#            /
#          /
#        /
# ---------- -3:10:1 ----------


def parse_map(current_line):
    if current_line.count(":") != 1:
        # probably not the beginning line
        return

    start_index = 0
    chunk_lines = c.current_chunk.split("\n")
    for i, line in enumerate(chunk_lines):
        if line == current_line:
            start_index = i
            end_index = start_index
            stuff = chunk_lines[i : i + 5]
        elif (line.count(":") >= 2) and (line.count("-") >= 6):
            end_index = i
            break

    stuff = chunk_lines[start_index : end_index + 1]
    c.delete_lines(stuff)
    echo("\n".join(stuff))


map_triggers = [
    (
        r"^--- (.*) -*---$",
        # beginning of map
        lambda m: parse_map(c.current_line),
    ),
    (
        r"^----+ (.*) -*---$",
        # beginning of map
        lambda m: echo(f"end of map: {m[0]}"),
    ),
]
c.add_triggers(map_triggers)
