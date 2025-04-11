---
layout      : single
title       : LeetCode 3507. Minimum Pair Removal to Sort Array I
tags        : LeetCode Easy Simulation
---
weekly contest 444。

## 題目

<https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/>

## 解法

暴力模擬。  
判斷如果非遞增，就按要求找到最小的數對 nums[i], nums[i+1] 合併。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        def ok():
            return all(x<=y for x, y in pairwise(nums))

        ans = 0
        while not ok():
            ans += 1
            mn = inf
            idx = 0
            for i in range(len(nums)-1):
                val = nums[i] + nums[i+1]
                if val < mn:
                    mn = val
                    idx = i
            nums = nums[:idx] + [mn] + nums[idx+2:]

        return ans
```
