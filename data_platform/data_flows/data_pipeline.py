class DataPipeline:
    """
    Run a data pipeline, include many dataflows
    """
    def __init__(self, data_flows):
        """
        Constructor
        :param data_flows: dataflows
        """
        self.data_flows = data_flows

    def start(self, data):
        """
        Run data pipeline
        :param data: input data
        :return: final data after run all dataflows
        """
        result = data
        for data_flow in self.data_flows:
            result = data_flow.start(result)
        return result
