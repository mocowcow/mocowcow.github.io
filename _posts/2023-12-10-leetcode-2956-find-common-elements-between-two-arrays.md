---
layout      : single
title       : LeetCode 2956. Find Common Elements Between Two Arrays
tags        : LeetCode Easy Array Simulation HashTable
---
雙周賽119。

## 題目

輸入整數陣列nums1和nums2，兩者大小分別是n和m。  

計算下列數值：  

- 滿足0 <= i < n的索引i，有多少nums1[i]在nums2中出現**至少一次**  
- 滿足0 <= i < m的索引i，有多少nums2[i]在nums1中出現**至少一次**  

回傳長度2的整數陣列，分別代表以上兩值。  

## 解法

暴力法直接模擬。  

時間複雜度O(mn)。  
空間複雜度O(1)。  

```python
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        v1=sum(x in nums2 for x in nums1)
        v2=sum(x in nums1 for x in nums2)
        
        return [v1,v2]
```

測資範圍大一點的話要先轉成集合，以供O(1)查找。  

時間複雜度O(m+n)。  
時間複雜度O(m+n)。  

```python
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        v1=sum(x in s2 for x in nums1)
        v2=sum(x in s1 for x in nums2)
        
        return [v1,v2]
```
