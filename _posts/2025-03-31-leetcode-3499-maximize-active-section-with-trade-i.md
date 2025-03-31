---
layout      : single
title       : LeetCode 3499. Maximize Active Section with Trade I
tags        : LeetCode Medium Greedy
---
biweekly contest 153。

## 題目

<https://leetcode.com/problems/maximize-active-section-with-trade-i/description/>

## 解法

題目有點繞。  
最後一段說明可以理解成所有連續的 0 的旁邊都有 1，不必考慮邊界。  

反正操作分兩步驟：  

1. 先找某個 011..110 把中間連續 1 的改成 0，整串都變成 0  
2. 然後把這串連續的 0 整串變 1  

這操作相當於把兩段相鄰的 0 都變 1。例如：  
> ..001100..
> 第一步驟變 ..000000..  
> 第二步驟變 ..111111..  

先把所有連續的 0 長度找出來，以相鄰的兩個大小和更新最大值。  
注意：答案問的是 1 的總數，所以還要加上原本就有的 1 數量。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        N = len(s)
        a = []
        i = 0
        while i < N:
            j = i
            while j+1 < N and s[i] == s[j+1]:
                j += 1

            if s[i] == "0":
                a.append(j-i+1)
            i = j + 1

        ans = 0
        for x, y in pairwise(a):
            ans = max(ans, x + y)

        return s.count("1") + ans
```
