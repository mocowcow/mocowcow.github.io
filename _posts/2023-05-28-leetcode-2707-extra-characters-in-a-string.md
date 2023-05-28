--- 
layout      : single
title       : LeetCode 2707. Extra Characters in a String
tags        : LeetCode Medium String DP
---
雙周賽105。這題用python是真的好寫，不少人被這題卡住。  

# 題目
輸入字串s，還有各單字的字典dictionary。  
你必須將s分割成數個**不重疊**子字串，且子字串必須在dictionary中。s中可以有某些不屬於任何子字串的**多餘字元**。  

求s以最佳方式拆分後，最少有幾個**多餘字元**。  

# 解法
雖然從s中以任意順序切出子字串，但是如果先切中間，前後段的字串很難處理，不如固定一個方向切。  

對於一個字串s有兩種情況：  
- 前綴剛好是dictionary中的某個字word，將word從s前方刪掉，繼續匹配  
- 把第一個字元視為**多餘**，刪掉第一個字元，繼續匹配  

不同的匹配方式有可能得到相同的結果，例如：  
> s = "aab", dictionary = ["a", "aa"]  
> 第一種可能：匹配到兩個"a"，最後剩下"b"是多餘的  
> 第二種可能：匹配到"aa"，最後剩下"b"是多餘的  

擁有重疊的子問題，很明顯需要dp。  

定義dp(s)：字串s的最小**多餘字元**數量。  
轉移方程式：min(dp(ns) FOR ALL w+ns=s)，其中w為dictionary任意單字  
base case：當s為空字串時，不需繼續匹配，多餘字元為0  

每次匹配前綴最多O(N)，s最多產生N個子字串，時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        @cache
        def dp(s):
            if s=="":
                return 0
            ans=dp(s[1:])+1
            for w in dictionary:
                if s.startswith(w):
                    ns=s[len(w):]
                    ans=min(ans,dp(ns))
            return ans
        
        return dp(s)  
```
