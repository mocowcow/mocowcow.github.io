---
layout      : single
title       : LeetCode 3210. Find the Encrypted String
tags        : LeetCode Easy Array String Simulation
---
周賽 405。

## 題目

輸入字串 s 和整數 k。使用以下演算法加密：  

- 對於 s 中每個字元 c，將其替換成 c 之後的第 k 個字元 (以循環方式)  

回傳加密後的字串。  

## 解法

按照題意模擬，記得對 i + k 模 N。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        N = len(s)
        ans = [0] * N
        for i in range(N):
            ans[i] = s[(i + k) % N]
            
        return "".join(ans)
```

隨便舉個簡單例子：  
> s = "abcd", k = 1  
> ans = "bcda"  

發現其實就是把前 k 個字元搬到後面去。  
注意 k 可能比字串大小 N 還大，記得先對 k 模 N。  

```python
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k %= len(s)
        return s[k:] + s[:k]
```
