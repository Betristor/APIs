import requests
import json

from BaiduMapAPI.getAK import getAK


def getDistance(start, end, unit="km"):
    url = "http://dev.virtualearth.net/REST/V1/Routes?wp.0={}&wp.1={}&distanceUnit={}&key={}".format(
        start, end, unit, getAK()["AK"]
    )
    res = requests.get(url)
    json_data = json.loads(res.text)

    if json_data["statusCode"] == 200:
        return json_data["resourceSets"][0]["resources"][0]["travelDistance"]
    else:
        print(json_data["statusDescription"])
        return -1