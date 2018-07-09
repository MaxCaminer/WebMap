import folium
import pandas
data = pandas.read_csv("worldcapitals.csv", encoding = "latin1")
d1 = data.loc[:, "Name":"Longitude"]


map = folium.Map(location=[0, 0], zoom_start=2, tiles ="Mapbox Bright")

city_name = list(data.ix[:, 1])
country = list(data.ix[:, 2])
lat = list(data["Latitude"])
long = list(data["Longitude"])



fg = folium.FeatureGroup(name= "World Capitals")

for lt, lg, city, cy in zip(lat, long, city_name, country):
     fg.add_child(folium.CircleMarker(location=[lt, lg], radius=2, fill=True, popup=folium.Popup(str(city) + ', ' + str(cy), parse_html=True), icon=folium.Icon(color='black')))

map.add_child(fg)

map.save("Map1.html")