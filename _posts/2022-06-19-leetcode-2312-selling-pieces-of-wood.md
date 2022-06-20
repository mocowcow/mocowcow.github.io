--- 
layout      : single
title       : LeetCode 2312. Selling Pieces of Wood
tags        : LeetCode Hard Array DP
---
周賽298。雖然知道是DP但不知道怎麼切塊，想了半天想不出，好苦。  
雖然官方標籤有個回溯，但我還真沒看到有人用回溯解法。  

# 題目
輸入整數m和n，代表一塊長方形木頭的高度和寬度。還有一個二維整數陣列prices，其中prices[i] = [hi, wi, pricei]表示高度為hi且寬度為wi的木頭售價為pricei。  

你可以多次將**整塊**木頭垂直或水平切割，將其分成兩個較小的部分。切成多塊後依不同價格出售，同樣形狀的木頭可以出售多次，且不必出售每種形狀。  
木頭紋理有所不同，因此不能通過旋轉來交換的度和寬度。  

回傳切割一塊m*n木頭所獲得的最大利潤。  

# 解法
當時一直糾結木頭有很多種切法，不知道怎麼切，重新看過題目才發現：**一刀下去必定使某塊木頭變成兩半**。有這個大前提問題就簡單很多，至少不會出現什麼螺旋結構。  

根據一刀兩斷的原則，假設一塊5*4的木頭，可以有4種橫切方式，分別切出高度為[1+4, 2+3, 3+2, 4+1]的兩塊木頭；還有三種縱切方式，分別切出寬度為[1+3, 2+2, 3+1]的兩塊木頭。但1+4和4+1其實是對撐的，順序並不重要，所以只需要切到長/寬一半即可。  

接下來dp狀態定義就很清楚了：dp(i,j)為一塊高度i寬度j的木頭最大出售利潤。  
轉移方程式：dp(i,j)=max(整塊出售, dp(各種橫切), dp(各種縱切))  
base cases：當i或j等於0時，沒有這種木頭，直接回傳0。  

```python
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        d=defaultdict(int)
        for a,b,p in prices:
            d[(a,b)]=p
            
        @cache
        def dp(i,j):
            if i==0 or j==0:
                return 0
            best=d[(i,j)]
            for k in range(1,i//2+1):
                best=max(best,dp(i-k,j)+dp(k,j))
            for k in range(1,j//2+1):
                best=max(best,dp(i,j-k)+dp(i,k))
            return best
        
        return dp(m,n)
```

改成bottom up，從最小塊的木頭開始往上計算。

```python
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp=[[0]*205 for _ in range(205)]
        for a,b,p in prices:
            dp[a][b]=p
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                for k in range(1,i//2+1):
                    dp[i][j]=max(dp[i][j],dp[i-k][j]+dp[k][j])
                for k in range(1,j//2+1):
                    dp[i][j]=max(dp[i][j],dp[i][j-k]+dp[i][k])
                
        return dp[m][n]
```