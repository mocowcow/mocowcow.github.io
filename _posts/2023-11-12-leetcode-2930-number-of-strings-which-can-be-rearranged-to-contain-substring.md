---
layout      : single
title       : LeetCode 2930. Number of Strings Which Can Be Rearranged to Contain Substring
tags        : LeetCode Medium Array String DP Math
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

排容原理又來了，一樣是找出所有字串，扣掉不合法的。  
字串總共有26^n種排列。  

滿足以下任一可以使字串不合法：  

- 沒l  
  l之外任選n次，即25^n  
- 沒t  
  同上，25^n  
- 沒ee  
  沒有任何e的情況同上，25^n  
  但可以有一個e，其他位置填非e，即n\*25^(n-1)  

不合法的字串也就是三種條件的聯集。  
根據排容原理：  
> A∪B∪C = A+B+C-A∩B-A∩C-B∩C+A∩B∩C  

符合兩項條件的地方重複計算，需要扣除。  

- 沒l也沒t  
  l,t以外任選n次，即24^n  
- 沒t且沒ee  
  t,e以外任選n次，即24^n  
  但可以有一個e，其他位置填非e,t，即n\*24^(n-1)  
- 沒l且沒ee  
  同上，n\*24^(n-1)  

最後補上三項條件皆滿足的部分。  

- 沒l且沒t且沒ee  
  l,t,e以外任選n次，即23^n  
  但可以有一個e，其他位置填非l,e,t，即n\*23^(n-1)  

答案記得要取餘數。  

時間複雜度O(log n)，在於快速冪求n次方。  
空間複雜度O(1)。  

```python
class Solution:
    def stringCount(self, n: int) -> int:
        MOD=10**9+7
        tot=pow(26,n,MOD)
        
        # no "l"
        exclude=pow(25,n,MOD)
        # no "t"
        exclude+=pow(25,n,MOD)
        # no "ee"
        exclude+=pow(25,n,MOD)+n*pow(25,n-1,MOD)        
        
        # no "l" && no "t"
        exclude-=pow(24,n,MOD)
        # no "l" && no "ee"
        exclude-=pow(24,n,MOD)+n*pow(24,n-1,MOD)
        # no "t" && no "ee"
        exclude-=pow(24,n,MOD)+n*pow(24,n-1,MOD)
        
        # no "l" && no "t" && no "ee"     
        exclude+=pow(23,n,MOD)+n*pow(23,n-1,MOD)
        
        return (tot-exclude)%MOD
```
