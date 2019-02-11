import sqlite3 as sql
from sqlite3 import Error
import json
import ast
from datetime import datetime as dt
import ijson
import pandas as pd

def create_connection(db_file):
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

conn = create_connection('yelp.db')

reader = pd.read_json('review.json', lines=True, chunksize=10000)
for chunk in reader:
    with conn:
        chunk.to_sql('review', conn, index=False, if_exists='append')

"""
with open('review.json', encoding="UTF-8") as json_file:
    for line_number, line in enumerate(json_file):
        line_as_file = io.StringIO(line)
        # Use a new parser for each line
        json_parser = ijson.parse(line_as_file, chunksize=10000)
        for prefix, t, value in json_parser:
            if prefix == 'review_id':
                review_id = value
            elif prefix == 'user_id':
                user_id = value
            elif prefix == 'business_id':
                business_id = value
            elif prefix == 'stars':
                stars = value
            elif prefix == 'date':
                date = value
            elif prefix == 'text':
                text = value
            elif prefix == 'useful':
                useful = value
            elif prefix == 'funny':
                funny = value
            elif prefix == 'cool':
                cool = value
        review_tuple = (review_id, user_id, business_id, stars, date, text, useful, funny, cool)
        with conn:
            populate_table_review(conn, review_tuple)
"""