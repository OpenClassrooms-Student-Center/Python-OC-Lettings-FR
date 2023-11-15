import sqlite3
import pandas as pd


path_db = "oc-lettings-site.sqlite3"
path_csv = "data_csv/"
 
 
def data_transfer(src, dst):
    '''Transfer datas from source tables in sqlite3 and update to CSV and write
       in destination tables in sqlite3'''
    # Extract from table source :
    con = sqlite3.connect(path_db)
    data = pd.read_sql_query(f"SELECT * FROM {src}", con)
    con.close()
 
    # CSV naming
    name = src
    new = name.split('_')
    new_name = new[-1]
    csv = path_csv + f'{new_name}.csv'
 
    # Transform and save to CSV
    data.to_csv(csv, index=False)
 
    # Transfer to destination tables
    con = sqlite3.connect(path_db)
    data = pd.read_csv(csv)
    data.to_sql(dst, con, if_exists='replace', index=False)
    con.close()
 
 
data_transfer('oc_lettings_site_address', 'lettings_address')
data_transfer('oc_lettings_site_profile', 'profiles_profile')
data_transfer('oc_lettings_site_letting', 'lettings_letting')