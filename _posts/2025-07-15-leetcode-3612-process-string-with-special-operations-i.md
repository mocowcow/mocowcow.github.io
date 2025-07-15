---
layout      : single
title       : LeetCode 3612. Process String with Special Operations I
tags        : LeetCode Medium Simulation
---
weekly contest 458。  
感覺比上周 Q1 簡單很多，不太懂為什麼是中等。  

## 題目

<https://leetcode.com/problems/process-string-with-special-operations-i/description/>

## 解法

題目本身按照題目模擬即可，值得一講的是複雜度分析。  

最差情況下執行 N 次複製操作，最終字串長度為 2^N。  
2^N 長度複製 N 次，複雜度 O(N \* 2^N)。  

但仔細觀察字串長度變化：  
> 1, 2, 4, .., 2^(N-1), 2^N  

從第一項加到 2^(N-1)，正好是 (2^N) - 1。  
全部加起來只是兩倍的 2^N 次字元操作而已，常數可忽略。  

時間複雜度 O(2^N)。  
空間複雜度 O(1)，答案空間不計。  

```python
class Solution:
    def processStr(self, s: str) -> str:
        a = []
        for c in s:
            if c == "*":
                if a:
                    a.pop()
            elif c == "#":
                a += a
            elif c == "%":
                a.reverse()
            else:
                a.append(c)

        return "".join(a)
```
