---
layout      : single
title       : LeetCode 3212. Count Submatrices With Equal Frequency of X and Y
tags        : LeetCode Medium Array Matrix PrefixSum
---
周賽 405。

## 題目

輸入二維矩陣 grid，其中 grid[i][j] 只可能是 'X', 'Y' 或 '.'。  
求有多少子矩陣滿足：  

- 包含 grid[0][0]
- 'X' 和 'Y' 的出現頻率相同  
- 包含至少一個 'X'  

## 解法

幾乎也是裸題，維護兩個二維前綴和，分別統計 X 和 Y 的頻率即可。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        ps_x = PrefixSum2D(grid, "X")
        ps_y = PrefixSum2D(grid, "Y")
        ans = 0
        for r in range(M):
            for c in range(N):
                x = ps_x.range_sum(0, 0, r, c)
                y = ps_y.range_sum(0, 0, r, c)
                if x > 0 and x == y:
                    ans += 1
                    
        return ans


class PrefixSum2D:

    def __init__(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        ps = self.ps = [[0]*(N+1) for _ in range(M+1)]
        for r in range(M):
            for c in range(N):
                ps[r+1][c+1] = \
                    ps[r][c+1] + ps[r+1][c] - \
                    ps[r][c] + int(matrix[r][c] == target)

    def range_sum(self, r1, c1, r2, c2):
        ps = self.ps
        return ps[r2+1][c2+1] - ps[r2+1][c1] - ps[r1][c2+1] + ps[r1][c1]
```
