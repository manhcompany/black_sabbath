from pyspark.sql import SparkSession

from context.context import Context
from utils.singleton_meta import SingletonMeta


class Session(metaclass=SingletonMeta):
    """
    Session in Spark
    """
    def __init__(self):
        """
        Constructor
        """
        sc = Context()
        self.__session = SparkSession.builder.getOrCreate()

    def get_session(self):
        """
        Get session
        :return: Spark Session (Singleton)
        """
        return self.__session
