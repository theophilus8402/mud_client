class SimpleFileLogger():

    def __init__(self, file_path):
        self._fd = open(file_path, "a")

    def update(self, msg):
        if not msg.endswith("\n"):
            msg = msg + "\n"
        self._fd.write(msg)
        self._fd.flush()

    def __del__(self):
        self._fd.close()
