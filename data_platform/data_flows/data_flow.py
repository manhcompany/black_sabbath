class DataFlow:
    """
    Abstract dataflow
    """
    def __init__(self, handle, **kwargs):
        """
        Constructor
        :param handle: handle function
        :param kwargs: parameters
        """
        self.handle = handle
        self.params = kwargs

    def start(self, data):
        """
        Run handle function with input data
        :param data: dataframe or rdd
        :return: result of handle function
        """
        return self.handle(data, **self.params)
