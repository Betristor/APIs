import requests
import json

from BaiduMapAPI.getAK import getAK
from BaiduMapAPI.getPosition import getPosition


def getDistance(start, end):
    url = "https://api.map.baidu.com/directionlite/v1/driving?origin={}&destination={}&ak={}".format(
        start, end, getAK()["AK"]
    )
    res = requests.get(url)
    json_data = json.loads(res.text)

    if json_data["status"] == 0:
        return json_data["result"]["routes"][0]["distance"]
    else:
        print(json_data["message"])
        return -1


def calcDistance(startName, endName):
    start, status1 = getPosition(startName)
    end, status2 = getPosition(endName)
    if status1 == 0 and status2 == 0:
        return getDistance(start, end)
    else:
        return -1
