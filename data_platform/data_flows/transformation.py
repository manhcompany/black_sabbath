from data_flows.internal_deduplication import InternalDeDuplication

from data_flows.cleaning import Cleaning

from context.session import Session
from pyspark.sql import Row


class Transformation:
    def __init__(self, model, external_deduplication=None,
                 cleaning=Cleaning(), internal_deduplication=InternalDeDuplication()):
        self.__model = model
        self.__external_deduplication = external_deduplication
        self.__cleaning = cleaning
        self.__internal_deduplication = internal_deduplication

    def start(self, data):
        rdd_data = data.map(lambda x: self.__model.load(x)) \
            .filter(lambda x: x is not None) \
            .map(lambda x: x.transform())

        rdd_data = self.external_deduplicate(rdd_data)
        rows = rdd_data\
            .map(lambda x: Row(**dict(x)))

        df = Session().get_session().createDataFrame(rows, samplingRatio=1.0).dropDuplicates()

        df = self.cleaning(df)
        df = self.internal_deduplicate(df)

        return df

    def cleaning(self, df):
        return self.__cleaning.cleaning(df)

    def internal_deduplicate(self, df):
        return self.__internal_deduplication.deduplicate(df)

    def external_deduplicate(self, rdd_data):
        if self.__external_deduplication is not None:
            rdd_data = rdd_data.map(lambda x: (x.get_id(), x))
            rdd_data = self.__external_deduplication.deduplicate(rdd_data)
        return rdd_data
