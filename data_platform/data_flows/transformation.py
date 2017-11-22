from context.session import Session
from pyspark.sql import Row


class Transformation:
    def __init__(self, model, deduplication=None):

        self.__model = model
        self.__deduplication = deduplication

    def start(self, data):
        rdd_data = data.map(lambda x: self.__model.load(x))\
            .filter(lambda x: x is not None)\
            .map(lambda x: x.transform())
        print(rdd_data.collect())
        if self.__deduplication is not None:
            rdd_data = rdd_data.map(lambda x: (x.get_id(), x))
            rdd_data = self.__deduplication.deduplicate(rdd_data)
        rows = rdd_data\
            .map(lambda x: Row(**dict(x)))

        df = Session().get_session().createDataFrame(rows, samplingRatio=1.0).dropDuplicates().dropna()
        return df
