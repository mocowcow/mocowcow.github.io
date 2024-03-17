--- 
layout      : single
title       : LeetCode 2289. Steps to Make Array Non-decreasing
tags        : LeetCode Medium Array Stack MonotonicStack
---
周賽295。這鬼題目應該是hard才對，比第四題更難，AC率也才2.8%。

# 題目
輸入索引從0開始的整數陣列nums。在每次動作中，刪除所有nums[i]，其中nums[i-1]>nums[i] for all 0 < i < nums.length。  
回傳需要幾次刪除動作，才能使nums變成非遞減。  

# 解法
一開始還以為只要計算連續的遞增子陣列長度就行，後來發現沒這麼簡單。  

試考慮以下情況：  
> nums=[6,3,4,3,4,5]  
> 第一輪刪除後 [6,\_,4,\_,4,5]  
> 第二輪刪除後 [6,\_,\_,\_,4,5]  
> 第三輪刪除後 [6,\_,\_,\_,\_,5]  
> 第四輪刪除後 [6,\_,\_,\_,\_,\_]  
> 
可以用一個陣列dp表示各元素被刪除的的順序：  
> dp=[0,1,2,1,3,4]  

每個元素只有在左方有更大值存在時，才會被刪除，那麼我們可以維護一個單調嚴格遞減堆疊，將較小的元素合併，求出當前的被刪除順序。  


```python
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        N=len(nums)
        st=[]
        dp=[0]*N
        
        for i,n in enumerate(nums):
            rmv=0
            while st and n>=nums[st[-1]]:
                rmv=max(rmv,dp[st.pop()])
            if st:
                dp[i]=rmv+1
            st.append(i)                
    
        return max(dp)
```
