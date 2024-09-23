--- 
layout      : single
title       : LeetCode 2707. Extra Characters in a String
tags        : LeetCode Medium String DP
---
雙周賽 105。這題用 python 是真的好寫，不少人被這題卡住。  

## 題目

輸入字串 s，還有各單字的字典 dictionary。  
你必須將 s 分割成數個**不重疊**子字串，且子字串必須在 dictionary 中。s 中可以有某些不屬於任何子字串的**多餘字元**。  

求s以最佳方式拆分後，最少有幾個**多餘字元**。  

## 解法

雖然從s中以任意順序切出子字串，但是如果先切中間，前後段的字串很難處理，不如固定一個方向切。  

對於一個字串s有兩種情況：  

- 前綴剛好是 dictionary 中的某個字 word，將 word 從 s 前方刪掉，繼續匹配  
- 把第一個字元視為**多餘**，刪掉第一個字元，繼續匹配  

不同的匹配方式有可能得到相同的結果，例如：  
> s = "aab", dictionary = ["a", "aa"]  
> 第一種可能：匹配到兩個 "a"，最後剩下 "b" 是多餘的  
> 第二種可能：匹配到 "aa"，最後剩下 "b" 是多餘的  

擁有重疊的子問題，很明顯需要 dp。  

---

定義 dp(s)：字串 s 的最小**多餘字元**數量。  
轉移：min(dp(ns) FOR ALL w + ns = s)，其中 w 為 dictionary 任意單字。  
base：當 s 為空字串時，不需繼續匹配，答案為 0。

只能由前方依序刪除字元，至多產生 N 個狀態。  
每個狀態需要對 M 個字串配對轉移，每次配對 O(N)。  

時間複雜度 O(N^2 \* M)，其中 N = len(s)，M = len(dictionary)。  
空間複雜度 O(N^2)。  

```python
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        @cache
        def dp(s):
            if s == "":
                return 0
            res = 1 + dp(s[1:])
            for w in dictionary:
                if s.startswith(w):
                    ns = s[len(w):]
                    res = min(res, dp(ns))
            return res

        return dp(s)
```
