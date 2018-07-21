"""
UPSERT METHOD FOR POSTGRESQL TABLES:

Given two identically defined tables this function performs the postgreSQL UPSERT method:
    1 UPDATE table1 ... FROM table2 ...;
    2 INSERT INTO table1 ... FROM table2 ON CONFLICT ...;

"""

import psycopg2
from config import config


def upsert(**kwargs):

    url = "postgres://{user}:{password}@{host}/{database}".format(**kwargs)
    try:
        conn = psycopg2.connect(url)

        upsert_query = """UPDATE {table}
                            SET "CLIENT_ID" = {table_secondary}."CLIENT_ID",
                                recommendations = {table_secondary}.recommendations 
                            FROM {table_secondary}
                            WHERE {table}."CLIENT_ID" = {table_secondary}."CLIENT_ID";
                        
                          INSERT INTO {table} ("CLIENT_ID", recommendations)
                            SELECT *
                            FROM {table_secondary}
                            ON CONFLICT ("CLIENT_ID") DO NOTHING;""".format(**kwargs)

        cur = conn.cursor()
        cur.execute(upsert_query)
        conn.commit()
        conn.close()
    except Exception as e:
        raise e

params = config('configuration.ini', 'postgresql')
upsert(**params)