---
layout      : single
title       : LeetCode 153. Find Minimum in Rotated Sorted Array
tags 		: LeetCode Medium BinarySearch Array
---
二分搜學習計畫最後一天。個人覺得這題不應該放這麼後面，畢竟前面好幾題已使用過重複的概念。

# 題目
輸入一個旋轉過的有序數列nums，找到裡面最小的元素。  
時間複雜度必須在O(log n)內。

# 解法
看複雜度限制就知道只能二分搜了，暴力法不考慮。  
每次取中間位置mid，如果nums[mid]大於nums[hi]，代表選轉過後的最小元素出現在右半邊，所以把下界更新為mid+1；否則確定最小元素出現在左方，更新上界為mid。  
注意，考慮以下案例，所以更新下界時不可設為mid-1：  
> [**3,1,2**] lo=0, hi=2, mid=1  更新上界  
> [**3,1**,2]  lo=0, hi=1, mid=0  更新下界  
> [3,**1**,2] lo=1  

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-1
        while lo<hi:
            mid=(lo+hi)//2
            if nums[mid]>nums[hi]: # left side sorted
                lo=mid+1
            else: # right side sorted
                hi=mid
            
        return nums[lo]
```

