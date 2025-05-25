---
layout      : single
title       : LeetCode 3556. Sum of Largest Prime Substrings
tags        : LeetCode Medium Math Simulation
---
biweekly contest 157。

## 題目

<https://leetcode.com/problems/sum-of-largest-prime-substrings/>

## 解法

暴力枚舉子陣列，判斷是否為質數。  
排序找前三大的質數即可。  

時間複雜度 O(N^2 \* sqrt(MX))，其中 MX =  10^10。  
空間複雜度 O(N^2)。  

```python
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        N = len(s)
        p = set()
        for i in range(N):
            x = 0
            for j in range(i, N):
                x = x*10 + int(s[j])
                if is_prime(x):
                    p.add(x)

        return sum(sorted(p)[-3:])


# check is prime or not
# O(sqrt(n))
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2
```
