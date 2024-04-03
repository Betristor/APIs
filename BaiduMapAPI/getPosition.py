import requests
import json

from BaiduAPI.getAK import getAK


def getPosition(address):
    url = r"http://api.map.baidu.com/place/v2/search?query={}&region=全国&output=json&ak={}".format(
        address, getAK()["AK"]
    )
    res = requests.get(url)
    json_data = json.loads(res.text)

    print(json_data)
    if json_data["status"] == 0:
        lat = json_data["results"][0]["location"]["lat"]  # 纬度
        lng = json_data["results"][0]["location"]["lng"]  # 经度
    else:
        print(json_data["message"])
        return "0,0", json_data["status"]
    return str(lat) + "," + str(lng), json_data["status"]
