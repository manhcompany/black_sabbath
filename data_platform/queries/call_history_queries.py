from context.session import Session
from pyspark.sql.functions import *


def aggregate_call_duration(df):
    return df.groupBy('from_phone_number').\
        sum("call_duration").\
        select(col("from_phone_number").alias("from_phone_number"),
               col("sum(call_duration)").alias("call_duration"))


def aggregate_number_of_call(df):
    return df.groupBy('from_phone_number').\
        count().\
        select(col('from_phone_number'),
               col('count').alias('number_of_call'))


def aggregate_number_of_call_in_working_hour(df, **kwargs):
    first_hour = int(kwargs['first_hour'])
    second_hour = int(kwargs['second_hour'])
    return df.where((df.hour >= first_hour) & (df.hour <= second_hour)).\
        groupBy('from_phone_number').\
        count().\
        select(col('from_phone_number'),
               col('count').alias('number_of_call'))


def find_imei_most_call(df, *args):
    row = df.groupBy('from_phone_number', 'imei').\
        count().\
        select(col('from_phone_number'), col('imei'), col('count').alias('number_of_call')).\
        orderBy('number_of_call').first()
    df_result = Session().get_session().createDataFrame([row])
    return df_result


def find_top_2_localtion(df, *args):
    rows = df.groupBy('from_phone_number', 'location').\
        count().\
        select(col("from_phone_number"), col("location"), col("count").alias("number_of_call")).\
        orderBy('number_of_call').head(2)
    df_result = Session().get_session().createDataFrame(rows)
    return df_result
