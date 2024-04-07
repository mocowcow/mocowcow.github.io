---
layout      : single
title       : LeetCode 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
tags        : LeetCode Easy Array Greedy
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

其實直接遍歷最簡單，只要**不滿足**遞增/遞減就重新計算長度。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0
        inc_prev, dec_prev = -inf, inf
        inc_cnt = dec_cnt = 0
        for curr in nums:
            if curr > inc_prev:
                inc_cnt += 1
            else:
                inc_cnt = 1
            if curr < dec_prev:
                dec_cnt += 1
            else:
                dec_cnt = 1
            inc_prev = dec_prev = curr
            ans = max(ans, inc_cnt, dec_cnt)
            
        return ans
```
