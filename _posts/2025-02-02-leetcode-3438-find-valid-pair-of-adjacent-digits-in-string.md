---
layout      : single
title       : LeetCode 3438. Find Valid Pair of Adjacent Digits in String
tags        : LeetCode Easy Simulation
---
biweekly contest 149。

## 題目

<https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/description/>

## 解法

字元計數後，枚舉相鄰字元對即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def findValidPair(self, s: str) -> str:
        d = Counter(s)
        for a, b in pairwise(s):
            if a != b and d[a] == int(a) and d[b] == int(b):
                return a+b
                
        return ""
```
