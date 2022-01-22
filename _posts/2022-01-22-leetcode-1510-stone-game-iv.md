---
layout      : single
title       : LeetCode 1510. Stone Game IV
tags 		: LeetCode Hard DP
---
Stone Game系列使我想起某次競賽的慘況，AC率只有10%，好險這題沒那麼刁鑽。拜託Alice和Bob玩點簡單的遊戲吧！

# 題目
Alice和Bob又在玩石頭，一樣是Alice先手，每人一次可拿走平方數的石頭(1,4,9...)，沒石頭可拿的人就算輸。  
假設兩人都採最佳策略，如果Alice能獲勝則回傳True，否則False。

# 解法
沒石頭的人就算輸，當n=0時就是False。  
採用top-down的方式DP，對所有可選的平方數遞迴，如果可以使剩下的石頭數(n-i*i)為False時，則n為True。

```python
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dp(n):
            if n == 0:  # base case
                return False
            i = 1
            while i*i <= n:
                if not dp(n-i*i):
                    return True
                i += 1
            return False

        return dp(n)

```

改用陣列bottom-up的版本，比前者快了不少。

```python
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                if not dp[i-j*j]:
                    dp[i] = True
                    break
                j += 1

        return dp[n]

```
