---
layout      : single
title       : LeetCode 3142. Check if Grid Satisfies Conditions
tags        : LeetCode Easy Array Matrix Simulation
---
雙周賽 130。

## 題目

輸入 m \* n 的正整數矩陣 grid。每個 grid[i][j] 必須滿足：  

- 如果下面有格子，則需**等於**下面的格子。也就是 grid[i][j] == grid[i + 1][j]  
- 如果右邊有格子，則需**不等於**右邊的格子。也就是 grid[i][j] != grid[i][j + 1]  

若所有格子都滿足條件則回傳 true，否則回傳 false。  

## 解法

按照題意模擬即可。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        for r in range(M):
            for c in range(N):
                if r + 1 < M: # check down
                    if grid[r][c] != grid[r + 1][c]:
                        return False
                if c + 1 < N: # check right
                    if grid[r][c] == grid[r][c + 1]:
                        return False
                
        return True
```
