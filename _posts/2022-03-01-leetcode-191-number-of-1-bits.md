---
layout      : single
title       : LeetCode 191. Number of 1 Bits
tags 		: LeetCode Easy BitManipulation
---
Study Plan - Programming Skills Day 2 Operator。  
剛好跟今天的每日題呼應，真巧。

# 題目
輸入一個整數，求以二進位表示有多少個位元1。

# 解法
維護變數cnt，當n>0時將cnt加上n&1，並將n/2。最後cnt就是答案。

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n & 1
            n >>= 1

        return cnt

```
