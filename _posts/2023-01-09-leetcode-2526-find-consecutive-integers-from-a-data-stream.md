--- 
layout      : single
title       : LeetCode 2526. Find Consecutive Integers from a Data Stream
tags        : LeetCode Medium Design
---
雙周賽95。

# 題目
有一個整數數據流，實作一個資料結構來檢查資料流中最後解析的k個整數是否**等於**value。  

實作DataStream類別：  
- DataStream(int value, int k)：以value和k初始化  
- boolean consec(int num)：將num加入到數據流。若最後k個整數都等於value，則回傳true；否則回傳false。若少不足k個整數，也回傳false  

# 解法
題目要求最後k個**全都要是value**，那只要紀錄value連續出現幾次即可。連續出過超過k次，代表最後k個一定也是value。  

每次consec成本O(1)，共呼叫N次，整體時間複雜度。空間複雜度O(1)。  

```python
class DataStream:

    def __init__(self, value: int, k: int):
        self.k=k
        self.value=value
        self.cnt=0

    def consec(self, num: int) -> bool:
        if num==self.value:
            self.cnt+=1
        else:
            self.cnt=0
        return self.cnt>=self.k
```

順帶一提，如果改成最後k個整數中，判斷是否至少有x個value，則要使用佇列。  