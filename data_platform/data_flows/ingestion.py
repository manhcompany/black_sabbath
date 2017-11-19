from data_flows.data_flow import DataFlow


class Ingestion(DataFlow):
    def __init__(self, model, **kwargs):
        self.model = model
        self.param = kwargs
        super().__init__(self.handle, **kwargs)

    def start(self, data):
        super().start()

    def handle(self, data):
        return data.map(lambda x: self.model.load(x))\
            .filter(lambda x: x is not None)\
            .map(lambda x: x.transform())