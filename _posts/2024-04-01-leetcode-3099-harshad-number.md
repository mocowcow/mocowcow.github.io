---
layout      : single
title       : LeetCode 3099. Harshad Number
tags        : LeetCode Easy String Simulation
---
周賽 391。好像常常在 Q1 看到數位分解。  

## 題目

若一個整數能夠被其**所有數字總和**整除，則稱為**哈沙德**數。  

輸入整數 x，若 x 是**哈沙德**數則回傳其數字總和，否則回傳 -1。  

## 解法

py 做數位分解真的很方便，轉成字串再遍歷轉回整數。  

時間複雜度 O(log x)。  
空間複雜度 O(1)。  

```python
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sm = sum(int(d) for d in str(x))
        if x % sm == 0:
            return sm
        
        return -1
```
