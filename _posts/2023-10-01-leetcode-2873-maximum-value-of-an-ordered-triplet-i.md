---
layout      : single
title       : LeetCode 2873. Maximum Value of an Ordered Triplet I
tags        : LeetCode Easy Array Simulation
---
周賽365。

## 題目

輸入整數陣列nums。  

回傳所有索引三元組(i, j, k)的最大值，其中 i < j < k。  
若所有值都是負數，則回傳0。  

索引三元組(i, j, k)的值等於(nums[i] - nums[j]) * nums[k]。  

## 解法

在nums長度夠小的情況下，暴力枚舉還是挺方便的。  

時間複雜度O(N^3)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    ans=max(ans,(nums[i]-nums[j])*nums[k])
                    
        return ans
```
