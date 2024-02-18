---
layout      : single
title       : LeetCode 3039. Apply Operations to Make String Empty
tags        : LeetCode Medium String Array HashTable
---
雙周賽124。

## 題目

輸入字串 s。  

重複以下操作，直到 s 變成空字串為止：  

- 對於 'a' 到 'z' 的每個字元，若存在於 s 之中，則刪除 s 中**最早**出現的該字元  

例如 s = "aabcbbca"，操作順序如下：  

- "**a**a**bc**bbca" 刪除粗體部分，變成 "abbca"
- "**ab**b**c**a" 刪除粗體部分，變成 "ba"  
- "**ba**" 刪除粗體部分，變成""  

求 s 執行**最後一次**操作**之前**的狀態。以上例而言，答案為 "ba"。  

## 解法

每次操作，每種字元都會被刪掉一個。  
所以出現越多次的字元可以留越久，最後被刪的字元也是**出現次數最多**的字元。  

先統計各字元的出現次數，並維護各字元**最後一次出現**的位置。  
找到最大的出現次數 mx_freq，並把出現 mx_freq 的字元填上所屬位置。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        N = len(s)
        freq = Counter(s)
        last_idx = {c:i for i, c in enumerate(s)}
        
        ans = [""] * N
        mx_freq = max(freq.values())
        for k, v in freq.items():
            if v == mx_freq:
                idx = last_idx[k]
                ans[idx] = k
                
        return "".join(ans)
```
