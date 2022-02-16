import folium
import pandas as pd
import json
from folium import plugins

df = pd.read_csv('starbucksInLACounty.csv')

with open('laMap.geojson') as f:
    laArea = json.load(f)

# initialize map around LA County
laMap = folium.Map(location=[34.0522, -118.2437], tiles='Stamen Toner', zoom_start=9)

# group the starbucks dataframe by zip code and count the number of stores in each zip code
numStoreSeries = df.groupby('zip').count().id

# create empty dataframe
numStoreByZip = pd.DataFrame()

# store zipcode and numStores column:
numStoreByZip['zipcode'] = [str(i) for i in numStoreSeries.index]
numStoreByZip['numStores'] = numStoreSeries.values

# draw the choropleth map. These are the key components:
# --geo_path: the geojson which you want to draw on the map [in our case it is the zipcodes in LA County]

# --data: the pandas dataframe which contains the zipcode information
# AND the values of the variable you want to plot on the choropleth

# --columns: the columns from the dataframe that you want to use
# [this should include a geospatial column [zipcode] and a variable [numStores]

# --key_on: the common key between one of your columns and an attribute in the geojson.
# This is how python knows which dataframe row matches up to which zipcode in the

choropleth = folium.Choropleth(geo_data='laZips.geojson', data=numStoreByZip,
                               columns=['zipcode', 'numStores'],
                               key_on='feature.properties.zipcode',
                               fill_color='YlGn',
                               fill_opacity=1
                               )
choropleth.add_to(laMap)
laMap.save('laChoropeth.html')
