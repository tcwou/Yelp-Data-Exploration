"""
import folium
import pandas as pd
import seaborn as sns
from IPython.display import HTML, display

data = pd.read_csv('coordinates.csv')
data.columns = ['business_id', 'latitude', 'longitude']

myMap = folium.Map(location=[48, -102], zoom_start=3)

mapWidth, mapHeight = (400,500) # width and height of the displayed iFrame, in pixels
srcdoc = myMap.HTML.replace('"', '&quot;')
embed = HTML('<iframe srcdoc="{}" '
             'style="width: {}px; height: {}px; display:block; width: 50%; margin: 0 auto; '
             'border: none"></iframe>'.format(srcdoc, mapWidth, mapHeight))
embed
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import pandas as pd
import cartopy.io.img_tiles as cimgt

pd.set_option('display.max_columns', 500)


data = pd.read_csv('eateries.csv')
data.columns = ['business_id', 'latitude', 'longitude', 'city', 'stars', 'category']

print(data['city'].value_counts(ascending=True))

#unique_business = data.groupby('business_id')
#print(unique_business.agg(pd.Series.mode))
