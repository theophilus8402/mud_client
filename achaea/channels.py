from client import c, echo, send
from client.messenger import SimpleMessenger
from client.logger import SimpleFileLogger


says = SimpleMessenger()
says_logger = SimpleFileLogger("says.log")
says.attach(says_logger)


def handle_says(gmcp_data):
    says(gmcp_data["text"])
c.add_gmcp_handler("Comm.Channel.Text", handle_says)
