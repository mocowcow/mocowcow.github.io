---
layout      : single
title       : LeetCode 3442. Maximum Difference Between Even and Odd Frequency I
tags        : LeetCode Easy Simulation
---
weekly contest 435。  
滿無言的題目，總 WA 佔了總提交一半。  

## 題目

<https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/>

## 解法

注意：標題寫 even 和 odd，但內文要求的是 odd - even 的最大值。  

統計字元頻率，求**奇數最大值**扣掉**偶數最小值**，相減即可。  
題目保證奇偶頻率至少都會出現一次，不必特判例外。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxDifference(self, s: str) -> int:
        odd_mx = -inf
        even_mn = inf
        for v in Counter(s).values():
            if v % 2 == 1:
                odd_mx = max(odd_mx, v)
            else:
                even_mn = min(even_mn, v)

        return odd_mx - even_mn
```
