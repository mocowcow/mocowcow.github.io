---
layout      : single
title       : LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee
tags 		: LeetCode Medium DP Greedy Array
---
DP教學系列。其實也可以不DP。

# 題目
輸入一個正整數陣列prices及整數fee，prices表示各日股價，而每次賣出都須收取手續費fee。可以買賣無限次，求最大利潤多少。

# 解法

>步驟1：定義狀態  

變數只有prices，採用一維DP，但有買/賣兩個狀態，所以分成buy, sell兩個DP陣列。    
buy[p][i]表示帶入第p個股價時，買入第i次的最佳情況，sell[p][i]表示賣出。  


>步驟2：找出狀態轉移方程式  

想要賣一定得先買入，而且扣完手續費還要有賺錢，所以sell[p][i]=max(sell[p][i],buy[p][i]+prices[p]-fee)。  
而要買第i次時是使用上一次買賣的盈餘資本，而且要比已知況狀更省錢，所以buy[p][i]=max(buy[p][i],sell[p][i-1]-prices[p])。

>步驟3：處理base cases

第一天沒有庫存股可以賣，sell一定是0。也只有一個選擇可以買，buy=-prices[0]。

因為只用到前一天的狀態，所以空間壓縮成一維。
而且一天內只會有買或是賣，不可能同時發生，所以sell,buy不會在同一天更新，不需要考慮暫存問題。

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = 0
        buy = -prices[0]

        for p in prices:
            sell = max(sell, buy+p-fee)
            buy = max(buy, sell-p)

        return sell
```

提供另一個我更喜歡的解法。維護一個stock變數表示之前買入的股價，如果買入價扣掉手續費>當天股價，代表有賺，加入利潤並更新買入價。若當天股價低於先前買入價，則更新最低買入價。  
特別解釋一下為何賣出時更新的買入價要預先扣掉fee？
因為搞不好你隔天會碰到更好的賣價，實際上只要花一次手續費而已。  
例如：
> prices=[...10,15,16], fee=2  
> 手上成本價10，第n天時價15，第n日最大利潤15-10-2=3  
> n+1日時價16，代表第n天不賣才能利潤最大化，第n+1日最大利潤應為16-10-2=4

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        stock = math.inf
        for p in prices:
            if p-fee > stock:
                profit += p-stock-fee
                stock = p-fee
            elif p < stock:
                stock = p

        return profit
```