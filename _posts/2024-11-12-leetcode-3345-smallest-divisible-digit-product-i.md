---
layout      : single
title       : LeetCode 3345. Smallest Divisible Digit Product I
tags        : LeetCode Easy Simulation
---
biweekly contest 143。  
題目簡潔，而且例題很良心，給個讚。  

## 題目

輸入兩個整數 n 和 t。  
求大於等於 n，且**各數位乘積**可被 t 整除的**最小**數字。  

## 解法

例如 n = 123，乘積就是 1\*2\*3 = 6。  
看能不能被 t 整除，不能就繼續找 n+1。  

範例一告訴我們只要整數中包含 0，就肯定能被 t 整除，因此最多找到 n+9 就可以停止。  
每次算乘積需要 O(log n)，至多 9 次視為常數。  

時間複雜度 O(log n)。  
空間複雜度 O(1)。  

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for x in count(n):
            rem = x
            prod = 1
            while rem > 0:
                prod *= rem % 10
                rem //= 10
            if prod % t == 0:
                return x

        return -1
```

python 內建函數寫法。  

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for x in count(n):
            prod = reduce(mul, map(int, str(x)))
            if prod % t == 0:
                return x

        return -1
```

很難看的一行版本。  

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        return next(x for x in count(n) if reduce(mul, map(int, str(x))) % t == 0)  
```
