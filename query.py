import sqlite3 as sql

conn = sql.connect('yelp.db')
c = conn.cursor()

s = """ SELECT category, COUNT(DISTINCT(b.business_id))/ FROM business b
        JOIN category c ON c.business_id = b.business_id
        WHERE food = 1
        GROUP BY category ORDER BY COUNT(DISTINCT(b.business_id))"""

for row in c.execute(s):
    print(row)

conn.close()

