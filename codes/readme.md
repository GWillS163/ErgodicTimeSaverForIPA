# ⚠️注意
如果你要拷贝本项目的代码到IPA中使用，请注意去掉以下注释，否则无法运行。

IPA 中使用: 去掉运行注释
项目测试时: 打开运行注释


- `codes/A_ReadROMTemp.py`
  ```python
  RAMTemp = readROMTemp(tempPath, tempName)
  ```

- `codes/B_ReadRAMTemp.py`
  ```python
  itemData = readRAMTemp(itemKey, RAMTemp)
  ```
- `codes/C_AddToROMTemp.py`
  ```python
  RAMTemp = addToROMTemp(itemKey, itemData, RAMTemp, tempPath, tempName)
  ```
- `codes/D_DelROMTemp.py`
  ```python
  delROMTemp(tempPath, tempName)
  ```