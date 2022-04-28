--- 
layout      : single
title       : LeetCode 154. Find Minimum in Rotated Sorted Array II
tags        : LeetCode Hard Array BinarySearch
---
二分搜學習計畫。相似題[153. find minimum in rotated sorted array]({% post_url 2022-04-15-leetcode-153-find-minimum-in-rotated-sorted-array %})，似乎在旋轉過的有序陣列中，碰到重複值是差不多的處理方法。

# 題目
輸入一個旋轉過的有序數列nums，元素有可能重複出現，找到裡面最小的元素。  

# 解法
和原生題一樣，每次抓中間的數字和上界比較，有三種狀況：  
1. 中間數大於上界數，代表最小元素在右半邊，更新下界  
2. 中間數小於上界數，代表最小元素在左半邊，更新上界  
3. 中間數等於上界數，不確定最小元素在哪，只好把上界縮減1格

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-1
        while lo<hi:
            mid=(lo+hi)//2
            if nums[mid]>nums[hi]: #left side sorted
                lo=mid+1
            elif nums[mid]<nums[hi]: #right side sorted
                hi=mid
            else:
                hi-=1
            
        return nums[lo]
```
