---
layout      : single
title       : LeetCode 1162. As Far from Land as Possible
tags 		: LeetCode Medium Matrix BFS
---
Study Plan - Graph Theory。  
這題故意不讓人dfs，我不信邪，吃了三次TLE，服了。

# 題目
輸入矩陣grid，每上下左右移動一格算1距離，求最遠的0和1距離多少。  
若矩陣全是0或全是1則回傳-1。

# 解法
先把整個矩陣加起來，過濾特例，全為0總和是0，全為1總和是N*N。  
維護佇列q，集合vistied做bfs，把每個1四周的格子都加進來。  
如果超過矩陣範圍外或是或是(r,c)不為0，又或是已經處理過則略過，否則將四周格子也加入佇列。

```python
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if sum(sum(grid, [])) in [0, N**2]:
            return -1

        q = deque()
        dist = -1
        visited = set()

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    q.append((i+1, j))
                    q.append((i-1, j))
                    q.append((i, j+1))
                    q.append((i, j-1))

        while q:
            t = []
            for r, c in q:
                if not (0 <= r < N and 0 <= c < N) or grid[r][c] != 0 or (r, c) in visited:
                    continue
                visited.add((r, c))
                t.append((r+1, c))
                t.append((r-1, c))
                t.append((r, c+1))
                t.append((r, c-1))
            dist += 1
            q = t

        return dist
```

