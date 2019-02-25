
from .client import add_gmcp_handler, echo
from .variables import v

def gmcp_bal_eq(gmcp_data):

    v.bal = gmcp_data.get("bal")
    v.eq = gmcp_data.get("eq")

add_gmcp_handler("Char.Vitals", gmcp_bal_eq)

