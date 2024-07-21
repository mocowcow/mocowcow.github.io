---
layout      : single
title       : LeetCode 3226. Number of Bit Changes to Make Two Integers Equal
tags        : LeetCode Easy Simulation BitManipulation
---
weekly contest 407。  

## 題目

輸入正整數 n 和 k。  

在 n 的**二進位表示**中，你可以選擇**任意**的 1 位元，將其變成 0。  

求需要改變幾次才能使得 n 等於 k。若不可能，則回傳 -1。  

## 解法

只能將 1 變成 0，如果 n 的位元是 0、且 k 的位元是 1，則不可能達成。  
否則不同的位元個數就是答案。  

時間複雜度 O(log n)。  
空間複雜度 O(log n)。  

```python
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        for i in range(30):
            bn = (n >> i) & 1
            bk = (k >> i) & 1
            if bn == 0 and bk == 1:
                return -1
            if bn != bk:
                ans += 1

        return ans
```
