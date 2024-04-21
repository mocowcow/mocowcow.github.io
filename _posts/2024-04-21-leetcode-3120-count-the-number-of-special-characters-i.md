---
layout      : single
title       : LeetCode 3120. Count the Number of Special Characters I
tags        : LeetCode Easy Array String Simulation BitManipulation Bitmask
---
周賽 394。

## 題目

輸入字串 word。  
若某個字元的**大寫和小寫**都有在 word 中出現，則稱為**特殊的**。  

求有多少個**特殊的**字元。  

## 解法

枚舉 26 種字元，分別找大小寫即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0 
        for c in string.ascii_lowercase:
            if c in word and c.upper() in word:
                ans += 1
                
        return ans
```

也可以先掃一次 word，預處理所有字元的大小寫出現情況。  
因為字母只有 26 個，可以使用整數作為 bitmask 維護出現狀況。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper = 0
        lower = 0
        for c in word:
            a = ord(c)
            if a >= 97: 
                lower |= (1 << (a - 97))
            else:
                upper |= (1 << (a - 65))
        
        ans = 0
        for i in range(26):
            mask = 1 << i
            if upper & mask and lower & mask:
                ans += 1
                
        return ans
```
