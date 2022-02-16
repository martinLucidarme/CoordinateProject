import folium
import pandas as pd
import json
from folium import plugins

df = pd.read_csv('starbucksInLACounty.csv')

with open('laMap.geojson') as f:
    laArea = json.load(f)

# initialize map around LA County
laMap = folium.Map(location=[34.0522, -118.2437], tiles='Stamen Toner', zoom_start=9)

# add the shape of LA County to the map
folium.GeoJson(laArea).add_to(laMap)

# for each row in dataset, plot corresponding lat and long on the map
for i, row in df.iterrows():
    folium.CircleMarker((row.latitude, row.longitude), radius=3, weight=2, color='red', fill_opacity=.5).add_to(laMap)

# save map as html
laMap.save('laPointMap.html')
