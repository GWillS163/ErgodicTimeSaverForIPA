# Github: GWillS163
# User: 駿清清 
# Date: 08/12/2022 
# Time: 13:33
import os
import pickle


def load(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def readROMTemp(tempPh, tempNm):
    fullPath = os.path.join(tempPh, tempNm)
    if not os.path.exists(tempPh) or not os.path.isfile(fullPath):
        return {}
    res = load(fullPath)
    return res if isinstance(res, dict) else {}


# tempPath = r"D:\work\长流程优化"
# tempName = r"temp.pytmp"

RAMTemp = readROMTemp(tempPath, tempName)
# print(RAMTemp)
