---
layout      : single
title       : LeetCode 3461. Check If Digits Are Equal in String After Operations I
tags        : LeetCode Easy Simulation
---
weekly contest 438。

## 題目

<https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/>

## 解法

轉成整數陣列後暴力模擬，不斷合併直到長度剩下 2 為止。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        a = [int(x) for x in s]
        while len(a) > 2:
            a = [(x + y) % 10 for x, y in pairwise(a)]

        return a[0] == a[1]
```
