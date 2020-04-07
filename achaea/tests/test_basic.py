
from achaea.client import c, send, echo, delete_line

def test_echo():
    assert echo("hello") != None
    assert len(echo("hello").echo_lines) == 1
    assert echo("hello").echo_lines[0] == "hello"
    
