import asyncio


class MultiQueue:
    def __init__(self):
        self.main_queue = asyncio.Queue()

        # name : queue
        self.receivers = {}

    def put_nowait(self, item):
        for q in self.receivers.values():
            q.put_nowait(item)

    def put(self, item):
        for q in self.receivers.values():
            q.put(item)

    def get_receiver(self, name):
        new_queue = asyncio.Queue()
        self.receivers[name] = new_queue
        return new_queue

    def remove_receiver(self, name):
        del self.receivers[name]


if __name__ == "__main__":

    mqueue = MultiQueue()
    r1 = mqueue.get_receiver("r1")
    r2 = mqueue.get_receiver("r2")

    mqueue.put_nowait("test")
