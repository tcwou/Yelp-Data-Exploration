# Create tables
import sqlite3 as sql
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

"""
business_id:1SWheh84yJXfytovILXOAQ
name:Arizona Biltmore Golf Club
address:2818 E Camino Acequia Drive
city:Phoenix
state:AZ
postal_code:85016
latitude:33.5221425
longitude:-112.0184807
stars:3
review_count:5
is_open:0
attributes:{} 1 item
GoodForKids:False
categories:Golf, Active Life
hours:null
"""


database = 'yelp.db'
sql_create_business_table = """ CREATE TABLE IF NOT EXISTS business (
                                business_id text PRIMARY KEY,
                                name text,
                                address text,
                                city text,
                                state text,
                                postal_code integer,
                                latitude real,
                                longitude real,
                                stars real,
                                review_count integer,
                                is_open integer ); """

sql_create_category_table = """ CREATE TABLE IF NOT EXISTS category (
                                business_id text,
                                food int,
                                category text,
                                FOREIGN KEY(business_id) REFERENCES business(business_id) ); """


conn = create_connection('yelp.db')
if conn is not None:
    create_table(conn, sql_create_business_table)
    create_table(conn, sql_create_category_table)
    conn.commit()
else:
    print("Error cannot create db connection")