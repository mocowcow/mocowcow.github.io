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

```python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        N=len(nums)
        j=0
        while j+1<N and nums[j+1]==nums[j]+1:
            j+=1
        
        # find missing
        s=set(nums)
        x=sum(nums[:j+1])
        while x in s:
            x+=1
            
        return ps
```
