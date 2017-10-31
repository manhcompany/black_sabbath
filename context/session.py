from pyspark.sql import SparkSession

from context.context import Context
from utils.singleton_meta import SingletonMeta


class Session(metaclass=SingletonMeta):
    def __init__(self):
        sc = Context()
        self.__session = SparkSession.builder.getOrCreate()

    def get_session(self):
        return self.__session
