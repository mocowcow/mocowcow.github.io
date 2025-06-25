---
layout      : single
title       : LeetCode 3591. Check if Any Element Has Prime Frequency
tags        : LeetCode Easy Math
---
weekly contest 455。

## 題目

<https://leetcode.com/problems/check-if-any-element-has-prime-frequency/description/>

## 解法

按照題意模擬。會判斷質數就行。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
MX = 100
sieve = [True] * (MX + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(MX ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, MX + 1, i):
            sieve[j] = False


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        d = Counter(nums)
        return any(sieve[v] for v in d.values())
```
