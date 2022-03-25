---
layout      : single
title       : LeetCode 910. Smallest Range II
tags 		: LeetCode Medium Math Greedy Sorting Array
---
學習計畫的。雖然知道是greedy但不太好想出來，而且解法似乎只有一種。

# 題目
輸入整數陣列nums和整數k，你必須對nums中的每個數字n加k或是減k。  
分數指的是數列中最大值和最小值的差，求nums改變後的最小分數為多少。

# 解法
要將差值最小化，一定會想到先排序找最大、最小值。數列分成兩半，理論上左半邊都要加上k，而右半邊都要減掉k，然後我就卡住了。  

後來想想，最大的數last-最小數first的差值為diff，若k大於diff時，最佳解法應該是整個數列都加/減k，使分數維持不變；若有不同方向則必定會使上界或下界變大，造成錯誤答案。所以當k>=diff時，直接回傳差值。  
其餘的狀況，都是從first開始到某個點i都+k，有可能會更新上界，而i+1開始到last都是-k，有可能會更新下界。試著對每個點i重新計算，看新的上下界能不能降低分數。

```python
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        N=len(nums)
        nums.sort()
        first=nums[0]
        last=nums[-1]
        
        if k>=last-first:
            return last-first
        
        ans=last-first
        for i in range(N-1):
            ub=max(last-k,nums[i]+k)
            lb=min(first+k,nums[i+1]-k)
            ans=min(ans,ub-lb)
            
        return ans
```

