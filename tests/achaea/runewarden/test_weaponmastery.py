from queue import Queue

from achaea.runewarden.ab_weaponmastery import *
from achaea.state import s
from client import c


def test_raze_target():
    c.to_send.clear()
    s.target = "bill"
    raze_target("bill")
    assert c.to_send.pop() == f"queue prepend eqbal stand;raze {s.target}"
