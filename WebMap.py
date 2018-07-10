import folium
import pandas

# Reading in the 'worldcapitals.csv' file
data = pandas.read_csv("worldcapitals.csv", encoding ="latin1")
# Creates a folium Map object
map = folium.Map(location=[0, 0], zoom_start=2, tiles ="Mapbox Bright")

# First Layer for world capitals
fgwc = folium.FeatureGroup(name="World Capitals")

# Various lists created from the data
city_name = list(data.ix[:, 1])
country = list(data.ix[:, 2])
lat = list(data["Latitude"])
long = list(data["Longitude"])

# Loops through all the lists and creates children for the layer
# Had to parse through HTML as there was a bug in the list if it had apostrophes in the entries
for lt, lg, city, cy in zip(lat, long, city_name, country):
     fgwc.add_child(folium.CircleMarker(location=[lt, lg], radius=6, color='red', fill=True,
                                      popup=folium.Popup(str(city) + ', ' + str(cy), parse_html=True)))

# Second Layer for the Population
fgp = folium.FeatureGroup(name="Population")
# Reading in a json file using the GeoJson method in folium
# Then showing population through colours
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000
                                                      else 'red'}))

# Adding the layers to the map
map.add_child(fgwc)
map.add_child(fgp)
# Used the LayerControl method to be able to control the layers
map.add_child(folium.LayerControl())
# Saved the map into a HTML file so you can view it
map.save("Map1.html")