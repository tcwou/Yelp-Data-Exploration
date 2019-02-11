import sqlite3 as sql
from sqlite3 import Error
import json
from pandas.io.json.normalize import nested_to_record
import ast
from datetime import datetime as dt

def create_connection(db_file):
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def populate_table_business(conn, row):
    s = ''' INSERT INTO business(business_id, name, address, city, state, postal_code, latitude, longitude, stars,
            review_count, is_open)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(s, row)

def populate_table_category(conn, row):
    s = ''' INSERT INTO category(business_id, food, category)
            VALUES(?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(s, row)

def populate_table_hours(conn, row):
    s = ''' INSERT INTO hours(business_id, mon_open, mon_close, tue_open, tue_close, wed_open, wed_close, thu_open,
            thu_close, fri_open, fri_close, sat_open, sat_close, sun_open, sun_close)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(s, row)

def populate_table_misc(conn, row):
    s = ''' INSERT INTO misc(business_id, misc)
            VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(s, row)

def populate_table_meal(conn, row):
    s = ''' INSERT INTO meal(business_id, meal)
            VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(s, row)

def populate_table_parking(conn, row):
    s = ''' INSERT INTO parking(business_id, parking)
            VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(s, row)

def populate_table_ambience(conn, row):
    s = ''' INSERT INTO ambience(business_id, ambience)
            VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(s, row)

json_set = []
data = []
with open('business.json', 'r', encoding='utf-8') as f:
    for row in f:
        json_set.append(row)
    for row in json_set:
        data.append(json.loads(row))


"""
from pandas.io.json import json_normalize

norm = json_normalize(data)
print(norm.columns)

columns = ['address', 'attributes', 'attributes.AcceptsInsurance',
       'attributes.AgesAllowed', 'attributes.Alcohol', 'attributes.Ambience',
       'attributes.BYOB', 'attributes.BYOBCorkage', 'attributes.BestNights',
       'attributes.BikeParking', 'attributes.BusinessAcceptsBitcoin',
       'attributes.BusinessAcceptsCreditCards', 'attributes.BusinessParking',
       'attributes.ByAppointmentOnly', 'attributes.Caters',
       'attributes.CoatCheck', 'attributes.Corkage',
       'attributes.DietaryRestrictions', 'attributes.DogsAllowed',
       'attributes.DriveThru', 'attributes.GoodForDancing',
       'attributes.GoodForKids', 'attributes.GoodForMeal',
       'attributes.HairSpecializesIn', 'attributes.HappyHour',
       'attributes.HasTV', 'attributes.Music', 'attributes.NoiseLevel',
       'attributes.Open24Hours', 'attributes.OutdoorSeating',
       'attributes.RestaurantsAttire', 'attributes.RestaurantsCounterService',
       'attributes.RestaurantsDelivery', 'attributes.RestaurantsGoodForGroups',
       'attributes.RestaurantsPriceRange2',
       'attributes.RestaurantsReservations',
       'attributes.RestaurantsTableService', 'attributes.RestaurantsTakeOut',
       'attributes.Smoking', 'attributes.WheelchairAccessible',
       'attributes.WiFi', 'business_id', 'categories', 'city', 'hours',
       'hours.Friday', 'hours.Monday', 'hours.Saturday', 'hours.Sunday',
       'hours.Thursday', 'hours.Tuesday', 'hours.Wednesday', 'is_open',
       'latitude', 'longitude', 'name', 'postal_code', 'review_count', 'stars',
       'state'],
"""

def process_attributes(row):
    try:
        first_level_keys = [k for k,v in row['attributes'].items() if v == 'True' or v is True]
    except:
        first_level_keys = []
    try:
        good_for_meal = (ast.literal_eval(row['attributes']['GoodForMeal']))
        good_for_meal_keys = [k for k,v in good_for_meal.items() if v == 'True' or v is True]
    except:
        good_for_meal_keys = []
    try:
        business_parking = (ast.literal_eval(row['attributes']['BusinessParking']))
        business_parking_keys = [k + 'parking' for k, v in business_parking.items() if v == 'True' or v is True]
    except:
        business_parking_keys = []
    try:
        ambience = (ast.literal_eval(row['attributes']['Ambience']))
        ambience_keys = [k + 'ambience' for k, v in ambience.items() if v == 'True' or v is True]
    except:
        ambience_keys = []

    return first_level_keys, good_for_meal_keys, business_parking_keys, ambience_keys


#print(data[15600]['attributes'])
print(process_attributes(data[15600]))
"""
unique_at = []
for row in data:
    try:
        row_at = [k for k,v in row['attributes'].items()]
    except:
        row_at = []
    unique_at += [at for at in row_at if at not in unique_at]
"""

hours = data[1]['hours']
print(hours)

def process_hours(row):
    # Extract times to HH:mm format
    try:
        mon = row['hours']['Monday'].split('-')
        mon_open = dt.strftime(dt.strptime(mon[0], '%H:%M'), '%H:%M')
        mon_close = dt.strftime(dt.strptime(mon[1], '%H:%M'), '%H:%M')
    except (TypeError, KeyError) as e:
        mon_open = None
        mon_close = None
    try:
        tue = row['hours']['Tuesday'].split('-')
        tue_open = dt.strftime(dt.strptime(tue[0], '%H:%M'), '%H:%M')
        tue_close = dt.strftime(dt.strptime(tue[1], '%H:%M'), '%H:%M')
    except (TypeError, KeyError) as e:
        tue_open = None
        tue_close = None
    try:
        wed = row['hours']['Wednesday'].split('-')
        wed_open = dt.strftime(dt.strptime(wed[0], '%H:%M'), '%H:%M')
        wed_close = dt.strftime(dt.strptime(wed[1], '%H:%M'), '%H:%M')
    except (TypeError, KeyError) as e:
        wed_open = None
        wed_close = None
    try:
        thu = row['hours']['Thursday'].split('-')
        thu_open = dt.strftime(dt.strptime(thu[0], '%H:%M'), '%H:%M')
        thu_close = dt.strftime(dt.strptime(thu[1], '%H:%M'), '%H:%M')
    except (TypeError, KeyError) as e:
        thu_open = None
        thu_close = None
    try:
        fri = row['hours']['Friday'].split('-')
        fri_open = dt.strftime(dt.strptime(fri[0], '%H:%M'), '%H:%M')
        fri_close = dt.strftime(dt.strptime(fri[1], '%H:%M'), '%H:%M')
    except (TypeError, KeyError) as e:
        fri_open = None
        fri_close = None
    try:
        sat = row['hours']['Saturday'].split('-')
        sat_open = dt.strftime(dt.strptime(sat[0], '%H:%M'), '%H:%M')
        sat_close = dt.strftime(dt.strptime(sat[1], '%H:%M'), '%H:%M')
    except (TypeError, KeyError) as e:
        sat_open = None
        sat_close = None
    try:
        sun = row['hours']['Sunday'].split('-')
        sun_open = dt.strftime(dt.strptime(sun[0], '%H:%M'), '%H:%M')
        sun_close = dt.strftime(dt.strptime(sun[1], '%H:%M'), '%H:%M')
    except (TypeError, KeyError) as e:
        sun_open = None
        sun_close = None
    return (row['business_id'], mon_open, mon_close, tue_open, tue_close, wed_open, wed_close, thu_open, thu_close,
            fri_open, fri_close, sat_open, sat_close, sun_open, sun_close)
hours_list = []
for row in data:
    hours_tuple = process_hours(row)
    hours_list.append(hours_tuple)
print(hours_list[:3])
#print(str([k for k,v in data[1]['attributes'].items() if v is True]).replace('[', '').replace(']', ''))

misc_list = []
meal_list = []
parking_list = []
ambience_list = []
for row in data:
    misc, meal, parking, ambience = process_attributes(row)
    for item in misc:
        misc_tuple = (row['business_id'], item)
        misc_list.append(misc_tuple)
    for item in meal:
        meal_tuple = (row['business_id'], item)
        meal_list.append(meal_tuple)
    for item in parking:
        parking_tuple = (row['business_id'], item)
        parking_list.append(parking_tuple)
    for item in ambience:
        ambience_tuple = (row['business_id'], item)
        ambience_list.append(ambience_tuple)


#Create a tuple with data for each column
business_list = []
i = -1
for row in data:
    i += 1
    try:
        attribute = str(list(row['attributes'].keys())).replace('[', '').replace(']', '')
    except:
        attribute = None
    try:
        hours = str(list(row['hours'].keys())).replace('[', '').replace(']', '')
    except:
        hours = None
    try:
        row_tuple = (
        row['business_id'],
        row['name'],
        row['address'],
        row['city'],
        row['state'],
        row['postal_code'],
        row['latitude'],
        row['longitude'],
        row['stars'],
        row['review_count'],
        row['is_open']
        )
        business_list.append(row_tuple)
    except Exception as e:
        print(i)

category_list = []
for row in data:
    food = 0
    try:
        row_list = row['categories'].split(', ')
        if 'Restaurants' in row_list:
            food = 1
            row_list.remove('Restaurants')
        if 'Food' in row_list:
            food = 1
            row_list.remove('Food')
    except:
        row_list = []
    for category in row_list:
        row_tuple = (row['business_id'], food, category)
        category_list.append(row_tuple)
print(len(data))
print(len(category_list))

conn = create_connection('yelp.db')
with conn:
    for row in business_list:
        populate_table_business(conn, row)
    for row in category_list:
        populate_table_category(conn, row)
    for row in hours_list:
        populate_table_hours(conn, row)
    for row in misc_list:
        populate_table_misc(conn, row)
    for row in meal_list:
        populate_table_meal(conn, row)
    for row in parking_list:
        populate_table_parking(conn, row)
    for row in ambience_list:
        populate_table_ambience(conn, row)
