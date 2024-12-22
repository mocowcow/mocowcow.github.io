---
layout      : single
title       : LeetCode 3396. Minimum Number of Operations to Make Elements in Array Distinct
tags        : LeetCode Easy Simulation
---
weekly contest 429。

## 題目

輸入整數陣列 nums。  
你必須確保陣列中所有元素都是**不同的**。  
你可以進行以下操作任意次：  

- 從陣列開頭移除 3 個元素。若陣列元素小於 3 個，則移除全部。  

求**最少**操作次數。  

## 解法

暴力模擬，有重複就刪。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        def ok():
            return len(set(nums)) == len(nums)

        ans = 0
        while not ok():
            nums = nums[3:]
            ans += 1

        return ans
```
