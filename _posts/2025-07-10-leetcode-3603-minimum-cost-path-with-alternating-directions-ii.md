---
layout      : single
title       : LeetCode 3603. Minimum Cost Path with Alternating Directions II
tags        : LeetCode Medium DP
---
biweekly contest 160。

## 題目

<https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/description/>

## 解法

移動只能往右或下，每次移動後範圍都會縮小。  
不同的移動方式可能得到相同的範圍，有**重疊的子問題**，考慮 dp。  

除了座標以外，還受到時間的奇偶性影響。  
狀態 parity=0/1 代表當前時間的奇偶性。  

定義 dp(i,j,parity)：當前時間為 parity，從 (i, j) 走到終點的最小時間。  

出發時間為第 1 秒，答案入口 dp(0, 0, 1)。  
答案記得加上出發時間的 1。  

時間複雜度 O(mn)。  
空間複雜度 O(mn)。  

```python
class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:

        def move_cost(i, j):
            return (i+1) * (j+1)

        @cache
        def dp(i, j, parity):
            if i == m-1 and j == n-1:
                return 0

            # wait
            if parity == 0:
                return dp(i, j, 1) + waitCost[i][j]

            res = inf
            # down
            if i+1 < m:
                res = dp(i+1, j, 0) + move_cost(i+1, j)

            # right
            if j+1 < n:
                res = min(res, dp(i, j+1, 0) + move_cost(i, j+1))
            return res

        return dp(0, 0, 1) + 1
```
