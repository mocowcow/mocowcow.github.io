---
layout      : single
title       : LeetCode 3301. Maximize the Total Height of Unique Towers
tags        : LeetCode Medium Greedy Sorting
---
biweekly contest 140。  

## 題目

輸入整數陣列 maximumHeight，其中 maximumHeight[i] 代表第 i 座塔的**最大可用高度**。  

你必須決定每座塔的高度，滿足：  

- 第 i 座塔的高度不得超過 maximumHeight[i]。  
- 所有塔的高度互不相同。  

求可達到的**最大**總高度。若無合法方案，則回傳 -1。  

## 解法

為了使總高度盡可能大，優先從可用高度最大的塔處理，先排序。  
過程中維護上一個塔的高度 prev，本次的高度不可超過 prev-1，也不可超過 maximumHeight[i]。  
途中若發現可用高度小於 1，則代表不合法，直接回傳 -1。  

時間複雜度 O(N log N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        ans = 0
        prev = inf
        for x in maximumHeight:
            t = min(prev-1, x)
            if t < 1: # invalid
                return -1
            ans += t
            prev = t

        return ans
```
