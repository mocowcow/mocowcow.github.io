---
layout      : single
title       : LeetCode 2908. Minimum Sum of Mountain Triplets I
tags        : LeetCode Easy Array PrefixSum
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

對於j來說，小於j的任意索引都可以作為i；反之，大於j的都可以當作k。  
答案求最小總和，索引對應的元素當然是越小越好。  

我們只要知道位於j左右兩方的最小值，又是老朋友**前後綴分解**。  
遍歷nums，計算出前後綴的最小值。最後再枚舉j，若為**山形**則以總和更新答案。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        N=len(nums)
        suff=[0]*N # suff[i] = min(nums[i, N-1])
        mn=inf
        for i in reversed(range(N)):
            mn=min(mn,nums[i])
            suff[i]=mn
            
        ans=inf
        mn=nums[0] # min(nums[0, i])
        for i in range(N-1):
            x=nums[i]
            if mn<x and x>suff[i+1]: # is mountain
                ans=min(ans,mn+x+suff[i+1])
            mn=min(mn,x)
            
        if ans==inf:
            return -1
        
        return ans
```
