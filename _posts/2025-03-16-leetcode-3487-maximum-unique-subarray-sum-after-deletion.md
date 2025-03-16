---
layout      : single
title       : LeetCode 3487. Maximum Unique Subarray Sum After Deletion
tags        : LeetCode Easy Greedy
---
weekly contest 441。  

## 題目

<https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/>

## 解法

可以從 nums 中刪除若干元素，但不得為空。  
再從修改過的 nums 中選擇**子陣列**。  

子陣列只是晃子，不要的都刪掉、留下的全選，也是一種子陣列。  
答案為所有**非負數**去重後加總。  

注意特判：如果 nums 全都是負數，又不能變成**空陣列**，只能留一個最小的負數。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)

        s = set()
        for x in nums:
            if x >= 0:
                s.add(x)
    
        return sum(s)
```
