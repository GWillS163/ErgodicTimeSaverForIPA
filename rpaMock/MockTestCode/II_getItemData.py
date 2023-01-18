# 本文件很可能是js脚本，仅用python模块示意

import random
import time


def getDataUnstable(itemKey: int):
    """
    通过itemKey获取数据，但是40%的概率会出现异常
    :param itemKey:
    :return:
    """
    mockData = [i * itemKey for i in range(4)]
    if random.randint(0, 10) >= 9:
        raise Exception('Mock Exception')
    time.sleep(3)
    return mockData


# itemKey= 38
itemData = getDataUnstable(itemKey)
print(itemData)
