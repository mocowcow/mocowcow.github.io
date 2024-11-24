---
layout      : single
title       : LeetCode 3364. Minimum Positive Sum Subarray 
tags        : LeetCode Easy Simulation
---
weekly contes 425。  

## 題目

輸入整數陣列 nums 和兩個整數 l, r。  
你的目標是找到長度介於 [l,r]、且元素和大於 0 的子陣列。  

求這些子陣列中的**最小**和。若不存在則回傳 -1。  

## 解法

暴力所有子陣列，若滿足條件則更新答案。  

時間複雜度 O(N^3)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        N = len(nums)

        ans = inf
        for i in range(N):
            for j in range(i, N):
                sz = j-i+1
                sm = sum(nums[i:j+1])
                if sm > 0 and l <= sz <= r:
                    ans = min(ans, sm)

        if ans == inf:
            return -1

        return ans
```
