---
layout      : single
title       : LeetCode 1254. Number of Closed Islands
tags 		: LeetCode Medium DFS Matrix
---
Study Plan - Graph Theory。  

# 題目
輸入矩陣grid，其中1代表水域，0代表陸地，求四周被水包圍的小島數量。  
接觸到邊界的陸地則不算是被水包圍。  
一個或多個1水平或是垂直相鄰，算做同一個島嶼。且grid四周範圍外也算是水域。

# 解法
注意這題的陸地0，水是1。  
既然邊界不算是水，那就換個方向思考，和邊界上有接觸的陸地一定不符合要求。先把四周邊框的陸地用dfs塗掉，之後就是普通的小島計數了。

```python
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < M and 0 <= c < N) or grid[r][c] != 0:
                return 0
            grid[r][c] = 1
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                dfs(nr, nc)
        
        for i in range(M):
            for j in range(N):
                if i == 0 or j == 0 or i == M-1 or j == N-1:
                    dfs(i, j)

        cnt = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    cnt += 1
                    dfs(i, j)

        return cnt
```
