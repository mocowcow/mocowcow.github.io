---
layout      : single
title       : LeetCode 3120. Count the Number of Special Characters I
tags        : LeetCode Easy Array String Simulation
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
