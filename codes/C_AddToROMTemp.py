# Github: GWillS163
# User: 駿清清 
# Date: 08/12/2022 
# Time: 13:35
import pickle
import os


def dump(ramTemp, tempPath):
    with open(tempPath, "wb") as f:
        pickle.dump(ramTemp, f)


def addToROMTemp(itemKey, itemData, tempPath, tempName, RAMTmp):
    # 尝试读取ROMTemp
    if not os.path.exists(tempPath):
        os.makedirs(tempPath)
    tempPath = os.path.join(tempPath, tempName)

    # RAMTemp 增加
    RAMTmp.update({itemKey: itemData})
    # ROMTemp 重写
    dump(RAMTmp, tempPath)
    return RAMTmp

ramTemp = addToROMTemp(itemKey, itemData, tempPath, tempName, RAMTemp)
