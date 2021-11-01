from client import c, send

from achaea.basic import eqbal
from achaea.state import s


def random_recite():
    """
    recite attend - undeaf
    recite fragility - more damage to next limb attack
    recite condemnation - justice
    guilt - guilt - if they focus, will cure, but also get a new aff
    unflinching - strike through parry + short heresy
    ash - spiritburn - dmg + mana dmg when on fire
    penance - paralysis
    reflection - give affs to them instead of me
    burn - drains mana on applying salves

    rebukes:
    chaos - need 3 verses - hallucinations
    darkness - 2 verses - paranoia
    evil - 3 verses - masochism

    "{\"type\": \"Char.Vitals\", \"data\": {\"hp\": \"4843\", \"maxhp\": \"4843\", \"mp\": \"4150\", \"maxmp\": \"4150\", \"ep\": \"19265\", \"maxep\": \"19265\", \"wp\": \"15800\", \"maxwp\": \"15800\", \"nl\": \"49\", \"bal\": \"1\", \"eq\": \"1\", \"string\": \"H:4843/4843 M:4150/4150 E:19265/19265 W:15800/15800 NL:49/100 \", \"charstats\": [\"Bleed: 0\", \"Rage: 0\", \"Angelpower: 4767\", \"Devotion: 97%\", \"conviction: 10\", \"prayer_length: 0\", \"Prayer: Yes\"]}}"]
    """
    pass


zeal_aliases = [
    (
        "^rwill(?: (.+))?$",
        "recite will ?/me",
        lambda m: eqbal(f"recite will {m[0] or 'me'}"),
    ),
    (
        "^rend(?: (.+))?$",
        "recite endurance ?/me",
        lambda m: eqbal(f"recite endurance {m[0] or 'me'}"),
    ),
    (
        "^att(?: (.+))?$",
        "recite attend ?/me",
        lambda m: eqbal(f"recite attend {m[0] or '&tar'}"),
    ),
    (
        "^rfire(?: (.+))?$",
        "recite fire ?/me",
        lambda m: eqbal(f"recite fire {m[0] or 'me'}"),
    ),
    (
        "^rvoid(?: (.+))?$",
        "recite void ?/me",
        lambda m: eqbal(f"recite void {m[0] or '&tar'}"),
    ),
    (
        "^prot(?: (.+))?$",
        "recite protection ?/me",
        lambda m: eqbal(f"recite protection {m[0] or 'me'}"),
    ),
    (
        "^frag(?: (.+))?$",
        "recite fragility ?/me",
        lambda m: eqbal(f"recite fragility {m[0] or '&tar'}"),
    ),
    (
        "^cond(?: (.+))?$",
        "recite condemnation ?/me",
        lambda m: eqbal(f"recite condemnation {m[0] or '&tar'}"),
    ),
    (
        "^guilt(?: (.+))?$",
        "recite guilt ?/me",
        lambda m: eqbal(f"recite guilt {m[0] or '&tar'}"),
    ),
    (
        "^unf(?: (.+))?$",
        "recite unflinching ?/me",
        lambda m: eqbal(f"recite unflinching {m[0] or '&tar'}"),
    ),
    (
        "^rash(?: (.+))?$",
        "recite ash ?/me",
        lambda m: eqbal(f"recite ash {m[0] or '&tar'}"),
    ),
    (
        "^pen(?: (.+))?$",
        "recite penance ?/me",
        lambda m: eqbal(f"recite penance {m[0] or '&tar'}"),
    ),
    (
        "^ref(?: (.+))?$",
        "recite reflection ?/me",
        lambda m: eqbal(f"recite reflection {m[0] or '&tar'}"),
    ),
    (
        "^burn(?: (.+))?$",
        "recite burn ?/me",
        lambda m: eqbal(f"recite burn {m[0] or '&tar'}"),
    ),
    (
        "^lig$",
        "recite light",
        lambda m: eqbal(f"recite light"),
    ),
    (
        "^ref(?: (.+))?$",
        "recite reflection ?/me",
        lambda m: eqbal(f"recite reflection {m[0] or '&tar'}"),
    ),
]
c.add_aliases("ab_zeal", zeal_aliases)
