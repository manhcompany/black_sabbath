from pyspark.sql.utils import AnalysisException


class ExternalDeDuplication:
    def __init__(self, parquet_storage, key='id'):
        """
        Constructor
        :param parquet_storage: parquet storage of master data
        :type parquet_storage: ParquetStorage
        :param key: Unique key
        :type key: str
        """
        self.__parquet_storage = parquet_storage
        self.__key = key

    def deduplicate(self, rdd_new):
        """
        De-Duplicate
        :param rdd_new: rdd input to master data
        :type rdd_new: RDD
        :return: rdd not exist in master data
        :rtype: RDD
        """
        try:
            rdd_exist = self.__parquet_storage.select(self.__key).rdd
            rdd_exist = rdd_exist.map(lambda x: (str(x.id).strip(), x))
            rdd_union = rdd_new \
                .reduceByKey(lambda x, y: x) \
                .union(rdd_exist) \
                .reduceByKey(lambda x, y: None) \
                .filter(lambda x: (x[1] is not None) and
                                  (x[1].__class__.__name__ != "Row"))
        except AnalysisException:
            rdd_union = rdd_new \
                .reduceByKey(lambda x, y: x)
        return rdd_union.map(lambda x: x[1])
