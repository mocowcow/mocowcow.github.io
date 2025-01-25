---
layout      : single
title       : LeetCode 3427. Sum of Variable Length Subarrays
tags        : LeetCode Easy Simulation PrefixSum
---
weekly contest 433。

## 題目

<https://leetcode.com/problems/sum-of-variable-length-subarrays/>

## 解法

對於每個 i 來說，子陣列起點 start = max(0, i-nums[i])。  
暴力模擬，枚舉子陣列並求和。  

時間複雜度 O(N^2)。  
空間複雜度 O(1)。  

```python
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            start = max(0, i-nums[i])
            sub = nums[start:i+1]
            ans += sum(sub)

        return ans
```

可用**前綴和**優化子陣列求和。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        N = len(nums)
        ps = list(accumulate(nums, initial=0))
        ans = 0
        for i in range(N):
            start = max(0, i-nums[i])
            ans += ps[i+1] - ps[start]

        return ans
```
