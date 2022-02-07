---
layout      : single
title       : LeetCode 198. House Robber
tags 		: LeetCode Medium DP Array
---
一樣是DP教學內容。

# 題目
輸入一個長度N陣列nums代表各家的錢財。你是一個小偷，連續偷兩家相鄰的則會觸發警報。求不被發現的情況下最多可以得到多少錢。

# 解法
>步驟1：定義狀態  

dp[i]表示經過第i家時，身上最多能有多少錢。

>步驟2：找出狀態轉移方程式  

經過每一家時，我們可以決定偷或不偷。只有前一家沒偷才能偷當前這家，但是前一家沒偷也可以不偷當前這家，因為有兩家有錢人夾著兩家窮人的情況。  
所以dp[i]=max(dp[i-1], dp[i-2]+nums[i])。

>步驟3：處理base cases  

先判斷長度N，如果只有1家，那肯定是拿了走人，直接回傳nums[0]。  
其他情況下，當走到第一家時，最佳狀況一定是拿，所以dp[0]=nums[0]。  
而第二家時，只有可能從第一家和第二家選擇偷誰，所以是max(nums[0],nums[1])。  

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        dp = [0]*N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]
```
