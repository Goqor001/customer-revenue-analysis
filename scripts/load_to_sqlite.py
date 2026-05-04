import pandas as pd
import sqlite3

df = pd.read_csv(r"data\clean_sales_data.csv")

conn = sqlite3.connect("sales.db")

df.to_sql("sales",conn, if_exists="replace",index=False)