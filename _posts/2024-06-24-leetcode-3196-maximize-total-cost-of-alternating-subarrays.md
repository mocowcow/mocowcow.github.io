---
layout      : single
title       : LeetCode 3196. Maximize Total Cost of Alternating Subarrays
tags        : LeetCode Medium Array DP
---
周賽 403。題目有點長，實際上並沒有這麼複雜。  

## 題目

輸入長度 n 的整數陣列 nums。  

子陣列 nums[l..r] 的成本定義為：  

- cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)<sup>r − l</sup>  

你的目標是將 nums **分割**成數個子陣列，且所有子陣列的**總成本最大化**。  
每個元素必須正好屬於其中一個子陣列。  

求最佳分割方式下，可得到的子陣列**總成本最大值**。  

注意：如果 nums 不分割，即分割成 1 個子陣列，則總成本為 cost(0, n - 1)。  

## 解法

仔細觀察這個 cost 的定義，其實就是子陣列中偶數位的元素取正數、奇數位取負數，不斷正負、正負交替。  
一個長度為 4 的子陣列其實可看做 2 個長度為 2 的子陣列，基本上就只有兩種狀態。  
除了正負的差別以外，奇數位還可以最為當前子陣列的**結尾**，使得**下一個元素**成為新的子陣列的**第一個元素**，也就是偶數位取正值，進而使得連續兩個數取正值。  

我們不知道取正負數何者較好，而且不同的分割法有可能形成**重疊的子問題**，因此考慮 dp。  

---

定義 dp(i, sign)：在 nums[i] 的正負號為 sign 時，分割 nums[i..n-1] 的最大總成本。  
轉移：  

- sign = 1：當前數是正數，下一個數可以是負數、也可以是正數  
    dp(i, 1) = max(dp(i + 1, -1) + dp(i + 1, 1)) + nums[i]  
- sign = -1：當前數是負數，下一個數只能是正數  
    dp(i, -1) = dp(i + 1, 1) - nums[i]  

base：當 i = N，沒有剩餘元素，回傳 0。  

nums[0] 只能做為正數只用，因此答案入口為 dp(0, 1)。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        N = len(nums)
        
        @cache
        def dp(i, sign):
            if i == N:
                return 0
            res = dp(i + 1, -sign)
            if sign == 1:
                res = max(res, dp(i + 1, 1))
            return res + nums[i] * sign
        
        return dp(0, 1)
```
