
from .client import c
from .state import s

def gmcp_bal_eq(gmcp_data):
    s.bal = gmcp_data.get("bal")
    s.eq = gmcp_data.get("eq")
c.add_gmcp_handler("Char.Vitals", gmcp_bal_eq)

