---
layout      : single
title       : LeetCode 139. Word Break
tags 		: LeetCode Medium DP String 
---
DP教學系列。當初到底怎麼寫出bottom-up的，神奇。

# 題目
輸入字串s以及字串陣列wordDict，求s是否能由wordDict的字組合而成。

# 解法
一開始想說要用start,end表示子問題，好險及時發現，改回一個參數。

>步驟1：定義狀態  

dp[start]代表s[start:N+1]是否能由wd組成。  
要求的解就是dp[0]。

>步驟2：找出狀態轉移方程式  

dp[start]若要由wd組成，一定要是s[start:某個位置]符合wd，且dp(某個位置)可以由wd組成。  
得dp[start]=任一dp[start:end] in wd 且 dp[end]=true，start+1<=end<=N。

>步驟3：處理base cases

當start超過s長度，只會有空字串，自然是true。

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        N = len(s)
        memo = [None]*N

        def dp(start):
            if start >= N:
                return True
            if memo[start] is None:
                for end in range(start+1, N+1):
                    if s[start:end] in wd and dp(end):
                        memo[start] = True
                        break
                else:
                    memo[start] = False
            return memo[start]

        return dp(0)
```

以前寫的bottom-up方法。dp[i]是表達s[:i+1]是否由wd組成。

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        N = len(s)
        dp = [False]*(N+1)
        dp[0] = True
        for i in range(1, N+1):
            for j in range(i):
                if dp[j] and s[j:i] in wd:
                    dp[i] = True
                    break
        return dp[-1]
```
