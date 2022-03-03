---
layout      : single
title       : LeetCode 413. Arithmetic Slices
tags 		: LeetCode Medium DP Array
---
每日題。其實有點像是滑動視窗的DP題。 

# 題目
整數陣列nums，求有多少**算數子陣列**。  
如果一個子陣列長度>=3且為等差數列，則稱為算術子陣列。

# 解法
定義dp(i)代表以nums[i]結尾的算術子陣列有幾個。  
若nums[i]與前一數的公差與前兩數的公差相同，則可以將之前nums[i-1]結尾的子陣列加上nums[i]，數量為dp[i-1]+1。  
轉移方程式dp(i)=dp(i-1)+1 若 nums[i]-nums[i-1]==nums[i-1]-nums[i-2] 否則為0。  
dp(i)一定會參考到前兩個結果，且最少需要3個元素，dp[0]和dp[i]為case bases，值為0。

```python
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*N
        for i in range(2, N):
            if nums[i-1]-nums[i-2] == nums[i]-nums[i-1]:
                dp[i] = dp[i-1]+1

        return sum(dp)
```
