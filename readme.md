# 长遍历优化 - ErgodicTimeSaver
## 🖼️提出背景
RPA开发场景中，有6w条数据需要使用IPA进行处理，但每条需5s处理时间，共需要84小时.
若在82小时内有中断，则整个流程进度清空，需要重新来过。即使每条处理99%的成功率，连续成功处理100次后，成功率也仅剩36%。
<div  align="center" >
<img src="res/img.png" style="width: 50%" alt="流程">
</div>

## ✨解决效果
- ### 断点续行：
> 在遍历（Ergodic）内每次处理时，对处理后的数据进行Dump操作，进度文件（Temp）保存在硬盘（ROM）中，下次运行即可快速跳过已处理部分。

- ### 数据去重：
> 重复遇到已处理后的数据，则通过内存（RAM）中快速得到已处理关键值的信息。

## 🐿️快速体验
> 运行`RPAMock/xxx.rpa`，此demo内含有两个子流程，可直接运行（需修改变量的保存地址）。

## 💭解决思路
在整个流程中，找到四个位置进行优化：
1. 读取数据后，遍历开始前：读取上一次运行时硬盘中的临时文件, 加载到内存中。
2. 每次遍历开始: 将每次遍历的数据与内存中的数据进行对比，若已存在，则使用已有数据，跳过本次处理
3. 每次遍历最后: 将每次处理后的数据进行Dump操作，保存到硬盘中。
4. 遍历结束后: 将临时文件删除。

## 📝代码实现
主要分为4个步骤

### `A_ReadROMTemp.py`
> 遍历前读取硬盘进度缓存文件，并将遍历前已处理部分恢复

### `B_ReadRAMTemp.py`
>遍历中每次处理新item时，从内存中查找曾处理过的部分，直接返回数据(0.1s)，而非再次处理(5s+)

### `C_AddToROMTemp.py`
> 遍历每次处理item后，将进度保存至硬盘&内存中；

### `D_DelROMTemp.py`
> 若此循环处理完成，删除本地的临时文件

<div  align="center" >
<img src="res/img_1.png" style="width: 50%" alt="新增模块后流程">
</div>

## 测试代码
test/目录下,共有两个文件，模拟了ErgodicTimeSaver周期的两个测试用例
- `test/lifeCycleTest1.py`: 模拟了第一次程序运行的情况，遍历两次后中断
- `test/lifeCycleTest2.py`: 模拟了第二次程序运行的情况，读取硬盘缓存，直接跳过已处理部分，直至运行成功。

## 🍀使用方式
1. 新增3个变量
  <div  align="center" >
  <img src="res/img3.png" style="width: 50%" alt="新增变量">
  </div>
2. codes文件夹下的四个模块代码，分别放在4个模块中
  <div  align="center" >
  <img src="res/img_4.png" style="width: 50%" alt="放置新代码">
  </div>
3. 四个模块的输入输出，参考codes/文件夹下的四个模块内最后的执行行（如下. 等号左边是输出，函数里面是输入:D，看不懂的话直接运行RPAMock/xxx.rpa文件吧）。

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
  
 4. 最后，你还可以直接运行RPAMock/xxx.rpa文件，进行快速上手体验（本文配图所在的项目）。
