from pyspark.sql.types import *
from pyspark.sql.functions import from_unixtime

schema = StructType([
    StructField("userId", IntegerType(), True),
    StructField("movieId", IntegerType(), True),
    StructField("rating", DoubleType(), True),
    StructField("timestamp", IntegerType(), True)
])

ratings = spark.read.csv("datasets/ml-latest-small/ratings.csv", header=True, nullValue='NA', schema=schema)
ratings = ratings.withColumn('timestamp', from_unixtime('timestamp').cast(TimestampType()))

ratings.show()
ratings.printSchema()