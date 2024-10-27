---
layout      : single
title       : LeetCode 3335. Total Characters in String After Transformations I
tags        : LeetCode Medium DP
---
weekly contest 421。  
竟然在 Q2 就有 dp，受到驚嚇。  

## 題目

輸入字串 s 和 整數 t，代表**轉換**次數。  
每次**轉換**須按照以下規則替換字元：  

- 若字元是 'z'，則將其替換成 "ab"。  
- 否則替換成字母表中的下個字元。例如 'a' 變成 'b'，'b' 變成 'c'，以此類推。  

求字串進行**正好** t 次**轉換**後的長度。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

字串中的所有字元都是**獨立**的，彼此互不影響。  
例如 "aaa" 可以看做是三個 "a" 分別轉換 t 次。  
而 "z" 轉換後則拆成兩個 "a" 和 "b" 分別轉換 t-1 次。  
不同的字元都有相同的結果，是**重疊的子問題**，考慮 dp。  

"z" 會對 "a", "b" 產生貢獻，這邊用**填表法**比較好寫。  
首先統計 s 中各自元的頻率，然後模擬轉換 t 次。  

時間複雜度 O(N + 26t)。  
空間複雜度 O(26)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        f = [0] * 26
        for c in s:
            f[ord(c)-97] += 1

        for _ in range(t):
            f2 = [0] * 26
            # a~x
            for i in range(25):
                f2[i+1] = f[i]
            # z
            f2[0] += f[25]
            f2[1] += f[25]
            f = f2

        return sum(f) % MOD        
```
