---
layout      : single
title       : LeetCode 3162. Find the Number of Good Pairs I
tags        : LeetCode Easy Array Simulation
---
周賽 399。

## 題目

輸入兩個整數陣列 nums1, nums2，長度分別是 n, m。  
還有一個正整數 k。  

一個數對 (i, j) 若滿足 nums1[i] 可被 nums2[j] \* k 整除，則稱為**好的**。  

求有多少**好的**數對。  

## 解法

暴力模擬，隨便寫隨便過。  

```python
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for x in nums1:
            for y in nums2:
                if x % (y *k) == 0:
                    ans += 1
                    
        return ans
```
