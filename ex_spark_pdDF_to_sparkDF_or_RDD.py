import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext


# initialize spark context:
def init_spark_context():
    # load spark context
    conf = SparkConf()
    conf.setAppName("dataframes-test")
    sc = SparkContext(conf=conf)

    return sc

sc = init_spark_context()

sqlContext = SQLContext(sc)

d = {'col1': [1, 2], 'col2': [3, 4]}
my_spark_df = sqlContext.createDataFrame(pd.DataFrame(data=d))  # creates a spark Data Frame
my_rdd = my_spark_df.rdd.map(tuple)                             # creates a spark RDD and maps to tuple

my_spark_df.show(2)
print(my_rdd.take(2))