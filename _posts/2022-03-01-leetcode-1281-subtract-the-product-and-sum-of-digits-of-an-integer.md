---
layout      : single
title       : LeetCode 1281. Subtract the Product and Sum of Digits of an Integer
tags 		: LeetCode Easy Math
---
Study Plan - Programming Skills Day 2 Operator。  
又是奇怪的算數題。

# 題目
輸入整數n，先把n的每個位數拆開來，求(位數全部相乘)-(位數全部相加)為多少。

# 解法
照著描述做就好，太懶得寫，直接內建函數解決。

```python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        d = [int(x) for x in str(n)]
        return reduce(operator.mul, d)-sum(d)

```
