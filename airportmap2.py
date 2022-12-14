#Please Note: If you are having trouble using the above example, please try the one below :

#Prior to performing the below steps, a few packages are to be installed. See below :
- pip install FlightRadarAPI
- pip install pandas
- pip install folium
- pip install geopandas
- pip install matplotlib

##Import modules
import pandas as pd
import folium
import geopandas
import matplotlib.pyplot as plt
from FlightRadar24.api import FlightRadar24API

## Get data, load into dataframe and map
fr_api = FlightRadar24API()
airports = fr_api.get_airports()
df = pd.DataFrame(airports)
geometry = geopandas.points_from_xy(df.lon, df.lat)
gdf = geopandas.GeoDataFrame(df[['name','country', 'lat', 'lon']], geometry=geometry)
geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in gdf.geometry ]
i = 0
for coordinates in geo_df_list:
    if gdf.name[i] == "name":
        type_color = "blue"
    else:
        type_color = "purple"
    
    map.add_child(folium.Marker(location = coordinates,popup =
                                "Name: " + str(gdf.name[i]) + '<br>' +
                                "Country: " + str(gdf.country[i]) + '<br>' +
                                "Latitude: " + str(gdf.lat[i]) + '<br>'
                                "Longitude: " + str(gdf.lon[i]) + '<br>'
                                "Coordinates: " + str(geo_df_list[i]),
                                icon = folium.Icon(color = "%s" % type_color)))
    i = i + 1
## To save the map and open in a web browser or host on your webserver, run:
map.save('map.html')
## The above will save the html file to current working directory. So if you'd like that to be your project directory, be my guest:-)
print(gdf.head())
