class Sender():
    """
    The idea for the sender is you can send something here and the message
    will be send to any number of recipients.  The recipients can process
    the information as they wish.

    I'm hoping this will help with things like logging and announcing things.
    """

    def __init__(self):
        self.receivers = []

    def __call__(self, msg):
        for rcvr in self.receivers:
            rcvr.receive(msg)

    def add_receiver(self, receiver):
        self.receivers.append(receiver)

    def remove_receiver(self, receiver):
        try:
            self.receivers.remove(receiver)
        except ValueError:
            pass
