---
layout      : single
title       : LeetCode 3423. Maximum Difference Between Adjacent Elements in a Circular Array
tags        : LeetCode Easy Simulation
---
biweekly contest 148。

## 題目

<https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/>  

## 解法

按照題意模擬，記得對索引取模即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        N = len(nums)
        ans = -inf
        for i in range(N):
            j = (i+1) % N
            ans = max(ans, abs(nums[i] - nums[j]))

        return ans
```
