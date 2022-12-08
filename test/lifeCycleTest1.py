from envConf import *


# 模拟了第一次程序运行的情况，遍历两次后中断
class ErgodicLifeCycle(unittest.TestCase):

    def test_1_D_AddToRAMTemp(self):
        print("删除ROMTemp")
        self.assertEqual(delROMTemp(tempPath, tempName), None)

    def test_2_A_ReadROMTemp(self):
        # 第一次运行程序时，ROMTemp为空
        print("第一次运行程序时，ROMTemp为空")
        self.assertEqual(None,
                         readROMTemp(tempPath, tempName))

    def test_3_B_ReadRAMTemp(self):
        # 第一次运行程序时，内存中没有重复值
        print("第一次运行程序时，内存中没有重复值")
        keyStr = "a"
        RAMTemps = {}
        self.assertEqual(None,
                         readRAMTemp(keyStr, RAMTemps))

    # 遍历的第二次运行
    def test_4_C_AddToROMTemp(self):
        # 第一次运行程序时，ROMTemp为空， 新写入ROMTemp
        print("第一次运行程序时，ROMTemp为空， 新写入ROMTemp")
        itemKey = "a"
        itemData = 1
        RAMTemps = {}
        RAMTemps = addToROMTemp(itemKey, itemData, tempPath, tempName, RAMTemps)
        self.assertEqual(RAMTemps, {"a": 1})

    def test_5_B_ReadRAMTemp(self):
        # 第一次运行程序时，内存中没有重复值
        print("第一次运行程序时，内存中没有重复值")
        keyStr = "b"
        RAMTemps = {}
        self.assertEqual(None,
                         readRAMTemp(keyStr, RAMTemps))

    def test_6_C_AddToROMTemp(self):
        # 第一次运行程序时，ROMTemp为空， 新写入ROMTemp
        print("第一次运行程序时，ROMTemp为空， 新写入ROMTemp")
        itemKey = "b"
        itemData = 2
        RAMTemps = {"a": 1}
        addToROMTemp(itemKey, itemData, tempPath, tempName, RAMTemps)
        self.assertEqual({"a": 1, "b": 2}, RAMTemps)
        self.assertEqual({"a": 1, "b": 2}, readROMTemp(tempPath, tempName))


if __name__ == '__main__':
    unittest.main()
