---
layout      : single
title       : LeetCode 3281. Maximize Score of Numbers in Ranges
tags        : LeetCode Medium Sorting Greedy BinarySearch
---
weekly contest 414。  

## 題目

輸入整數陣列 start，還有整數 d，代表有 n 個區間 [start[i], start[i] + d]。  

對於每個區間，你必需選擇一個區間內的整數。  
所選整數中任意兩者的**最小**絕對差則叫做**分數**。  

求可能的**最大**分數。  

## 解法

start 長度上限 1e5，要暴力枚舉肯定不可能。  

有以下幾個線索：  

- 根據經驗，**最小值最大化**通常適用**二分搜**。  
- start[i] 的選擇順序並不影響答案，可以排序。  
- 若 score = x 合法，則必定可以找到不小於 x 的合法分數，答案具有**單調性**。  

因此考慮**二分答案**。  

---

維護函數 ok(score) 判斷是否存在分數**大於等於** score 的選法。  

絕對差的最小值為 0，下界為 0。  
在 d = start[i] 上限 1e9 時，所能選擇的最大整數為 2e9，上界為 2e9。  
若 mid 不合法，嘗試更小的分數，更新上界為 mid - 1；若合法則更新下界為 mid。  

---

至於如何實現 ok(score)？  

首先將 start 區間排序。  
若前一個選擇的元素是 prev，為了盡可能保留更多彈性空間給後方，下個整數 t 應當貪心地選擇 t = prev + score。  

遍歷 start 中所有區間的起點 x，其可選範圍為 [x, x + d]。  
若 t 超過 x + d，則不合法，直接回傳 false。  
若 t 小於 x，下個整數至少要是 x，所以更新 prev = max(t, x)。  

時間複雜度 O(N log N + N log MX)，其中 MX = max(start) + d。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def ok(score):
            prev = -inf
            for x in start:
                t = prev + score
                if t > x + d:
                    return False
                prev = max(t, x)
            return True

        lo = 0
        hi = 2 * (10 ** 9) # hi = max(start) + d
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if not ok(mid):
                hi = mid - 1
            else:
                lo = mid

        return lo
```
