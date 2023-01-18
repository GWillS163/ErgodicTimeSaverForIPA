# Github: GWillS163
# User: 駿清清 
# Date: 08/12/2022 
# Time: 17:49

import csv
import os

def saveCsvData(data, filePath):
    """
    保存数据到csv文件
    :param data:
    :param filePath:
    :return:
    """
    fileName = "data.csv"
    fullName = os.path.join(filePath, fileName)
    with open(fullName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


saveCsvData(csvData, csvPath)
