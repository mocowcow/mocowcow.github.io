---
layout      : single
title       : LeetCode 3462. Maximum Sum With at Most K Elements
tags        : LeetCode Medium Sorting Greedy
---
weekly contest 438。

## 題目

<https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/>

## 解法

每列限制最多取 limit[i] 個，也就是只有前 limit[i] 大的元素有機會被拿到。  

先找出每列能被拿的元素，全部蒐集完之後再重新排序，取最大的 k 個。  
最差情況下，整個矩陣的元素都會一起排序。  

時間複雜度 O(MN log MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        a = []
        for i, row in enumerate(grid):
            row.sort(reverse=True)
            a += row[:limits[i]]

        a.sort(reverse=True)
        
        return sum(a[:k])
```
