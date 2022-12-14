# AirportMap
This is a python program illustrating all the airports across the planet. It can be run in a jupyter interactive lab and can also be verified in a python interpreter.

# Below is an example of what this looks like:

![image](https://user-images.githubusercontent.com/101802030/183252346-dd73c805-b1ed-4cde-9514-3dadcbc2984e.png)
![image](https://user-images.githubusercontent.com/101802030/183252293-65eb58e7-ffad-4283-b88e-ed42e9c6c3ab.png)

# Open a notebook in jupyter labs and run the following code :

- pip install pandas
- pip install folium
- pip install FlightRadarAPI

- import pandas as pd
- import folium
- from FlightRadar24.api import FlightRadar24API

- fr_api = FlightRadar24API()
- airports = fr_api.get_airports()
- df = pd.DataFrame(airports)
- print(df)

- df = df[["lat", "lon", "name"]]
- map = folium.Map(location=[df.lat.mean(), df.lon.mean()], zoom_start=14, control_scale=True) # The zoom-start level may be adjusted to your specification.
- map

# Please note : The Jupyter lab interactive environment can be found here - https://www.anaconda.com/products/distribution.
# Please feel free to set it up in your environment. It is compatible with most web browsers.

# A view of what the new layout looks like :
![image](https://user-images.githubusercontent.com/101802030/183876214-e738577c-8668-462b-aac0-41386fde4761.png)

