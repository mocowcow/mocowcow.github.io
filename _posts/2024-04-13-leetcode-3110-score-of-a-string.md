---
layout      : single
title       : LeetCode 3110. Score of a String
tags        : LeetCode Easy String Simulation
---
雙周賽 128。

## 題目

輸入字串 s。  
字串的**分數**定義為字串中相鄰字元的 **ASCII** 差值總和。

求 s 的分數。  

## 解法

直接按照題意，枚舉相鄰的字元對，計算差值就行。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for a, b in pairwise(s):
            ans += abs(ord(a) - ord(b))
            
        return ans  
```

python 一行版本。  

```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a) - ord(b)) for a, b in pairwise(s))
```
