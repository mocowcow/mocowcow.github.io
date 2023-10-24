---
layout      : single
title       : LeetCode 2908. Minimum Sum of Mountain Triplets I
tags        : LeetCode Easy Array
---
模擬周賽368。

## 題目

輸入整數陣列nums。  

一個**山形**索引三元組 (i, j, k) 須滿足：  

- i < j < k  
- nums[i] < nums[j] 且 nums[k] < nums[j]  

求山形索引三元組對應nums中元素的**最小總和**。若不存在則回傳-1。  

## 解法

測資不大的情況下，直接暴力枚舉所有三元組。  

時間複雜度O(N^3)。  
空間複雜度O(N^3)。  

```python
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        N=len(nums)
        ans=inf
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    if nums[i]<nums[j] and nums[j]>nums[k]:
                        ans=min(ans,nums[i]+nums[j]+nums[k])
                        
        if ans==inf:
            return -1
        
        return ans
```
