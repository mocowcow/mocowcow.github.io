--- 
layout      : single
title       : LeetCode 2537. Count the Number of Good Subarrays
tags        : LeetCode Medium Array SlidingWindow TwoPointers HashTable
---
周賽328。雖然很容易想到滑動窗口，但怎麼滑卻不太容易想到。  

# 題目
輸入整數陣列nums和整數k，求有多少個**好的子陣列**。  

一個子陣列若至少擁有k個索引數對(i, j)，滿足i < j且arr[i] == arr[j]，則稱之為**好的子陣列**。  

# 解法
當某個子陣列滿足k個數對後，不管是從左方還是右方加入新的元素，一定也至少擁有k個數對。  

因此可以窮舉每個索引right作為右邊界，依序加入子陣列中。如果索引數對pair滿足k，則代表以left為左邊界，搭配right\~N-1為右邊界都是**好的子陣列**，將N-right個好的子陣列加入答案，並收縮左邊界。  

時間複雜度O(N)。空間複雜度O(N)。  

```python
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N=len(nums)
        d=Counter()
        ans=0
        pair=0
        left=0
        
        for right,n in enumerate(nums):
            pair+=d[n]
            d[n]+=1
            while pair>=k:
                ans+=N-right
                d[nums[left]]-=1
                pair-=d[nums[left]]
                left+=1
                
        return ans
```
