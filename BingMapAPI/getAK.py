import os


def getAK(key):
    # Store BingMapAPI information in ~/.bingapirc
    file = "~/.bingapirc"
    file = os.path.expanduser(file)
    with open(file, "r") as f:
        lines = f.readlines()

    # Dict object that stores baidu api information
    info = dict()

    # Extract AK from ~/.bingapirc
    for line in lines:
        line = line.strip()
        if line.startswith():
            info["AK"] = line.split(" ")[1]

    return info
