---
layout      : single
title       : LeetCode 322. Coin Change
tags 		: LeetCode Medium DP
---
DP教學系列。經典中的經典，似乎是幾年前首次接觸DP時碰到的。

# 題目
輸入整數陣列coins，代表硬幣幣值，整數amount代表金額，求使用各種幣值換錢，湊到amount最少需要幾個硬幣。

# 解法
這題要我寫出top-down還真不太好寫，思維已經完全是迭代的形狀了。但還是照著框架寫寫看。

>步驟1：定義狀態  

影響的變數有coins及amount，需要二維DP。  
dp[c][i]代表代入第c種幣值時，換到i元最少需要多少硬幣。

>步驟2：找出狀態轉移方程式  

當試著帶入新幣值coin時，dp[c][i]如果換入一個coin，新數量會是dp[上一個幣值][i-當前幣值]+1，如果新數量小於原本數量才更新。  
dp[c][i]=min(dp[c][i], dp[c-1][i-coin]+1)。

>步驟3：處理base cases

dp[c][i]，i<0時是inf，因為不存在負數金額。i=0時回傳0，因不需要任何硬幣就可達成。

以前代入過的幣值就不重要了，只會用到上一次的結果，且都是從頭循序，DP陣列可以壓縮到一維。

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                if dp[i-coin]+1 < dp[i]:
                    dp[i] = dp[i-coin]+1

        return dp[-1] if dp[-1] != math.inf else -1
```
