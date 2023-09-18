---
layout      : single
title       : LeetCode 2859. Sum of Values at Indices With K Set Bits
tags        : LeetCode Easy Array BitManipulation Simulation
---
周賽363。

## 題目

輸入索引從0開始的整數陣列nums和整數k。  

回傳一個整數，其代表nums中擁有**正好k個set bits**的**索引**對應的元素**總和**。  

set bits指的是一個整數的二進位表示中，所出現的數字1個數。  
例如：21的二進位是10101，擁有3個set bits。  

## 解法

簡單模擬，索引i如果正好k個bit，就把nums[i]加入答案。  
使用內建函數求set bits的時間是O(1)。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans=0
        for i,x in enumerate(nums):
            if i.bit_count()==k:
                ans+=x
                
        return ans
```
