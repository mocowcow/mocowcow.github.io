---
layout      : single
title       : LeetCode 2140. Solving Questions With Brainpower
tags 		: LeetCode Medium DP Array
---
模擬周賽276。第三題解最順的一次，難得看完馬上知道解法，要好好感謝官方DP教學文。

# 題目
輸入長度N的陣列questions，questions[i]代表points[i],brainpower[i]。  
你必須從第0個問題開始作答，每一題可以選擇作答並獲得point[i]，但是接下來的brainpower[i]題都不可以作答；也可以選擇不作答這題，直接跳到下一題。  
求最多可以獲得幾分。

# 解法
當前題目答或不答，要根據之後的結果來選擇。  
定義dp[i]為答完第i題的最佳分數。可以選擇答題得分並休息幾題，或是沒得分直接下一題，dp[i]=max(得分[i]+dp[i+休息+1], dp[i+1])。  
N個題目，最後題號為N-1，若i>=N為base case，回傳0分。

```python
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)

        @lru_cache(None)
        def dp(i):
            if i >= N:
                return 0
            point, skip = questions[i]
            return max(point+dp(i+skip+1), dp(i+1))

        return dp(0)

```

改成bottom up。

```python
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0]*(N+1)

        for i in range(N-1, -1, -1):
            solve = questions[i][0]+dp[min(N, questions[i][1]+i+1)]
            skip = dp[i+1]
            dp[i] = max(solve, skip)

        return dp[0]

```