--- 
layout      : single
title       : LeetCode 2770. Maximum Number of Jumps to Reach the Last Index
tags        : LeetCode Medium Array DP
---
周賽353。

# 題目
輸入長度n的整數陣列num，還有整數target。  

你從索引0出發。每次移動，你可以從i跳到滿足以下條件的索引j：  
- 0 <= i < j < n  
- -target <= nums[j] - nums[i] <= target  

求跳到索引n-1**最多可跳多少次**。  

若無法跳到n-1則回傳-1。  

# 解法
反正就是只能向右跳，兩格的絕對差不可超過target。  
某個索引j可能從不同的索引i跳來，有重疊的子問題，故考慮dp。  

定義dp(i)：從i跳到n-1，最多可跳幾次。  
轉移方程式：dp(i)=max( dp(j)+1 FOR ALL i<j<n WHERE abs(nums[i]-nums[j])<=2 )  
base case：若i=n-1，已達終點，回傳0；若不存在j可以跳，回傳-inf使答案不計入。  

時間複雜度O(n)。  
空間複雜度O(n)。  

```python
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        N=len(nums)
        
        @cache
        def dp(i):
            if i==N-1:
                return 0
            res=-inf
            for j in range(i+1,N):
                diff=abs(nums[i]-nums[j])
                if diff<=target:
                    res=max(res,dp(j)+1)
            return res
            
        ans=dp(0)
        
        if ans==-inf:
            return -1
        
        return ans
```
