class SimpleMessenger():

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observer.remove(observer)

    def notify(self, msg):
        for observer in self._observers:
            observer.update(msg)

    def __call__(self, msg):
        self.notify(msg)
