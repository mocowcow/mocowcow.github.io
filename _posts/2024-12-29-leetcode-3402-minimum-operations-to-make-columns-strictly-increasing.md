---
layout      : single
title       : LeetCode 3402. Minimum Operations to Make Columns Strictly Increasing
tags        : LeetCode Easy Simulation Greedy
---
weekly contest 430。

## 題目

輸入 m x n 的非負整數矩陣。  

每次操作，你可以將任意 grid[i][j] 的值加 1。  

求使得每直行**嚴格遞增**所需的***最少***操作次數。  

## 解法

按照題意模擬。  
只要沒比前一個數 pre 大，就改成 pre + 1。  

時間複雜度 O(MN)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        ans = 0
        for c in range(N):
            pre = -inf
            for r in range(M):
                x = grid[r][c]
                if x > pre:
                    pre = x
                else:
                    pre += 1
                    ans += pre - x

        return ans

```

反正 grid[r][c] = x 的新值不是 x 就是 pre + 1。  
直接兩者取最大值也可以。  

```python
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        ans = 0
        for c in range(N):
            pre = -inf
            for r in range(M):
                x = grid[r][c]
                pre = max(pre+1, x)
                ans += pre - x

        return ans
```
