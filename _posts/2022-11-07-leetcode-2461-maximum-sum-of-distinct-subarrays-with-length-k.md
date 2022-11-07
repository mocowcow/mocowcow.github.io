--- 
layout      : single
title       : LeetCode 2461. Maximum Sum of Distinct Subarrays With Length K
tags        : LeetCode Medium Array HashTable SlidingWindow
---
周賽318。滑動窗口經典題，關鍵在於如何把空元素從雜湊表中刪除。  

# 題目
輸入一個整數陣列nums和整數k。求滿足以下條件的nums子陣列的最大和：  
- 子陣列長度k  
- 子陣列中所有元素都不重複  

如果沒有滿足條件的子陣列，則回傳0。  

# 解法
維護一個大小為k的滑動窗口，右邊加入一個元素，左邊就要出去一個。每次移動完檢查是否有重複元素，若無則以窗口內元素總和更新答案。  

每個元素出入各一次，時間複雜度O(N)。最差情況下整個陣列元素都不重複，空間複雜度O(N)。  

```python
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d=Counter()
        sm=0
        l=0
        ans=0
        
        for r,n in enumerate(nums):
            sm+=n
            d[n]+=1
            if len(d)==k:
                ans=max(ans,sm)
            if r+1>=k:
                d[nums[l]]-=1
                if d[nums[l]]==0:del d[nums[l]]
                sm-=nums[l]
                l+=1
                
        return ans
```
