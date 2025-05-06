---
layout      : single
title       : LeetCode 3536. Maximum Product of Two Digits
tags        : LeetCode Easy Simulation
---
weekly contest 448。

## 題目

<https://leetcode.com/problems/maximum-product-of-two-digits/description/>

## 解法

把 n 中的每個數位看做獨立數字，共有 O(log n) 個。  
求任選兩個的最大乘積。  

時間複雜度 O(log n \* log n)。  
空間複雜度 O(log n)。  

```python
class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10

        N = len(digits)
        ans = 0
        for i in range(N):
            for j in range(i+1, N):
               ans = max(ans, digits[i] * digits[j]) 

        return ans
```

其實只需要在拆分數字的時候維護最大值和次大值即可。  

時間複雜度 O(log n)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxProduct(self, n: int) -> int:
        mx1 = mx2 = 0
        while n > 0:
            n, r = divmod(n, 10)
            if r > mx1:
                mx2 = mx1
                mx1 = r
            elif r > mx2:
                mx2 = r

        return mx1 * mx2
```
