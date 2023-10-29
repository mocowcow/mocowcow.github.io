---
layout      : single
title       : LeetCode 2915. Length of the Longest Subsequence That Sums to Target
tags        : LeetCode Medium Array DP
---
雙周賽116。明明是很經典的01背包，誰知道OJ又出現什麼鳥問題，用@cache竟然給我炸MLE，害我名次直接噴掉50名。  

## 題目

輸入整數陣列nums，還有整數target。  

回傳總和正好為target的子陣列的**最大子序列長度**。若不存在則回傳-1。  

## 解法

反正就把nums[i]當作物品大小，target是背包空間，求正好裝滿背包最多可以拿幾個物品。  

定義dp(i,remain)：前i個物品中，正好裝滿remain空間最多可以拿幾個物品。  
轉移方程式：dp(i,remain)=max( dp(i-1,remain), 1+dp(i-1,remain-num[i]) )  
base cases：當i<0且remain正好為0，代表剛好拿滿，回傳0；否則不合法，回傳-inf。  

時間複雜度O(N\*target)。  
空間複雜度O(N\*target)。  

```python
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        N=len(nums)
        
        @cache
        def dp(i,remain):
            if i<0 and remain==0:
                return 0
            if i<0 or remain<0:
                return -inf
            res=dp(i-1,remain) # no take
            res=max(res,1+dp(i-1,remain-nums[i])) # take
            return res
        
        ans=dp(N-1,target)
        dp.cache_clear() # prevent MLE
        
        if ans==-inf:
            return -1
        
        return ans
```
