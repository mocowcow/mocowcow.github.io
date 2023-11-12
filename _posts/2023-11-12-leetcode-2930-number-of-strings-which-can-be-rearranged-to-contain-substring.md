---
layout      : single
title       : LeetCode 2930. Number of Strings Which Can Be Rearranged to Contain Substring
tags        : LeetCode Medium Array String DP
---
雙周賽117。我在那邊搞排容原理搞一輩子，都沒想到dp也可以做，還簡單的很。  

## 題目

輸入整數n。  

一個由小寫字母組成的字串s，如果排序後可以包含子字串"leet"，則稱為**好的**。  

例如：  

- "lteer"可以重排成"leetr"，是好的  
- "letl"重排後無法得到"leet"，不是好的  

求有多少長度n的**好的字串**。  
答案可能很大，先模10^9+7後回傳。  

## 解法

必要條件是一個l、一個t、兩個e。  

對於一個長度n的字串，可以由長度n-1的字串加上任意一種字母而來。  
字串的組成是決定**選哪個**字母加上去，因此考慮dp。  

我們只在乎let三字母的出現次數。而且一旦滿足，再多也沒有意義。  
換句話說，"leeet"和"lleettt"的效果都等價於"leet"，都是合法的。  

定義dp(n,l,e,t)：長度為n，且需要有l個l、e個e、t個t的字串，總共有幾種。  
轉移方程式：dp(n) = dp(n-1)拿其他 + dp(n-1)拿l + dp(n-1)拿e + dp(n-1)拿t  
base case：當n=0時，不能繼續選，如果let需求都滿足，則回傳1；否則不合法，回傳0。  

dp狀態共有n\*l\*e\*t個，其中l\*e\*t為視作常數。  
每個狀態轉移4次。  
時間複雜度O(n)。  
空間複雜度O(n)。  

```python
class Solution:
    def stringCount(self, n: int) -> int:
        MOD=10**9+7
            
        @cache
        def dp(n,l,e,t):
            if n==0:
                return int(l+e+t==0)
            # take other
            res=dp(n-1,l,e,t)*23
            # take l
            res+=dp(n-1,max(0,l-1),e,t)
            # take e
            res+=dp(n-1,l,max(0,e-1),t)
            # take t
            res+=dp(n-1,l,e,max(0,t-1))
            return res%MOD
        
        return dp(n,1,2,1)
```
