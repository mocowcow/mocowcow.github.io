---
layout      : single
title       : LeetCode 3223. Minimum Length of String After Operations
tags        : LeetCode Medium String Simulation HashTable
---
biweekly contest 135。  

## 題目

輸入字串 s。  

你可以執行以下操作任意次:  

- 選擇字串中的某個索引 i，滿足 i 左方與右方**各至少**存在一個等於 s[i] 的字元。  
- 刪除 i 左方最近且等於 s[i] 的字元  
- 刪除 i 右方最近且等於 s[i] 的字元  

求可以達成的**最小字串長度**。  

## 解法

仔細想想，刪哪個其實無所謂，只要同一種字元剩餘超過 3 個，那就可以不斷重複刪掉 2 個。  
統計各字元出現次數，並模擬刪除。每次刪除同時使長度減少 2。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumLength(self, s: str) -> int:
        d = Counter(s)
        ans = 0
        for v in d.values():
            while v >= 3:
                ans += 2
                v -= 2

        return len(s) - ans
```
