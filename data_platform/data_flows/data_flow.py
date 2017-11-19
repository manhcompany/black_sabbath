class DataFlow:
    def __init__(self, handle, **kwargs):
        self.handle = handle
        self.params = kwargs

    def start(self, data):
        return self.handle(data, self.params)
