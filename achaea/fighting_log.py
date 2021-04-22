from client.messenger import SimpleMessenger
from client.logger import SimpleFileLogger


fighting = SimpleMessenger()
fighting_logger = SimpleFileLogger("fighting.log")
fighting.attach(fighting_logger)
