---
layout      : single
title       : LeetCode 3107. Minimum Operations to Make Median of Array Equal to K
tags        : LeetCode Medium Array Greedy
---
周賽 392。比賽中好像沒講清楚偶長度怎麼辦，不過範例倒是看得出要取右中位數。  

## 題目

輸入整數陣列 nums 還有非負整數 k。  
每次操作，你可以將任意元素**增加**或**減少** 1。  

求最少需要幾次操作，才能使得 nums 的中位數等於 k。  

中位數是有序遞增陣列中，位於最中間的元素。如果有兩個中位數，則選擇**右中位數**。  

## 解法

設中位數的索引為 mid。  

如果當前中位數 nums[mid] < k，我們需要把他變大。這時 nums[mid] 可能會大於 nums[mid + 1]，中位數就換人了。  
例如：  
> a = [1,1,1], k = 2  
> 把 a[1] 增加 1  
> a = [1,2,1] 不滿足遞增，重新排序成 [1,1,2]  
> 把 a[1] 增加 1  
> a = [1,2,2]  
> 共需要兩次操作  

可見隨著中位數的增加，位於右方的元素會輪流成為中位數，直到中位數變成 k 為止。  
因此只要找到右半邊小於 k 的所有元素，求出他們與 k 的差值總和，即為操作次數。  
同理，在 nums[mid] > k 時，找左半邊大於 k 的元素求差值總和。  

時間複雜度 O(N log N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        mid = N // 2
        median = nums[mid]
        if median == k:
            return 0
        
        ans = 0
        if median < k: # right part
            for i in range(mid, N):
                if nums[i] < k:
                    ans += k - nums[i]
        else: # left part
            for i in range(mid + 1):
                if nums[i] > k:
                    ans += nums[i] -k
                
        return ans
```
