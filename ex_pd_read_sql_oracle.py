import cx_Oracle
import pandas as pd
import time


db_dsn = cx_Oracle.makedsn(host='127.0.0.1',
                           port='1521',
                           sid='my_oracle_db')
conn = cx_Oracle.connect(user='user',
                         password='passwrd',
                         dsn=db_dsn,
                         encoding='UTF-8',
                         nencoding='UTF-16')

time0 = time.time()
# read services into dataframe
sql_query = "SELECT * " \
            "FROM " \
            "(SELECT DISTINCT SERVICE_ID, SERVICE_NAME " \
            "FROM RATING WHERE ROWNUM <= 10000) " \
            "WHERE ROWNUM <= 500"
services_df = pd.read_sql(sql=sql_query, con=conn)
# read ratings into dataframe
sql_query = "SELECT  /*+ parallel(a,16)*/ CUSTOMER_ID, SERVICE_ID, RATING " \
            "FROM RATING a " \
            "WHERE ROWNUM <= 1000"
ratings_df = pd.read_sql(sql=sql_query, con=conn)

print(services_df.head())
print(ratings_df.head())
time1 = time.time()
print("execution time: {runtime:.2f} [sec]".format(runtime=time1-time0))