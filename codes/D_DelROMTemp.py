# Github: GWillS163
# User: 駿清清 
# Date: 08/12/2022 
# Time: 13:36

import os


def delROMTemp(tempPath, tempName):
    filePath = os.path.join(tempPath, tempName)
    if os.path.exists(filePath):
        os.remove(filePath)
    if os.path.exists(tempPath) and len(os.listdir(tempPath)) == 0:
        os.rmdir(tempPath)


delROMTemp(tempPath, tempName)
