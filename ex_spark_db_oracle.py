from pyspark import SparkContext, SparkConf
from pyspark.sql.session import SparkSession
from pyspark.sql import DataFrameReader, SQLContext
import os
from config import config
import time

db_params = config(filename='database.ini', section='oracle')

# set oracle url
db_url = "jdbc:oracle:thin:{user}/{password}@//{host}:{port}/{service}".format(**db_params)
db_properties = {'user': db_params['user'], 'password': db_params['password']}


# initialize spark context:
def init_spark_context():
    # set environment
    sparkClassPath = os.getenv('SPARK_CLASSPATH', os.path.join(os.getcwd(), 'ojdbc6.jar'))
    # load spark context
    conf = SparkConf()
    conf.setAppName("oracle-test")
    # conf.set("log4j.configuration", "log4j.properties")
    # conf.setMaster("spark://localhost:7077")    # hardcoded master (not recommended)
    # conf.set("spark.executor.memory", "16G")          # memory per executor
    # conf.set("spark.submit.deployMode", "cluster")    # use when ...
    conf.set('spark.jars', '{}'.format(sparkClassPath))  # jars to include on the driver and executor classpaths
    # conf.set('spark.executor.extraClassPath', sparkClassPath) # only for older Spark versions
    # conf.set('spark.driver.extraClassPath', sparkClassPath)
    # conf.set('spark.jars.packages', sparkClassPath) # for Maven users
    # IMPORTANT: pass additional Python modules to each worker here
    spark_context = SparkContext(conf=conf, pyFiles=None)
    # quiet_logs(sc)

    return spark_context


def quiet_logs(spark_context: SparkContext):
    # from https://stackoverflow.com/a/36413124/8510370
    logger = spark_context._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(logger.Level.ERROR)
    logger.LogManager.getLogger("akka").setLevel(logger.Level.ERROR)


sc = init_spark_context()
sqlContext = SQLContext(sc)


# ========================================================================================
# Method 1: define dataframe using spark session read
def method1(spark_context: SparkContext, database_URL: str):
    print('fetching jdbc dataframe...')
    # Create a SparkSession
    spark = SparkSession(spark_context)
    # Create a DataFrame object
    jdbc_df = spark.read \
        .format("jdbc") \
        .option("url", database_URL) \
        .option("dbtable", "RATING") \
        .option("driver", "oracle.jdbc.driver.OracleDriver") \
        .option("fetchSize", "5001") \
        .load()

    return jdbc_df


# ========================================================================================


# ========================================================================================
# Method 2: define dataframe using DataFrameReader interface
def method2(sql_context: SQLContext, database_URL: str, database_properties: dict):
    print('fetching jdbc dataframe...')
    # Create a DataFrameReader interface
    jdbc_df = DataFrameReader(sql_context).option("fetchSize", "5001")
    # Create a DataFrame object
    jdbc_df = jdbc_df.jdbc(url=database_URL,
                           table='RATINGS',
                           # column="SERVICE_ID",
                           # lowerBound="0",
                           # upperBound="4",
                           # numPartitions=4,
                           properties=database_properties)

    return jdbc_df


# ========================================================================================


def main():
    time0 = time.time()

    # Get JDBC DataFrame:

    # jdbc_df = method1(my_sc, db_url)
    jdbc_df = method2(sqlContext, db_url, db_properties)

    services_rdd = jdbc_df.select('MOVIE_ID', 'SERVICE_NAME').rdd.map(tuple)
    print('\nsuccessfully created "services_rdd"')
    for line in services_rdd.take(5):
        print(line)

    ratings_rdd = jdbc_df.select('CLIENT_ID', 'MOVIE_ID', 'RATINGS').rdd.map(tuple)
    print('\nsuccessfully created "ratings_rdd"')
    for line in ratings_rdd.take(5):
        print(line)

    time1 = time.time()
    print("\nexecution time: {runtime:.2f} [sec]".format(runtime=time1 - time0))


if __name__ == '__main__':
    main()

# TODO: Enable parallel execution of SQL statements
# TODO: Select a method (both essentially same, so...)
