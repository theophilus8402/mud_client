from client import c

assisted = None

def set_assisted(new_assisted):
    global assisted
    assisted = new_assisted


assist_aliases = [
    (
        "^assist (.+)$",
        "assist someone",
        lambda m: set_assisted(m[0]),
    ),
]
c.add_aliases("assist", assist_aliases)
