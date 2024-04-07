---
layout      : single
title       : LeetCode 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
tags        : LeetCode Easy Array
---
周賽 392。

## 題目

輸入整數陣列 nums。  
求 nums 中，**嚴格遞增**或**嚴格遞減**子陣列的最大長度。  

## 解法

暴力法，從長度大到小枚舉所有子陣列，只要滿足遞增或遞減就回傳。  

時間複雜度 O(N^3)。  
空間複雜度 O(N)。  

```python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        
        def ok(sub):
            # increasing
            for a,b in pairwise(sub):
                if a >= b:
                    break
            else:
                return True
            
            # decreasing
            for a,b in pairwise(reversed(sub)):
                if a >= b:
                    break
            else:
                return True
            return False
        
        for size in reversed(range(N + 1)):
            for i in range(N - size + 1):
                sub = nums[i:i + size]
                if ok(sub):
                    return size

```
