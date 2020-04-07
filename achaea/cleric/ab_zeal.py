
from ..client import send, add_aliases
from ..basic import eqbal
from ..state import s


zeal_aliases = [
    (   "^att(?: (.+))?$",
        "recite attend */t",
        lambda m: eqbal(f"recite attend {m[0] or v.target}")
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
]
add_aliases("ab_zeal", zeal_aliases)


