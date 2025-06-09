---
layout      : single
title       : LeetCode 3576. Transform Array to All Equal Elements
tags        : LeetCode Medium Greedy
---
weekly contest 453。

## 題目

<https://leetcode.com/problems/transform-array-to-all-equal-elements/description/>

## 解法

只有改成 1 或是 -1 兩種可能。  
枚舉兩種可能，看能不能改。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        N = len(nums)

        def ok(t):
            a = nums.copy()
            cnt = 0
            for i in range(N-1):
                if a[i] != t:
                    a[i] *= -1
                    a[i+1] *= -1
                    cnt += 1
            return a[-1] == t and cnt <= k
                    
        return ok(1) or ok(-1)
```
