---
layout      : single
title       : LeetCode 3178. Find the Child Who Has the Ball After K Seconds
tags        : LeetCode Easy Array Simulation
---
周賽 401。

## 題目

輸入兩個正整數 n 和 k。  
有 n 個小孩編號分別從 0 到 n - 1，從左到右排成一列。  

最初，小孩 0 持有球並準備向右傳。每一秒鐘，持球的小孩會傳給下一個人。  
每當傳到最邊邊的小孩時，他們會改變傳球方向。  

求 k 秒後持球的小孩編號。  

## 解法

按照題目模擬，維護變數 curr 代表當前小孩，以及 x 代表移動方向。  

時間複雜度 O(k)。  
空間複雜度 O(n)。  

```python
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        x = 1
        curr = 0
        for _ in range(k):
            curr += x
            if curr == 0 or curr == n - 1:
                x = -x
                
        return curr
```
