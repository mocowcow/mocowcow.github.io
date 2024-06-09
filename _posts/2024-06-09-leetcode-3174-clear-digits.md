---
layout      : single
title       : LeetCode 3174. Clear Digits
tags        : LeetCode Easy String Stack Simulation
---
雙周賽 132。有點類似上週 Q3。  

## 題目

輸入字串 s。  

你的目標是重複以下操作，刪除字串中**所有**數字字元：  

- 刪除**第一個數字字元**，以及其**左方最近**的**非數字**字元  

回傳刪除所有數字字元後的字串。  

## 解法

題目保證每個數字的左方一定有非數字可刪除。  
因此只要按照**後進先出**的順序，使用堆疊維護剩餘的非數字字元即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for c in s:
            if c.isdigit():
                st.pop()
            else:
                st.append(c)
                
        return "".join(st)
```
