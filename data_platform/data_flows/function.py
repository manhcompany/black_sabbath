from data_flows.data_flow import DataFlow


class Function(DataFlow):
    """
    Dataflow of a special function
    """
    def __init__(self, model, **kwargs):
        """
        Constructor
        :param model: Model of special function
        :param kwargs: parameters
        """
        self.model = model
        self.param = kwargs
        super().__init__(self.handle, **kwargs)

    def start(self, data):
        """
        Start dataflow
        :param data:
        :return:
        """
        return self.handle(data)

    def handle(self, data, **kwargs):
        """
        Handle function, which transforming data
        :param data: data
        :param params: parameters
        :return: DataFrame or RDD
        """
        return data.map(lambda x: self.model.load(x))\
            .filter(lambda x: x is not None)\
            .map(lambda x: x.transform())