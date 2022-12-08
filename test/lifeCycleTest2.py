from envConf import *


# 模拟了中断后，第二次运行程序的情况。并将程序继续运行下去
class ErgodicLifeCircle2(unittest.TestCase):

    def test_1_A_ReadROMTemp2(self):
        # 中断后, 第重新二次运行程序时，ROMTemp 读取到上次遗留的值
        print("中断后, 第重新二次运行程序时，ROMTemp 读取到上次遗留的值")
        self.assertEqual({'a': 1, 'b': 2},
                         readROMTemp(tempPath, tempName))

    def test_2_B_ReadRAMTemp(self):
        # 内存中读取到了重复值
        print("二次运行程序时，内存中读取到了重复值")
        keyStr = "b"
        RAMTemps = {"a": 1, "b": 2}
        self.assertEqual(2,
                         readRAMTemp(keyStr, RAMTemps))

    # def test_3_C_AddToROMTemp(self):
    #     # 重复值，不写入ROMTemp
    #     print("二次运行程序时，重复值，不写入ROMTemp")
    #     pass

    def test_4_D_AddToRAMTemp(self):
        print("删除ROMTemp")
        self.assertEqual(delROMTemp(tempPath, tempName), None)


if __name__ == '__main__':
    unittest.main()
