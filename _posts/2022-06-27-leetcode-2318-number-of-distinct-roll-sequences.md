--- 
layout      : single
title       : LeetCode 2318. Number of Distinct Roll Sequences
tags        : LeetCode Hard DP
---
雙周賽81。一眼就知道是DP，但想不出轉移方程，剛開始還把間隔搞錯，沒有及時寫出來。

# 題目
你有一個公平的六面骰子，總共骰n次，求有多少獨特的骰動數值序列符合以下條件：  
- 兩個相鄰的骰動數值之間，gcd必須為1  
- 相同的數字至少要間隔兩次以上不同數字，才能再次出現  

例如：
> n = 4  
> 合法的序列包括：(1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1)  
> 不合法序列：(**1**, 2, **1**, 3) 兩次1的間隔不足  
> 不合法序列：(1, 2, **3**, **6**) 3和6的gcd不為1  

答案可能很大，必須模10^9+7後回傳。

# 解法
每次骰動之前，需要先檢查前一次和前前一次的數值，才能決定這次有那些數字合法。  
定義dp(i,prev,pprev)：上一次數值為prev，且上上次數值為pprev，骰完7次後的合法序列數量。  
轉移方程式：dp(i,prev,pprv)=sum(dp(i-1,**j**,prev) 其中j不同於prev和pprev且gcd(j,prev)為1)  
base cases：當i=0時，沒有骰過半次，當然只有空序列一種結果，回傳1。  

依照dp定義，我們要求的答案就是dp(m,None,None)。
可是前兩次骰動的時候會使用到None，而None又不能和整數一起丟進gcd處理，必須分開判斷：  
- 當prev為空時，pprev肯定也為空。所以1\~6的數字都可以選。  
- 當pprev為空時，只要判斷當前選擇的數字j和prev不同，且gcd為1即可。  
- 否則為一般情形，prev、pprev必須不同於j，且j和prev的gcd為1。  

prev和pprev的狀態各有6種，而當前可選的數字6種，計算成本為6^3。共要計算n次，故整體時間複雜度為O(n*(6^3))，可簡化為O(n)。  

```python
class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD=10**9+7
        
        @cache
        def dp(i,prev,pprev):
            if i==0:
                return 1
            ans=0
            if prev==None:
                for j in range(1,7):
                    ans+=dp(i-1,j,None)
            elif pprev==None:
                for j in range(1,7):
                    if j!=prev and gcd(j,prev)==1:
                        ans+=dp(i-1,j,prev)
            else:
                for j in range(1,7):
                    if j!=pprev and j!=prev and gcd(j,prev)==1:
                        ans+=dp(i-1,j,prev)
            return ans%MOD
            
        return dp(n,None,None)
```

把三個邏輯合併起來，看起來稍微簡潔一些。

```python
class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD=10**9+7
        
        @cache
        def dp(i,prev,pprev):
            if i==0:
                return 1
            ans=0
            for j in range(1,7):
                if prev==None or (pprev!=j and prev!=j and gcd(prev,j)==1):
                    ans+=dp(i-1,j,prev)
            return ans%MOD
            
        return dp(n,None,None)
```