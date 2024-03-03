---
layout      : single
title       : LeetCode 3070. Count Submatrices with Top-Left Element and Sum Less Than k
tags        : LeetCode Medium Array Matrix PrefixSum
---
周賽387。

## 題目

輸入整數矩陣 matrix 和整數 k。  

求包含 grid 左上角元素的子矩陣中，有**幾個**子矩陣的總和小於等於 k。  

## 解法

若要包含 grid 的左上角元素，則子矩陣的左上角座標必為 (0, 0)。  
依照由左到右、由上到下的方向枚舉子矩陣的右下角，其實就是**二維前綴和**。  
相似題 [304. range sum query 2d   immutable]({% post_url 2022-03-25-leetcode-304-range-sum-query-2d---immutable %})。  

矩陣中不包含負數，因此若某右下角座標為 (r, c) 子矩陣，其總和超過 k，則 (r+1, c) 和 (r, c+1) 必定也不合法。  
此作為一個小小的加速點，可以剪枝節省時間。  

```python
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        ps = [[0] * (N + 1) for _ in range(M + 1)]
        ans = 0
        for r in range(M):
            for c in range(N):
                ps[r+1][c+1] = ps[r+1][c] + ps[r][c+1] - ps[r][c] + grid[r][c]
                if ps[r+1][c+1] <= k:
                    ans += 1
                    
        return ans
```
