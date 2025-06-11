---
layout      : single
title       : LeetCode 3573. Best Time to Buy and Sell Stock V
tags        : LeetCode Medium DP
---
biweekly contest 158。  
股票系列又出新作，這次是**做空**。  

## 題目

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/description/>

## 解法

以往股票系列都是**先買後賣**，dp 狀態只有**買**或**賣**兩種。  

這次允許做空，也就是**先融券賣出後償還**。  
在開始之前，第一步驟可以是**買** (普通交易) 也可以是**賣** (做空)。  

第一步決定好之後，第二步驟就固定了。所以總共只有三種狀態：  

- 選擇普通交易或是做空  
- 普通交易已購入，等待賣出  
- 做空已售出，等待買回  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        N = len(prices)
        # state:
        # 0: 等待交易
        # 1: 普通交易，已買入，等賣出
        # 2: 做空，已賣出，等買回

        @cache
        def dp(i, rem, state):
            if i == N:
                return 0 if state == 0 else -inf

            res = dp(i+1, rem, state)  # 不交易
            x = prices[i]
            if state == 0:
                if rem > 0:
                    res = max(res, dp(i+1, rem-1, 1) - x)  # 普通交易先買
                    res = max(res, dp(i+1, rem-1, 2) + x)  # 做空先賣
            elif state == 1:
                res = max(res, dp(i+1, rem, 0) + x)  # 普通交易賣出
            else:
                res = max(res, dp(i+1, rem, 0) - x)  # 做空買回
            return res

        ans = dp(0, k, 0)
        dp.cache_clear()

        return ans
```
