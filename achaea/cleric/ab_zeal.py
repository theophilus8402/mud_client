
from client import send, c
from ..basic import eqbal
from ..state import s


zeal_aliases = [
    (   "^att(?: (.+))?$",
        "recite attend */t",
        lambda m: eqbal(f"recite attend {m[0] or '&tar'}")
    ),
    (   "^rfire(?: (.+))?$",
        "recite fire ?/me",
        lambda m: eqbal(f"recite fire {m[0] or 'me'}")
    ),
    (   "^rvoid(?: (.+))?$",
        "recite void ?/me",
        lambda m: eqbal(f"recite void {m[0] or 'me'}")
    ),
    (   "^prot(?: (.+))?$",
        "recite protection ?/me",
        lambda m: eqbal(f"recite protection {m[0] or 'me'}")
    ),
    (   "^pen$",
        "recite penance ?/t",
        lambda m: eqbal(f"recite penance &tar")
    ),
]
c.add_aliases("ab_zeal", zeal_aliases)


