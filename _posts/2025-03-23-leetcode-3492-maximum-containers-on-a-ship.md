---
layout      : single
title       : LeetCode 3492. Maximum Containers on a Ship
tags        : LeetCode Easy
---
weekly contes 442。  
大概是最近最簡單的 Q1。

## 題目

<https://leetcode.com/problems/maximum-containers-on-a-ship/description/>

## 解法

有 n \* n 的格子，每格可以放重量 w 的東西，總重量不得超過 maxWeight。  
要就是全放滿，不然就是 maxWeight / w。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n * n, maxWeight // w)
```
