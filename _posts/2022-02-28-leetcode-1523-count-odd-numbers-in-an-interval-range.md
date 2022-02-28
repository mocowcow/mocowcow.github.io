---
layout      : single
title       : LeetCode 1523. Count Odd Numbers in an Interval Range
tags 		: LeetCode Easy Math
---
Study Plan - Programming Skills Day 1 Basic Data Type。  
奇怪的數學題。

# 題目
輸入兩個整數low和high，求low~high共有多少奇數(包含low和high)。

# 解法
high最大竟然到10^9，感覺連O(N)都會炸掉，八成是要公式解。  
先算0\~high有多少質數，再扣掉0\~low有多少質數就是答案。

```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2-low//2

```
