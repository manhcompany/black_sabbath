class Model(dict):
    """
    Abstract model
    """
    def __init__(self):
        """
        constructor
        """
        self.__dict__ = self

    @staticmethod
    def load(data):
        """
        abstract: create a model from data
        :param data: input data
        :type data: object
        :return: model
        :rtype: Model
        """
        pass

    def get_id(self):
        """
        abstract: get id of model
        :return: id of model
        :rtype: str
        """
        pass

    def get_str(self):
        """
        Get string of model
        :return: str
        """
        pass

    def transform(self):
        """
        Transform model
        :return:
        """
        return self