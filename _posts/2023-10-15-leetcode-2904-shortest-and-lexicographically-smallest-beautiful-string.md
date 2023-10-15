---
layout      : single
title       : LeetCode 2904. Shortest and Lexicographically Smallest Beautiful String
tags        : LeetCode Medium String Simulation
---
周賽367。

## 題目

輸入二進位字串s，還有正整數k。  

如果一個s的子字串正好包含k個1字元，則稱為**美麗的**。  

令len為**最短**美麗子字串的長度。  

回傳字典序**最小**、且長度為len的美麗子字串。若不存在則回傳空字串。  

## 解法

從小到大枚舉子字串長度size，並維護長度為size的最小美麗子陣列。若找到直接回傳。  

時間複雜度O(n^3)。  
空間複雜度O(n)。  

```python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        N=len(s)
        ans=""
        
        for size in range(1,N+1):
            for i in range(N):
                sub=s[i:i+size]
                if sub.count("1")==k and (ans=="" or sub<ans):
                    ans=sub
            if ans!="":
                return ans
                    
        return ""
                    
```
