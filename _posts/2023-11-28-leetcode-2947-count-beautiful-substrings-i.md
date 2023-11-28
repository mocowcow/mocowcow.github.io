---
layout      : single
title       : LeetCode 2947. Count Beautiful Substrings I
tags        : LeetCode
---
周賽373。

## 題目

輸入字串s和正整數k。  

定義vow和con分別代表字串中母音和子音的個數。  

一個**美麗**的字串滿足：  

- vow == con  
- (vow \* con) % k ==0，換句話說，vow和con的乘積能被k整除  

求字串s中有多少**非空**的**美麗子字串**。  

## 解法

先來個暴力解，枚舉所有子字串，並維護母音子音個數，滿足條件答案就+1。  

時間複雜度O(N^2)。  
空間複雜度O(1)。  

```python
vowel=set("aeiou")

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        N=len(s)
        ans=0
        for i in range(N):
            vow=0
            con=0
            for j in range(i,N):
                if s[j] in vowel:
                    vow+=1
                else:
                    con+=1
                    
                if vow==con and (vow*con)%k==0:
                    ans+=1
                    
        return ans
```
