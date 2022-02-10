---
layout      : single
title       : LeetCode 518. Coin Change 2
tags 		: LeetCode Medium DP Array
---
DP教學系列。換錢幣計數版。

# 題目
輸入整數陣列coins，代表硬幣幣值，整數amount代表金額，求使用各種幣值換錢，湊到amount有幾種組合。

# 解法

>步驟1：定義狀態  

影響的變數有coins及amount，需要二維DP。  
dp[c][i]代表代入第c種幣值時，換到i元有多少組合。

>步驟2：找出狀態轉移方程式  

每代入一個新幣值coin，dp[c][i]的組合數會增加dp[c-1][i-coin]。  
方程式為dp[c][i]=dp[c-1][i]+dp[c-1][i-coin]。

>步驟3：處理base cases

要湊到0元只有一種組合，dp[i][0]設1。

直接bottom-up了，空間壓縮到一維。

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1   
        
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]+=dp[i-coin]

        return dp[-1]
```
