---
layout      : single
title       : LeetCode 3122. Minimum Number of Operations to Satisfy Conditions
tags        : LeetCode Medium Array DP
---
周賽 394。

## 題目

輸入 m \* n 的二維整數陣列 matrix。  
每次操作，你可以將任意格子的值改成任意**非負整數**。  
你必須透過數次操作，使得每個格子 grid[i][j] 滿足：  

- 若下方有格子，則兩者的值必須相等，即 grid[i][j] == grid[i + 1][j]  
- 若右方有格子，則兩者的值不相等，即 grid[i][j] != grid[i][j + 1]  

求**最少**需要幾次操作。  

## 解法

總而言之就是整行的值都相同，且相鄰兩行的值不同。  
但不知道要改成什麼值比較好，因此考慮 dp。  

定義 dp(col, prev)：第 col 行不可選擇 prev 的前提下，使得第 [col, N - 1] 行滿足限制的最小操作次數。  
轉移： max( cost + dp(col + 1, t) FOR ALL t != prev )，其中 cost = 該行不等於 t 的數量。  
base：當 col = N 時，不需要繼續操作，回傳 0。  

題目保證格子中的初始值為 [0, 9] 之間的數字，因此修改的新值也只考慮同樣的區間。  
而第一行隨便選什麼值都可以，因此答案入口為 dp(0, -1)。  

時間複雜度 O(MN + NK^2)，其中 K = 10。  
空間複雜度 O(NK)。  

```python
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        col_freq = [[0] * 10 for _ in range(N)]
        for j in range(N):
            for i in range(M):
                col_freq[j][grid[i][j]] += 1
        
        @cache
        def dp(col, prev):
            if col == N:
                return 0
            res = inf
            for t in range(10):
                if t == prev:
                    continue
                cost = M - col_freq[col][t]
                res = min(res, cost + dp(col + 1, t))
            return res
        
        return dp(0, -1)
```
