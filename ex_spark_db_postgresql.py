from pyspark.sql import DataFrameReader, SQLContext
from pyspark import SparkContext, SparkConf
import os

# Thanks to this post, this was solved:
# https://stackoverflow.com/a/46360434/8510370
#
# NOTE: Download the jdbc driver from https://jdbc.postgresql.org/download.html
#       and place it in your project or copy to all machines with environmental variables set

sparkClassPath = os.getenv('SPARK_CLASSPATH', os.path.join(os.getcwd(), 'postgresql-42.2.2.jar'))

conf = SparkConf()
conf.setAppName('application')
conf.set('spark.jars', 'file:%s' % sparkClassPath)
conf.set('spark.executor.extraClassPath', sparkClassPath)
conf.set('spark.driver.extraClassPath', sparkClassPath)
# Uncomment line below and modify ip address if you need to use cluster on different IP address
# conf.set('spark.master', 'spark://127.0.0.1:7077')

sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
url = 'jdbc:postgresql://127.0.0.1:5432/movielens'
properties = {'user': 'postgres', 'password': 'password'}

df = DataFrameReader(sqlContext).jdbc(url=url, table='movies', properties=properties)

df.select("movieid", "title").show(n=2)

movies_rdd = df.select("movieid", "title").rdd.map(tuple)
print(movies_rdd.take(5))
