--- 
layout      : single
title       : LeetCode 2441. Largest Positive Integer That Exists With Its Negative
tags        : LeetCode Easy Array
---
周賽315。

# 題目
輸入一個不包含零的整數陣列nums，找到最大的正整數k，使得k和-k都存在於陣列中。  
回傳正整數k，如果k不存在則回傳-1。  

# 解法
直接將nums裝入集合，由nums[i]的最大範圍1000開始往下找到1，如果某個數的正負數同時存在則回傳；都找不到才回傳-1。  

時空間複雜度O(N)。  

```python
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s=set(nums)
        
        for i in reversed(range(1,1001)):
            if i in s and -i in s:
                return i 
            
        return -1
```
