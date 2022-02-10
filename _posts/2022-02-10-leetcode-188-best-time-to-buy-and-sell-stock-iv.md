---
layout      : single
title       : LeetCode 188. Best Time to Buy and Sell Stock IV
tags 		: LeetCode Hard DP Array
---
DP教學系列。[這題](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)的進化版。

# 題目
輸入一個正整數陣列prices及整數k，prices表示各日股價，求買賣k次最多可以獲利多少。

# 解法
其實這題滿難想的，當初也是看人家討論才懂，但是理解之後就很容易了。  

>步驟1：定義狀態  

影響的變數有prices跟次數k，採用二維DP，而且有買/賣兩個狀態，所以需要分buy, sell兩個DP陣列。    
buy[p][i]表示帶入第p個股價時，買入第i次的最佳情況，sell[p][i]表示賣出。  


>步驟2：找出狀態轉移方程式  

想要賣一定得先買入，而且要比已知狀況更賺錢，所以sell[p][i]=max(sell[p][i],buy[p][i]+prices[p])。  
而要買第i次時是使用上一次買賣的盈餘資本，而且要比已知況狀更省錢，所以buy[p][i]=max(buy[p][i],sell[p][i-1]-prices[p])。

>步驟3：處理base cases

雖說買第i次要用賣完第i-1次的盈餘，但是買第1次時，哪來的賣第0次？  
sell[0]設為-inf防止出錯，且任何價格都可以更新。

```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [-math.inf]*(k+1)
        sell = [0]*(k+1)
        
        for p in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1]-p)
                sell[i] = max(sell[i], buy[i]+p)

        return sell[-1]
```
