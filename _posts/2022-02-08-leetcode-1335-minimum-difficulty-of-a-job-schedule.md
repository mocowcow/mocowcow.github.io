---
layout      : single
title       : LeetCode 1335. Minimum Difficulty of a Job Schedule
tags 		: LeetCode Hard DP Arrays
---
DP教學系列。變數名稱打錯卡住半小時，好慘。

# 題目
輸入長度N的陣列jobDifficulty，表示各工作的難度。整數d表示天數。  
你必須依序完成所有工作，而每天都至少要做一項。當天做的所有工作中，以最高者為當天的難度。求每日總難度可以壓低到多少。  
如果工作數比天數少則回傳-1。

# 解法
能夠影響計算的變數有剩餘天數、剩餘工作，使用二維DP。

>步驟1：定義狀態  

dp[day][i]代表還剩下day天工作日，從i開始所有的工作都未完成。  
要求的解就是dp[d][0]。

>步驟2：找出狀態轉移方程式  

例如job = [6,5,4,3,2,1], d = 2：  
N=6，在day=2時，可以選擇要做6、65、654...65432，至少要留下day-1項工作，否則會沒事做。  
在所有選擇中找出(當日難度+未來難度總和)最小者，方程式為：  
dp[day][i]=min(hardest+dp[day-1][todayJob] for all i<=todayJob<=N-day)，  
hardest=max(jobDifficulty[k] for all i<=k<=todayJob)。  
有寫錯請讀者不吝嗇指正。
  
>步驟3：處理base cases  

剩下一天要趕快把所有工作做完啊。day=1時，直接在所有剩餘工作求最大值。

```python
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if N < d:
            return -1
        memo = [[None]*N for _ in range(d+1)]

        def dp(day, i):
            if day == 1:
                return max(jobDifficulty[i:])
            if memo[day][i] is None:
                hardest = jobDifficulty[i]
                best = math.inf
                for jobToday in range(i, N-day+1):
                    hardest = max(hardest, jobDifficulty[jobToday])
                    best = min(best, hardest+dp(day-1, jobToday+1))
                memo[day][i] = best
            return memo[day][i]

        return dp(d, 0)
```
