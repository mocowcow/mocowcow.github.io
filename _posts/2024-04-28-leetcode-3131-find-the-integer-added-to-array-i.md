---
layout      : single
title       : LeetCode 3131. Find the Integer Added to Array I
tags        : LeetCode Easy Array Sorting
---
周賽395。

## 題目

輸入兩個長度 n 的整數陣列 nums1 和 nums2。  

若兩個陣列中，各整數的出現頻率相同，則稱兩陣列**相等**。  
你必須對 nums1 的每個元素都加上一個值 x，使得 nums1 和 nums2 **相等**。  

回傳整數 x。  

## 解法

原本輸入兩陣列是不規則的。兩者排序後，對於每個 nums2[i] - nums1[i] 的差值都會等於 x。  
大概像是這樣：  
> nums1 = [10, 20, 30]  
> nums2 = [10 + x, 20 + x, 30 + x]  

其實也不用排序，只要找到兩陣列的最小 / 最大值即可。  

時間複雜度 O(n)。  
空間複雜度 O(1)。  

```python
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)
```
