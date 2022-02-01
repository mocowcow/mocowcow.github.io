---
layout      : single
title       : LeetCode 121. Best Time to Buy and Sell Stock
tags 		: LeetCode Easy DP Greedy
---
初一解題格外神清氣爽。

# 題目
輸入陣列prices，表示當日股價。你可以選擇任一天買入，並在之後的日期賣出，求最大利潤。

# 解法
獲利=當日價-歷史低價，很直覺的知道只要維護一個lowest變數就可以求出最大利潤。  
不就是單純的Greedy嗎，怎麼會有DP標籤？  
[這篇討論](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39112/Why-is-this-problem-tagged-with-%22Dynamic-programming%22)有不錯回答，大意是說其實利潤可當成dp陣列，每次更新dp[i]=max(dp[i-1],todayProfit)，最後回傳dp[-1]。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = math.inf
        ans = 0
        for p in prices:
            if p < lowest:
                lowest = p
            elif p-lowest > ans:
                ans = p-lowest

        return ans

```
