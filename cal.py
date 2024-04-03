import pandas as pd
from geopy.distance import geodesic

if __name__ == "__main__":
    data = pd.read_csv("Routes.csv")
    lat_lon = pd.read_csv("china_capital.csv", index_col=0)
    res = []
    for i in range(0, len(data)):
        startName = data.iloc[i, 0]
        startlat = lat_lon.loc[startName, "Latitude"]
        startlon = lat_lon.loc[startName, "Longitude"]
        
        endName = data.iloc[i, 1]
        endlat = lat_lon.loc[endName, "Latitude"]
        endlon = lat_lon.loc[endName, "Longitude"]
        dist = geodesic((startlat, startlon), (endlat, endlon)).km

        res.append([startName, endName, dist])
    pd.DataFrame(res).to_csv(
        "result.csv",
        header=["Start_Zone", "End_Zone", "Distance"],
        index=None,
        encoding="utf-8"
    )
