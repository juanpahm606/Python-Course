import csv
import pandas as pd
import sqlite3
pd.read_csv("SxSW_2016_Leads_TEST.csv")
conn = sqlite3.connect('test1.sqlite')
df=pd.read_csv("SxSW_2016_Leads_TEST.csv")
df.to_sql('table_test', conn, if_exists='replace')
conn.close()
