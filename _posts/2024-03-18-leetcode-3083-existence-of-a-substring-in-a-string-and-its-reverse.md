---
layout      : single
title       : LeetCode 3083. Existence of a Substring in a String and Its Reverse
tags        : LeetCode Easy String Simulation
---
周賽 389。

## 題目

輸入字串 s，找到任意一個長度為 2，並且出現在反轉後的 s 的子字串。  

若存在則回傳 true，否則回傳 false。  

## 解法

測資很小，怎樣搞都可以。  
最爛又最快的的方式就是反轉 s，然後枚舉子字串去裡面找。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        N = len(s)
        rev = s[::-1]
        
        for i in range(N - 1):
            sub = s[i:i+2]
            if sub in rev:
                return True
            
        return False
```

更好的解法預處理反轉後、長度為 2 的子字串，放到集合裡面查詢。  
之後枚舉子字串查找只需要 O(1)。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        N = len(s)
        rev = s[::-1]
        seen = set()
        for i in range(N - 1):
            seen.add(rev[i:i + 2])
            
        for i in range(N - 1):
            if s[i:i + 2] in seen:
                return True
            
        return False
```
