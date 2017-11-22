class Model(dict):
    def __init__(self):
        """
        constructor
        """
        self.__dict__ = self

    @staticmethod
    def load(data):
        """
        abstract: create a business from data
        :param data: input data
        :type data: object
        :return: model
        :rtype: Model
        """
        pass

    def get_id(self):
        """
        abstract: get id of business
        :return: id of business
        :rtype: str
        """
        pass

    def get_str(self):
        pass

    def transform(self):
        return self