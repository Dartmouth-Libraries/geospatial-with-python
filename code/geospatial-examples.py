import folium
# comment 
m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
folium.Marker([40.7128, -74.0060]).add_to(m)
m
