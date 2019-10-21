import folium
import pandas as pd
 
data = pd.read_csv("data.csv")
print(data)
lat = list(data["lat"])
lon = list(data["lon"])
is_ = list(data["is"])
map = folium.Map(prefer_canvas=True, location=[47.6, 21.7], zoom_star=0)
 
fg = folium.FeatureGroup(name="Map")
for lt, ln, n in zip(lat, lon, is_):
    if n == '+':
        fg.add_child(folium.CircleMarker(location=[lt, ln], radius=2,
            popup='asd', fill_color="red", color="red", fill_opacity=1))
    else:
        fg.add_child(folium.CircleMarker(location=[lt, ln], radius=2,
            popup='asd', fill_color='green', color='green', fill_opacity=1))
map.add_child(fg)
 
map.save("map.html")
