#Prior to performing the below steps, a few packages are to be installed. See below :
- pip install FlightRadarAPI
- pip install pandas
- pip install folium

- import pandas as pd
- import folium

# Step 1 (Get the required data. In this case, it would be the airports data, but any other data from the api can be pulled in.)
- from FlightRadar24.api import FlightRadar24API
- fr_api = FlightRadar24AP()
- airports = fr_api.get_airports()

# Step 2 (Place the data into a DataFrame and confirm output with print statement.)
- df = pd.DataFrame(airports)
- print(df)

# Step 3 (Select required data from DataFrame.)
- df = df[["lat", "lon", "name"]]

# Step 4 (Define map data points and start zoom-level.)
- map = folium.Map(location=[df.lat.mean(), df.lon.mean()], zoom_start=14, control_scale=True)

# Step 5 (Run code.)
- Type : map and click run or enter.

  

