---
layout      : single
title       : LeetCode 34. Find First and Last Position of Element in Sorted Array
tags 		: LeetCode Medium Array BinarySearch
---
二分搜學習計畫。直接包含了lower bound和upper bound的應用，非常適合當作教材。

# 題目
輸入有序的數列nums，找到target在nums中的第一個和最後一個位置。若不存在target則回傳[-1,-1]。

# 解法
不同於普通的二分搜，lower bound找的是第一個大於等於x的位置，而upper bound找的是第一個大於x的位置。  
我們可以先找用lb找第一個位置L，若L位置超出陣列或nums[L]不是target的話，代表找不到，可以直接回傳[-1,-1]。  
但是ub找的是第一個大於x的位置，將其-1就等價於最後一個大於等於x的位置，因此最後一個位置R=upper bound-1。  
最後回傳數對[L,R]。

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L=bisect_left(nums,target)
        if L==len(nums) or nums[L]!=target:
            return [-1,-1]
        R=bisect_right(nums,target)-1
        return [L,R]
```

假設在[2,3,5,6]中要找4，此時lb=2, rb=2；又或者找7，此時lb=4, rb=4，可以假設目標值不存在的話，lb會等於rb。  
若要找3，lb=1, rb=2，答案為[lb,rb-1]=[1,1]。  
將邏輯簡化，並自己手刻lb和ub。  

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def lower(a,x):
            lo,hi=0,len(a)
            while lo<hi:
                mid=(lo+hi)//2
                if a[mid]<x:
                    lo=mid+1
                else:
                    hi=mid
            return lo
        
        def upper(a,x):
            lo,hi=0,len(a)
            while lo<hi:
                mid=(lo+hi)//2
                if a[mid]<=x:
                    lo=mid+1
                else:
                    hi=mid
            return lo
        
        L=lower(nums,target)
        R=upper(nums,target)
        if L==R:
            return [-1,-1]
        else:
            return [L,R-1]
```