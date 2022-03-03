---
layout      : single
title       : LeetCode 1502. Can Make Arithmetic Progression From Sequence
tags 		: LeetCode Easy Array Sorting
---
Study Plan - Programming Skills。  

# 題目
整數陣列nums，檢查是否可以透過重新排列而使nums成為等差數列。

# 解法
排序後，將第n2-n1訂為公差diff，依序檢查後面是否差皆為diff，否則回傳False。

```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        N = len(arr)
        arr.sort()
        diff = arr[1]-arr[0]
        for i in range(2, N):
            if arr[i]-arr[i-1] != diff:
                return False

        return True
```
