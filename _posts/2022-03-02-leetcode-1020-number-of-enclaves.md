---
layout      : single
title       : LeetCode 1020. Number of Enclaves
tags 		: LeetCode Medium Matrix DFS
---
Study Plan - Graph Theory。  
這套題前面都是這種小島題，就算只要稍微改程式碼還是覺得有點無聊。   

# 題目
矩陣grid，其中1表示陸地，0表示海洋，連在一起的陸地算是同一塊地，求沒有連接到邊界的陸地面積。

# 解法
用dfs把連接到最外圈的陸地全部砍掉，之後再計算面積即可。

```python
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < M and 0 <= c < N) or grid[r][c] != 1:
                return
            grid[r][c] = 0
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                dfs(nr, nc)

        for i in range(M):
            for j in range(N):
                if i == 0 or j == 0 or i == M-1 or j == N-1:
                    dfs(i, j)

        cnt = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    cnt += 1
        return cnt
```
