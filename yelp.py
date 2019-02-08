import sqlite3 as sql
from sqlite3 import Error
import json
from pandas.io.json.normalize import nested_to_record
import ast

def create_connection(db_file):
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def populate_db(conn, row):
    s = ''' INSERT INTO business(business_id, name, address, city, state, postal_code, latitude, longitude, stars,
            review_count, is_open, attributes, categories, hours)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(s, row)


json_set = []
data = []
with open('yelp.json', 'r', encoding='utf-8') as f:
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

    first_level_keys = [k for k,v in row['attributes'].items() if v == 'True' or v is True]
    
    try:
        good_for_meal = (ast.literal_eval(row['attributes']['GoodForMeal']))
        good_for_meal_keys = [k for k,v in good_for_meal.items() if v == 'True' or v is True]
    except:
        pass
    try:
        business_parking = (ast.literal_eval(row['attributes']['BusinessParking']))
        business_parking_keys = [k + 'parking' for k, v in business_parking.items() if v == 'True' or v is True]
    except:
        pass
    try:
        ambience = (ast.literal_eval(row['attributes']['Ambience']))
        ambience_keys = [k + 'ambience' for k, v in ambience.items() if v == 'True' or v is True]
    except:
        pass

    return first_level_keys + good_for_meal_keys + business_parking_keys + ambience_keys + first_level_values
print(data[1]['attributes'])
print(process_attributes(data[1]))
print(data[1]['categories'])
print(data[1]['hours'])
def process_hours(row):
    pass

#print(str([k for k,v in data[1]['attributes'].items() if v is True]).replace('[', '').replace(']', ''))

"""
#Create a tuple with data for each column
tuple_list = []
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
        row['is_open'],
        attribute,
        row['categories'],
        hours
        )
        tuple_list.append(row_tuple)
    except Exception as e:
        print(i)

print(tuple_list[0])
print(tuple_list[3])

conn = create_connection('yelp.db')
with conn:
    for row in tuple_list:
        populate_db(conn, row)
"""