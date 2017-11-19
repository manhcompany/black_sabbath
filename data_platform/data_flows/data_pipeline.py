class DataPipeline:
    def __init__(self, data_flows):
        self.data_flows = data_flows

    def start(self, data):
        result = data
        for data_flow in self.data_flows:
            result = data_flow.start(result)
        return result
