---
layout      : single
title       : LeetCode 1143. Longest Common Subsequence
tags 		: LeetCode Medium DP String
---
DP教學系列。還是自己手刻memo好了，不要偷懶。

# 題目
輸入長度M的字串text1、長度N的字串text2，找出最長的共通子序列長度為多少。  
例如"ace"是"abcde"的子序列。

# 解法
字串長度各為M、N，我們需要二維DP陣列。

>步驟1：定義狀態  

dp[i][j]代表text1前i+1個字元，以及text2前j+1個字元相互比對的結果。
例如text1 = "abcde", text2 = "ace"：  
dp[2][1]就是"abc"與"ac"比對的最長結果，也就是"ac"長度2。

>步驟2：找出狀態轉移方程式  

"abc"與"ac"比對時，如果最後一個字元相同，長度一定是"ab"與"a"的比對結果再加上1。方程式為dp[i][j] = dp[i-1, j-1]+1。  
如果不同，每次只會給其中一方加字元，所以是dp[i][j] = max(dp[i, j-1], dp[i-1, j])。
  
>步驟3：處理base cases  

如果i或是j小於0，沒辦法產生子字串，直接回傳0。

其實這題好像bottom-up比top-down更直觀？


```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        memo = [[None]*N for _ in range(M)]

        def dp(i, j):
            if i < 0 or j < 0:  # base cases
                return 0
            if memo[i][j] is None:
                if text1[i] == text2[j]:
                    memo[i][j] = dp(i-1, j-1)+1
                else:
                    memo[i][j] = max(dp(i, j-1), dp(i-1, j))
            return memo[i][j]

        return dp(M-1, N-1)
```

2022-6-14更新。  
今天的每日題剛好有用到這個概念，所以先回來複習一次。  
這次改用bottom up方法，因為要處理i=0或是j=0的base cases，所以DP陣列長度要各加上1。  

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M,N=len(text1),len(text2)
        dp=[[0]*(N+1) for _ in range(M+1)]
        
        for i in range(M):
            for j in range(N):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
                
        return dp[-1][-1]
```