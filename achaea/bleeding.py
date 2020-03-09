
from .client import c, send, echo
from .state import s


def stop_bleeding(matches):
    amt = int(matches[0])
    clots = []
    if (amt >= 50) and (s.mp >= 4500):
        clots.append("clot")
    if (amt >= 100) and (s.mp >= 4400):
        clots.append("clot")
    if (amt >= 200) and (s.mp >= 4300):
        clots.append("clot")
    if (amt >= 300) and (s.mp >= 4200):
        clots.append("clot")
    if (amt >= 400) and (s.mp >= 4100):
        clots.append("clot")
    if clots:
        echo(f"Clotting {len(clots)}x!")
        send(";".join(clots))


bleeding_triggers = [
    (   r"^You bleed (\d+) health.$",
        # bleeding!
        stop_bleeding
    ),
]
c.add_triggers(bleeding_triggers)
