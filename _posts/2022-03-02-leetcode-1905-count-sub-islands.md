---
layout      : single
title       : LeetCode 1905. Count Sub Islands
tags 		: LeetCode Medium Matrix DFS
---
Study Plan - Graph Theory。  
原來接下來三天一樣都是矩陣題，尷尬萬分。

# 題目
矩陣grid1和grid2，其中1表示陸地，0表示海洋，連在一起的陸地算是一塊島。  
若grid2的某塊島剛好也在grid1所有相同格子出現，則認為這塊地是一個子島。求grid2中有多少子島。

# 解法
先把用dfs把grid2的每座島分布記下來，加入subs中，然後對每個子島sub檢查其中的所有座標在grid1中都要是陸地，若是則代表是子島，計數+1。

```python
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        M, N = len(grid1), len(grid2[0])
        subs = []

        def dfs(r, c, sub):
            if not (0 <= r < M and 0 <= c < N) or grid2[r][c] != 1:
                return
            sub.append((r, c))
            grid2[r][c] = 0
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                dfs(nr, nc, sub)

        for i in range(M):
            for j in range(N):
                if grid2[i][j]:
                    sub = []
                    dfs(i, j, sub)
                    subs.append(sub)

        return sum(all(grid1[x][y] == 1 for x, y in sub) for sub in subs)
```
