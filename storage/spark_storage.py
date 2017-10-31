from context.context import Context

from context.session import Session
from storage.storage import SparkStorage


class FileStorage(SparkStorage):
    def __init__(self, config):
        super().__init__()
        self.__config = config

    def save(self, data, options=''):
        data.saveAsTextFile(self.__config.get_target_path())

    def load(self):
        sc = Context()
        return sc.get_context().textFile(self.__config.get_source_path())


class ParquetStorage(SparkStorage):
    def __init__(self, config):
        super().__init__()
        self.__config = config

    def load(self):
        session = Session()
        return session.get_session().read.load(self.__config.get_source_path())

    def select(self, columns='*'):
        session = Session()
        return session.get_session().sql("select %s from parquet.`%s`" % (columns, self.__config.get_source_path()))

    def save(self, data, mode='append', coalesce=0):
        if coalesce == 0:
            return data.write.mode(mode).save(self.__config.get_target_path())
        else:
            return data.coalesce(coalesce).write.mode(mode).save(self.__config.get_target_path())


class AvroStorage(SparkStorage):
    def __init__(self, config):
        super().__init__()
        self.__config = config

    def load(self):
        session = Session()
        return session.get_session().read.format("com.databricks.spark.avro").load(self.__config.get_source_path())

    def save(self, data):
        return data.write.format("com.databricks.spark.avro").save(self.__config.get_target_path())
