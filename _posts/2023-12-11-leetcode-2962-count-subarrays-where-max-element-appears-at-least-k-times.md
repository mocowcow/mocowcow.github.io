---
layout      : single
title       : LeetCode 2962. Count Subarrays Where Max Element Appears at Least K Times
tags        : LeetCode Medium Array
---
周賽375。

## 題目

輸入整數陣列nums，還有正整數k。  

求有多少子陣列，**nums中的最大值**在子陣列中出現至少k次。  

## 解法

要看清楚，是nums中的最大值，不是子陣列中的最大值。  
因此先遍歷一次nums找到最大值mx。  

枚舉右端點i，並維護mx的出現索引，如果mx至少出現了k次才有合法的子陣列。  
若mx出現size次，且cnt>=k時，只需要保留最右邊k個mx，其他的都可以丟掉。  
令從右數來第k個mx的索引為j，則對於右端點i來說，區間[0, j]之間的索引都可是**合法左端點**。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx=max(nums)
        idx=[]
        ans=0
        
        for i,x in enumerate(nums):
            if x==mx:
                idx.append(i)
            if len(idx)>=k:
                j=idx[len(idx)-k]
                ans+=j+1 # lb can be [0, j]
                
        return ans
```
