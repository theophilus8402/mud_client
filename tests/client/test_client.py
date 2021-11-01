from client import c, send


def test_send():
    c.to_send.clear()
    send("hello")
    assert c.to_send[0] == "hello"
