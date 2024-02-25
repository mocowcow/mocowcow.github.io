---
layout      : single
title       : LeetCode 3046. Split the Array
tags        : LeetCode Easy Array HashTable
---
周賽386。

## 題目

輸入**偶數長度**的整數陣列 nums。你必須將 nums 分割成 nums1 和 nums2，並滿足以下條件：  

- nums1.length == nums2.length == nums.length / 2.
- nums1 由**不同的**元素所組成  
- nums2 由**不同的**元素所組成  

若可分割則回傳 true，否則回傳 false。  

## 解法

題目保證了 nums 長度一定是偶數，那麼就不必考慮分割長度不相等的問題。  

既然要保證兩個分割的結果中不存在重複元素，那同一個元素在 nums 中最多只能出現 2 次。  

```python
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for v in d.values():
            if v > 2:
                return False
            
        return True
```
