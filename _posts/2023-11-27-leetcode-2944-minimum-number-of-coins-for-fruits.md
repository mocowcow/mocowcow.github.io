---
layout      : single
title       : LeetCode 2944. Minimum Number of Coins for Fruits
tags        : LeetCode Medium Array DP
---
雙周賽118。這題描述也挺爛的，範例也很爛，看半天才知道他想幹嘛。  

## 題目

有一間水果店，賣幾種不同的水果。  

輸入索引從1開始的陣列prices，其中prices[i]代表第i個水果的價格。  

水果店的報價如下：  

- 若你付prices[i]購買第i個水果，則接下來的i個水果都可以免費  

注意：即使你**能免費**拿第j個水果，也依然可以選擇付費以取得優惠。  

求購買所有水果所需的**最少花費**。  

## 解法

> If you purchase the ith fruit at prices[i] coins, you can get the next i fruits for free.  

題目也沒說要按照什麼順序買，鬼才知道next i是什麼意思。看範例才確定是指從i開始往右邊數i個。  

買了水果只有右邊的會免費，因此由左到右遍歷每個水果i。i可以選擇付費或不付費，考慮dp。  
定義dp(i,free)：依序購買第i\~N個水果，且當前免費次數剩下free次時，所需的最小花費。  
轉移方程式：dp(i,free) = max(付費, 免費)  
付費=dp(i+1,i)+prices[i-1]；免費=dp(i+1,free-1)  
base case：當free<0時，代表免費次數不夠，回傳inf；當i>N代表水果買完，回傳0。  

時間複雜度O(N^2)，其中N為prices長度，同時也是免費次數的最大值。  
空間複雜度O(N^2)。  

```python
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        N=len(prices)
        
        @cache
        def dp(i,free):
            if free<0:
                return inf
            if i>N:
                return 0
            pay=dp(i+1,i)+prices[i-1]
            free=dp(i+1,free-1)
            return min(pay,free)
        
        return dp(1,0)
```
