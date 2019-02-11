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

sql_create_hours_table = """ CREATE TABLE IF NOT EXISTS hours (
                                business_id text,
                                mon_open text,
                                mon_close text,
                                tue_open text,
                                tue_close text,
                                wed_open text,
                                wed_close text,
                                thu_open text,
                                thu_close text,
                                fri_open text,
                                fri_close text,
                                sat_open text,
                                sat_close text,
                                sun_open text,
                                sun_close text,
                                FOREIGN KEY(business_id) REFERENCES business(business_id) ); """

sql_create_misc_table = """ CREATE TABLE IF NOT EXISTS misc (
                                business_id text,
                                misc text,
                                FOREIGN KEY(business_id) REFERENCES business(business_id) ); """

sql_create_meal_table = """ CREATE TABLE IF NOT EXISTS meal (
                                business_id text,
                                meal text,
                                FOREIGN KEY(business_id) REFERENCES business(business_id) ); """

sql_create_parking_table = """ CREATE TABLE IF NOT EXISTS parking (
                                business_id text,
                                parking text,
                                FOREIGN KEY(business_id) REFERENCES business(business_id) ); """

sql_create_ambience_table = """ CREATE TABLE IF NOT EXISTS ambience (
                                business_id text,
                                ambience text,
                                FOREIGN KEY(business_id) REFERENCES business(business_id) ); """

sql_create_review_table = """ CREATE TABLE IF NOT EXISTS review (
                                review_id text PRIMARY KEY,
                                user_id text,
                                business_id text,
                                stars int,
                                date text,
                                text text,
                                useful int,
                                funny int,
                                cool int,
                                FOREIGN KEY(business_id) REFERENCES business(business_id),
                                FOREIGN KEY(user_id) REFERENCES user(user_id)); """

sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user (
                                user_id text PRIMARY KEY,
                                name text,
                                review_count int,
                                yelping_since text,
                                friends int,
                                useful int,
                                funny int,
                                cool int,
                                fans int,
                                elite int,
                                average_stars real,
                                compliment_hot int,
                                compliment_more int,
                                compliment_profile int,
                                compliment_cute int,
                                compliment_list int,
                                compliment_note int,
                                compliment_plain int,
                                compliment_cool int,
                                compliment_funny int,
                                compliment_writer int,
                                compliment_photos int ); """


conn = create_connection('yelp.db')
if conn is not None:
    create_table(conn, sql_create_business_table)
    create_table(conn, sql_create_category_table)
    create_table(conn, sql_create_hours_table)
    create_table(conn, sql_create_misc_table)
    create_table(conn, sql_create_meal_table)
    create_table(conn, sql_create_parking_table)
    create_table(conn, sql_create_ambience_table)
    create_table(conn, sql_create_review_table)
    create_table(conn, sql_create_user_table)
    conn.commit()
else:
    print("Error cannot create db connection")