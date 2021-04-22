from achaea.basic import eqbal
from achaea.fighting_log import fighting
from achaea.group_fighting.party import party_announce, register_announce_type
from achaea.state import s
from client import c, echo, send


register_announce_type("jester")


def fighting_pann(msg):
    fighting(msg)
    party_announce(msg, "jester")


pranks_triggers = [
    (
        r"^You reach out and bop (.*) on the nose with your blackjack.$",
        # bop'd someone!
        lambda m: fighting(f"BOP'D {m[0]}"),
    ),
    (
        r"^You quickly slip (.*) a mickey.$",
        lambda m: fighting_pann(f"MICKEY'd {m[0]}"),
    ),
]
c.add_triggers(pranks_triggers)


tarot_triggers = [
    (
        r"^Standing the Aeon on your open palm, you blow it lightly at (.*) and watch as it seems to slow .* movement through the time stream.$",
        lambda m: fighting_pann(f"AEON'd {m[0]}"),
    ),
]
c.add_triggers(tarot_triggers)


puppetry_triggers = [
    (
        r"^With a little laugh, you sink your fingers into the wood and shape it into the rough semblance of a humanoid.$",
        lambda m: fighting(f"FASHION'd (1) {s.target}"),
    ),
    (
        r"^While you hastily examine (.*), you mould the fledgling puppet a bit, further defining the arms and legs.$",
        lambda m: fighting(f"FASHION'd (2-9) {m[0]}"),
    ),
    (
        r"^Adding further detail to the puppet of (.*), you work on defining the nose, ears, eyes, and mouth.$",
        lambda m: fighting(f"FASHION'd (10-19) {m[0]}"),
    ),
    (
        r"^You examine the puppet carefully, and begin to form fingers and toes.$",
        lambda m: fighting(f"FASHION'd (20-29) {s.target}"),
    ),
    (
        r"^You fashion the eyes of your puppet to resemble those of (.*).$",
        lambda m: fighting(f"FASHION'd (30-39) {m[0]}"),
    ),
    (
        r"^With one hand pointed towards (.*), you rub your finger over the heart of your puppet.$",
        lambda m: fighting(f"FASHION'd (40-49) {m[0]}"),
    ),
    (
        r"^You laugh darkly and squint at (.*) as you add some final touches to your puppet of .*.$",
        lambda m: fighting(f"FASHION'd (50+) {m[0]}"),
    ),
]
c.add_triggers(puppetry_triggers)
