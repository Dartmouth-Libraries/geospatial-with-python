# point in polygon , geocoding 
# S. Gaughan v1: 2024-07-15

#Visit https://earthquake.usgs.gov/earthquakes/map/?extent=-21.1255,-150.99609&extent=71.80141,-38.67188

# Dartmouth JupyterLab instance: https://jupyterlab.dartmouth.edu/

pip install geopandas
pip install folium

# helpful geojson https://geojson.io/,  create spatial data # coordinates = geojson_data['features'][0]['geometry']['coordinates']

animal_sightings_df = pd.read_csv('/home/jovyan/shared/day08-am/data/animal-sightings.csv')

plt.scatter(animal_sightings_df['longitude'], animal_sightings_df['latitude'], alpha=0.5, edgecolors='w', s=100)
# Show the plot
plt.show()

import matplotlib.pyplot as plt

geodataframe = gpd.GeoDataFrame(animal_sightings_df, geometry=gpd.points_from_xy(animal_sightings_df.longitude, animal_sightings_df.latitude))

# coordinate system / epsg code https://epsg.io/4326

geodataframe.set_crs(epsg=4326, inplace=True)

coordinate = (43.705, -72.288)

latitude = coordinates[1]
longitude = coordinates[0]

m = folium.Map(location=[geodataframe['geometry'].y.mean(), geodataframe['geometry'].x.mean()], zoom_start=8)

for _, row in geodataframe.iterrows():
    folium.Marker(location=[row.geometry.y, row.geometry.x]).add_to(m)
  
import folium 
coordinate = (0,0)
m = folium.Map(location = coordinate, zoom_starts = 25)
folium.Marker(coordinate, popup= 'point of interest').add_to(m) 
m

m = folium.Map(location = [0,0], zoom_start = 2)
folium.Marker([0,0], popup = 'point of interest').add_to(m)
m


###### Paris, Berlin, London
geojson_data = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          2.3486997150556874,
          48.853697962437565
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          -0.1279081740221102,
          51.509466740960534
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          13.392239298152333,
          52.51910798875255
        ],
        "type": "Point"
      }
    }
  ]
}

m = folium.Map(location = (0,0), zoom_start = 2)
for x in range(3):
    coordinates = geojson_data['features'][x]['geometry']['coordinates']
    latitude = coordinates[1]
    longitutde = coordinates[0]
    folium.Marker([latitude,longitutde], popup = 'point of interest').add_to(m)
m

#########################
# geocoding 
pip install geopy
from geopy.geocoders import Nominatim

cities = ["Boston", "New York", "Los Angeles", "San Francisco"]

geolocator = Nominatim(user_agent="city_geocoder")
city_data=[]

for city in cities:
    location = geolocator.geocode(city)
    if location:
        city_data.append({"City":city, "Latitude":location.latitude, "Longitude":location.longitude})
        df = pd.DataFrame(city_data)
print(df)

mapcenter=[37,-95]
city_map = folium.Map(location=mapcenter, zoom_start=4)

for index, row in df.iterrows():
    folium.Marker(location=[row["Latitude"], row["Longitude"]], popup=row["City"]).add_to(city_map)
    
    city_map
    
    zip_path = '/home/jovyan/shared/day08-am/data/ne_110m_admin_0_countries.zip'
    
    gdf_countries = gpd.read_file(zip_path)
    gdf_countries.head()
    
    canada = gdf_countries[gdf_countries['ADMIN']=='Canada']
canada.plot()
plt.show()

canada_3395 = canada.to_crs(epsg=3395)
canada_buffer = canada_3395.copy()
canada_buffer.head()
canada_buffer['geometry'] = canada_3395['geometry'].buffer(100000)
canada_buffer.plot()
plt.show()

points = pd.read_csv('/home/jovyan/shared/day08-am/data/bear-sightings.csv')

polygons_path = "/home/jovyan/shared/day08-am/data/nationalparks_ak.zip"

polygons = gpd.read_file(polygons_path)

points = gpd.GeoDataFrame(points, geometry=gpd.points_from_xy(points.longitude, points.latitude))
points.head(2)
points.crs='EPSG:4326'
points = points.to_crs(polygons.crs)
points.crs.to_epsg()
polygons.plot(facecolor='none')
points.plot(ax=plt.gca())
points.plot(color='blue',ax=plt.gca())
plt.show()
    
    
points.crs='EPSG:4326'
points = points.to_crs(polygons.crs)
points.crs.to_epsg()
    
    
points_in_polygons=gpd.sjoin(points,polygons, predicate='within')
    
points_in_polygons.head(5)
    
# create a folium map, complete with in-notebook zoom tools
map = folium.Map(location=[62.65822, -148.95602],
    zoom_start=5,
    control_scale=True)

folium.GeoJson(polygons).add_to(map)
# loop through points
for index, row in points.iterrows():
    folium.CircleMarker(location=[ row.latitude,row.longitude], radius =5).add_to(map)
# loop through points in polygons, color them gray
for index, row in points_in_polygons.iterrows():
    folium.CircleMarker(location=[ row.latitude,row.longitude], color = 'gray',fill=True, fill_opacity=1).add_to(map)
# show the map
map

############
pip install geopy
pip install geopy from geopy.geocoders import Nominatim

cities = ["Boston", "New York", "Los Angeles", "San Francisco"]

geolocator = Nominatim(user_agent="city_geocoder") city_data=[]

for city in cities: location = geolocator.geocode(city) if location: city_data.append({"City":city, "Latitude":location.latitude, "Longitude":location.longitude}) df = pd.DataFrame(city_data) print(df)

mapcenter=[37,-95] city_map = folium.Map(location=mapcenter, zoom_start=4)

for index, row in df.iterrows(): folium.Marker(location=[row["Latitude"], row["Longitude"]], popup=row["City"]).add_to(city_map)

city_map

