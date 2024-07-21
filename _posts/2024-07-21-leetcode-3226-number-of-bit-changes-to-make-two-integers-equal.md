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
空間複雜度 O(1)。  

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

注意到 1 變 0 這個操作其實就是**位元 AND** 運算。  
直接拿 n 和 k 做 AND，就是 n 消掉不該有的位元之後的結果，若不等同於 k 則代表不合法。  

若合法，則需要找出有幾個位元不同。  
利用 XOR 找出不同的位元，最後統計有幾個 1 即可。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n & k != k:
            return -1
            
        diff = n ^ k
        return diff.bit_count()
```
