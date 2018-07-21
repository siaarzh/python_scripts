import cx_Oracle
import time
from sqlalchemy import create_engine
import pandas as pd

# engine = create_engine('oracle://user:passwrd@localhost:1521/my_oracle_db')
time1 = time.time()
dns = cx_Oracle.makedsn("localhost", "1521", "my_oracle_db")
con = cx_Oracle.connect("user", "passwrd", dns, encoding="UTF-8", nencoding="UTF-16")
print (con.version)
sql = ("SELECT * FROM table_name")s
df_fetch = pd.read_sql(sql, con=con)
time2 = time.time()
print(time2-time1)
con.close()