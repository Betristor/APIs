import os


def getAK():
    # Store baiduAPI information in ~/.baiduapirc
    file = "~/.baiduapirc"
    file = os.path.expanduser(file)
    with open(file, "r") as f:
        lines = f.readlines()

    # Dict object that stores baidu api information
    info = dict()

    # Extract AK from ~/.baiduapirc
    for line in lines:
        line = line.strip()
        if line.startswith("key"):
            info["AK"] = line.split(" ")[1]

    return info
