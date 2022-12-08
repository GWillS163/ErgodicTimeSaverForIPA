# Github: GWillS163
# User: 駿清清 
# Date: 08/12/2022 
# Time: 13:35


def readRAMTemp(itemKey, RAMTmp):
    """
    尝试读取内存中已处理过的数据
    :param itemKey:
    :param RAMTmp:
    :return:
    """
    if not RAMTmp:
        return None
    if itemKey in RAMTmp:
        return RAMTmp[itemKey]
    return None

# itemKey = 1
itemData = readRAMTemp(itemKey, RAMTemp)
