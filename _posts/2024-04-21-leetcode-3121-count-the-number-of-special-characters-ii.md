---
layout      : single
title       : LeetCode 3121. Count the Number of Special Characters II
tags        : LeetCode Medium String Simulation HashTable Simulation
---
周賽 394。

## 題目

輸入字串 word。  
若某個字元的**大寫和小寫**都有在 word 中出現，而且該字元 c 的所有小寫都在大寫**之前**出現，則稱為**特殊的**。  

求有多少個**特殊的**字元。  

## 解法

跟前一題很像，只是增加出現位置的約束。  
我們只要知道**最後一個小寫**和**第一個大寫**的索引，就能判斷是否合法。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {} 
        upper = {} 
        
        for i, c in enumerate(word):
            if c.islower(): # last lower
                lower[c] = i
            elif c not in upper: # first upper
                upper[c] = i
                
        ans = 0
        for c in string.ascii_lowercase:
            if c.upper() in upper and c in lower:
                if upper[c.upper()] > lower[c]:
                    ans += 1
                    
        return ans
```
