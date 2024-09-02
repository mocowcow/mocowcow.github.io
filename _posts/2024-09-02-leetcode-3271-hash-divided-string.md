---
layout      : single
title       : LeetCode 3271. Hash Divided String
tags        : LeetCode Medium String Simulation
---
biweekly contest 138。好像其實是 Q1 難度，可能題目很長才算中等題。  

## 題目

輸入長度 n 的字串 s，還有整數 k。保證 n 是 k 的倍數。  
你必需將 s 雜湊成一個新字串 result，其長度為 n / k。  

起初 result 是**空字串**。
將 s 分割成 n / k 個長度為 k 的子字串，並按照順序處理：  

- 每個字元的**雜湊值**是**英文字母順序** ('a' = 0, 'b' = 1, .., 'z' = 25)。  
- 計算子字串中所有字元的**雜湊值總和**。  
- 找出雜**湊總和**除 26 後的餘數，記做 hashedChar。  
- 將 hashedChar 對應的英文字母加回 result 尾端。  

回傳 result。  

## 解法

按照題意模擬即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)，答案空間不計入。  

```python
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        N = len(s)
        ans = []
        for i in range(0, N, k):
            res = 0
            for c in s[i:i + k]:
                res += ord(c) - 97
            ans.append(chr(res % 26 + 97))

        return "".join(ans)
```
