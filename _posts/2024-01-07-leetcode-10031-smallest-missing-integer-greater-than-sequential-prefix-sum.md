---
layout      : single
title       : LeetCode 10031. Smallest Missing Integer Greater Than Sequential Prefix Sum
tags        : LeetCode Easy Array PrefixSum Simulation HashTable
---
雙周賽121。

## 題目

輸入整數陣列nums。  

一個前綴nums[0..i]對於 1 <= j <= i 的所有元素都滿足 nums[j] = nums[j - 1] + 1，則稱為**循序的**。  
注意：只包含nums[0]的前綴也是**循序的**。  

求nums中沒有出現的**最小**整數x，且x必須大於等於**最長**循序前綴的總和。  

## 解法

先找到等差為1的最長前綴nums[0..j]，計算前綴和x。  

把nums轉成集合，以供O(1)查詢x是否存在。
若x存在，則嘗試x+1，直到不存在為止。最多只會嘗試N次。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        N=len(nums)
        i=0
        while i+1<N and nums[i+1]==nums[i]+1:
            i+=1
        
        # find missing
        s=set(nums)
        x=sum(nums[:i+1])
        while x in s:
            x+=1
            
        return ps
```
