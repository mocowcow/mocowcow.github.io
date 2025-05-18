---
layout      : single
title       : LeetCode 3550. Smallest Index With Digit Sum Equal to Index
tags        : LeetCode Easy Simulation
---
weekly contest 450。

## 題目

<https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/>

## 解法

按題意模擬。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            sm = sum(int(c) for c in str(x))
            # sm = 0
            # while x > 0:
            #     x, r = divmod(x, 10)
            #     sm += r
            if sm == i:
                return i

        return -1
```
