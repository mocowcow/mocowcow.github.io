---
layout      : single
title       : LeetCode 3572. Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values
tags        : LeetCode Medium Sorting Greedy
---
biweekly contest 158。

## 題目

<https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/description/>

## 解法

先找出 x 對應的 y 最大值。  
若不同的 x 數量不足 3 個無解；否則排序後取最大的三個。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        d = Counter()
        for xx, yy in zip(x, y):
            d[xx] = max(d[xx], yy)

        if len(d) < 3:
            return -1
            
        return sum(nlargest(3, d.values()))
```
