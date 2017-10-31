from pyspark import SparkContext

from utils.singleton_meta import SingletonMeta


class Context(metaclass=SingletonMeta):
    def __init__(self):
        """
        Constructor
        """
        self.__sc = SparkContext()

    def get_context(self):
        """
        Get spark context (Singleton)
        :return: spark context
        :rtype: SparkContext
        """
        return self.__sc
