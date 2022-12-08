# Github: GWillS163
# User: 駿清清 
# Date: 08/12/2022 
# Time: 13:33
import os
import pickle


def load(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def readROMTemp(tempPath, tempName):
    if not os.path.exists(tempPath):
        return None
    fullPath = os.path.join(tempPath, tempName)
    if os.path.isfile(fullPath):
        return load(fullPath)

