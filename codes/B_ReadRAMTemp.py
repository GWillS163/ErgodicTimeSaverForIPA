# Github: GWillS163
# User: 駿清清 
# Date: 08/12/2022 
# Time: 13:35


def readRAMTemp(itemKey, RAMTemp):
    """
    尝试读取内存中已处理过的数据
    :param itemKey:
    :param RAMTemp:
    :return:
    """
    if itemKey in RAMTemp:
        return RAMTemp[itemKey]
    return None


