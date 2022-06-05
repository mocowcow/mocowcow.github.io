--- 
layout      : single
title       : LeetCode 2294. Partition Array Such That Maximum Difference Is K
tags        : LeetCode Medium Array Greedy TwoPointers Sorting
---
周賽296。原本不小心看成**子陣列**，好險及時發現題目要的是**子序列**。

# 題目
輸入整數陣列nums和整數k。試將nums分成多個子序列，而使nums中每個數正好出現在其中一個子序列中。  
每個子序列中，最大元素與最小元素的差不得超過k，求最少需要幾個幾個子序列。  

# 解法
既然說是子序列，代表順序不重要，可以將nums重新排序。  
排序後，盡可能將相連續的數字裝在同一個子序列中。而子序列中第一個元素就是最小值，若當前數字n與最小值差不超過k，則將n加入當前子序列中；否則開啟新的子序列，將n設為第一個元素。  

```python
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        N=len(nums)
        nums.sort()
        ans=1
        first=nums[0]
        for n in nums[1:]:
            if n-first>k:
                ans+=1
                first=n
            
        return ans
```
