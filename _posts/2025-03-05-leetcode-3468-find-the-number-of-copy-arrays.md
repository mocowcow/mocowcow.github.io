---
layout      : single
title       : LeetCode 3468. Find the Number of Copy Arrays
tags        : LeetCode Medium Simulation
---
biweekly contest 151。

## 題目

<https://leetcode.com/problems/find-the-number-of-copy-arrays/description/>

## 解法

根據第一個條件，可知道只在乎 delta = original[i] - original[i-1] 的值。
例如：[1,2,3,4] 和 [2,3,4,5] 是等價的，相鄰元素差都是 [1,1,1]。  

第二個條件是說 copy[i] 可填的值是在區間 bounds[i] = [u, v] 之間。  

- i = 0 時，copy[0] 可填區間為 [l, r] = bounds[0] = [u, v]。  
- i > 0 時，考慮到 delta，copy[i] 可填區間變為 [l + delta, r + delta]。  
    但也要符合 bounds[i] = [u, v] 的限制，需求兩區間的交集。  

問題轉換成：求 N 個區間的交集長度。  
可能沒有交集，所以答案要和 0 取最大值。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        N = len(original)
        l, r = bounds[0]
        for i in range(1, N):
            delta = original[i] - original[i-1]
            l, r = l + delta, r + delta
            l = max(l, bounds[i][0])
            r = min(r, bounds[i][1])

        return max(0, r - l + 1)
```
