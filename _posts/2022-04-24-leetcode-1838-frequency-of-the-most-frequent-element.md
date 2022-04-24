---
layout      : single
title       : LeetCode 1838. Frequency of the Most Frequent Element
tags 		: LeetCode Medium SlidingWindow Greedy Sorting
---
二分搜學習計畫。但我覺得二分搜不是好解法，也不好想，反而很適合滑動窗口。

# 題目
輸入陣列nums和整數k，你可以對nums中任意位置的元素+1，最多k次。  
求最多可以讓幾個索引成為相同的數字。  
> nums = [1,4,8,13], k = 5  
> 可以變成[4,4,8,13]  
> 或變成[1,8,8,13]  
> 或變成[1,4,13,13]  
> 都是兩個數字相同，答案應為2

# 解法
若想將陣列中的數變成x，最好的方式是從和x相差較小的數開始加，因此先把nums排序。  
使用滑動窗口，試著把範圍內的每個數加到和窗口最右邊的數相同。每次加入新的數nums[right]，並計算需要加多少次，若k不足夠，則丟掉最左邊的元素，直到k值足夠為止，以視窗大小更新答案。

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N=len(nums)
        nums.sort()
        sm=0
        left=0
        ans=0
        for right,n in enumerate(nums):
            sm+=n
            while (right-left+1)*nums[right]-sm > k: # dont have enough k, pop the leftmost one out
                sm-=nums[left]
                left+=1
            ans=max(ans,right-left+1)
        
        return ans
```

