---
layout      : single
title       : LeetCode 3084. Count Substrings Starting and Ending with Given Character
tags        : LeetCode String 
---
周賽 389。這幾題的敘述都很精簡，非常省時間。  

## 題目

輸入字串 s 還有字元 c。  
求 s 裡面有多少子字串是以 c **開頭和結尾**。  

## 解法

每個 c 都能和自己組成子字串，或是和左方的任意 c 組成子字串。  
當他第一次出現，可以產生 1 個子字串；第二次產生 2 個，以此類推。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = 0
        ans = 0
        for cc in s:
            if cc == c:
                cnt += 1
                ans += cnt
                
        return ans
```
