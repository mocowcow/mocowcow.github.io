---
layout      : single
title       : LeetCode 2008. Maximum Earnings From Taxi
tags 		: LeetCode Medium DP Sorting 
---
以前某次周賽卡住的。明明就是[HARD題](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)的變形，那時就想說似曾相識。  
解法其實滿多種的，值得多刷的題目。

# 題目
你是計程車司機，一條筆直的道路上有1~n個站牌。  
rides代表想搭車的乘客們，rides[i]=[start,end,tip]，表示乘客i想從start搭到end，並且會給你tip小費。該趟的總收入是(end-start+tip)。  
求從1開始不斷往後開到底且不回頭，一趟路程最多能賺多少錢。  
註：乘客在某站下車後，可馬上在同站載下一位客人。車上同時最多只能有一位客人。


# 解法
先講我第一個想到的解法。  
題目很好心的告訴我們最後一個站牌是n，那我就很輕鬆地可以定義dp(i)為到達第i站的最大利潤，答案為dp(n)。  
將rides以目的地排序，依序往後處理，可以確保先前站牌最大利潤都已經計算過。  
遍歷每個rides，其從a搭到b，小費為cost。那麼站點b的最大利潤，可以是載了當前客人，收了他的錢+他上車時的最大利潤dp(a)，或是不管她，保持上一站點的最大利潤dp(b-1)。  
但像是[[1,2,0], [[5,10,0]]這種情況，上一個乘客下車後，格很多站才有人要上車，中間的dp(3)~dp(5)都不會被更新，所以需要多一個done變數，將dp(i)值先更新為dp(i-1)。最晚下車的乘客也不一定是在n點下車，所以也要透過done更新至dp(n)。  
最後dp(n)就是答案。站牌數N，乘客數M，時間複雜度應該是：排序O(M log M)+更新站牌O(N)+更新乘客O(M)。

```python
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp=[0]*(n+1)
        rides.sort(key=itemgetter(1))
        done=0
        
        for a,b,cost in rides:
            while done<=b:
                dp[done]=dp[done-1]
                done+=1
            dp[b]=max(dp[b],dp[a]+(b-a)+cost)
            
        while done<=n:
            dp[done]=dp[done-1]
            done+=1
            
        return dp[-1]
```

