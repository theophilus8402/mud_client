from achaea.basic import curebal, eqbal
from achaea.state import s
from client import c, echo, send

seafaring_aliases = [
    # (   "^cdef$",
    #    "list of defences",
    #    check_defences,
    # ),
]
c.add_aliases("seafaring", seafaring_aliases)
