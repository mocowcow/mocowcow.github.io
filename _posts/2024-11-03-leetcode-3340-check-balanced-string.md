---
layout      : single
title       : LeetCode 3340. Check Balanced String
tags        : LeetCode Easy Simulation
---
weekly contest 422。  

## 題目

輸入由數字組成的字串 num。  
如果字串偶數索引數字的和等於奇數索引數字的和，則稱為**平衡的**。  

若 num 是**平衡的**，則回傳 true，否回傳 false。  

## 解法

按照題意模擬。  
可用兩個變數分別表示奇數、偶數和；也可以只用一個變數，以正負數表示。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def isBalanced(self, num: str) -> bool:
        bal = 0
        for i, c in enumerate(num):
            if i%2 == 0:
                bal += int(c)
            else:
                bal -= int(c)

        return bal == 0
```
