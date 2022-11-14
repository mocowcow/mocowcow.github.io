--- 
layout      : single
title       : LeetCode 2466. Count Ways To Build Good Strings
tags        : LeetCode Medium Array DP
---
雙周賽91。才想說Q2放dp有點誇張，後來才發現這題算五分，是平常的Q3難度。  

# 題目
輸入整數0, 1, low和high，我們要從一個空字串開始構造一個字串，並在每一步執行以下任一操作：  
- 將字元"0"附加zero次  
- 將字元"1"附加one次  

你可以執行任意次操作。  

若一個字串是由上述過程所構造，且其長度在low和high(含)之間，則稱為**好字串**。  
求有多少符合以上條件的**好字串**。答案可能很大，需模10^9+7後回傳。  

# 解法
看到模運算就要知道是dp了。至於長度為i的字串，可以由長度為i-one或是i-zero的字串所組成，遞推公式就出來了。  

定義dp(i)：長度為i的好字串。  
轉移方程式：dp(i)=dp(i-zero)+dp(i-one) 。
base cases：若i小於0，不存在複數長度字串，回傳0；若等於0，只有一種組成空字串的方式，回傳1。  

最後將low\~high長度的字串數量加總得到答案。  

時空間複雜度都是O(N)。  

```python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD=10**9+7
        
        @cache
        def dp(i):
            if i<0:return 0
            if i==0:return 1
            return (dp(i-zero)+dp(i-one))%MOD
        
        ans=0
        for i in range(low,high+1):
            ans=(ans+dp(i))%MOD
        
        return ans
```

前陣子看到關於dp的文章，文中提到dp還可以分為**填表法**和**刷表法**，今天正好理解其中差異。  
大部分的時候都是只用前者的**填表法**，是從若干個已經求出的子問題答案來推出當前答案，**填入空格中**。  
在此例就是參考dp[i-one]和dp[i-zero]的答案，來求出dp[i]。  

```python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD=10**9+7
        dp=[0]*(high+1)
        dp[0]=1
        
        for i in range(high+1):
            if i>=zero:dp[i]=(dp[i]+dp[i-zero])%MOD
            if i>=one:dp[i]=(dp[i]+dp[i-one])%MOD
        
        ans=0
        for i in range(low,high+1):
            ans=(ans+dp[i])%MOD
        
        return ans
```

至於刷表法則是預判當前答案會**對哪些未來產生影響**，直接將貢獻的值更新上去。  
相當於dp[i]的值會影響到dp[i+one]和dp[i+zero]的答案。  

```python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD=10**9+7
        dp=[0]*(high+1)
        dp[0]=1
        
        for i in range(high+1):
            if i+zero<=high:dp[i+zero]=(dp[i+zero]+dp[i])%MOD
            if i+one<=high:dp[i+one]=(dp[i+one]+dp[i])%MOD
        
        ans=0
        for i in range(low,high+1):
            ans=(ans+dp[i])%MOD
        
        return ans
```