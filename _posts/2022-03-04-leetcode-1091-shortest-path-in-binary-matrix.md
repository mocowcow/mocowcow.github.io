---
layout      : single
title       : LeetCode 1091. Shortest Path in Binary Matrix
tags 		: LeetCode Medium Matrix BFS
---
Study Plan - Graph Theory。  

# 題目
矩陣grid，只會出現1和0，1代表障礙，而0代表可以移動的路線。  
從最左上方出發，每次可以移動到當前周圍的8個位置，求移動到最右下角需要多少步數。

# 解法
從q=[(0,0)]開始做BFS，把八方都加入佇列q之後把當前值改成1防止重複計算，成功到達則回傳step，否則最後回傳-1。

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        q = [(0, 0)]
        step = 0
        while q:
            step += 1
            t = []
            for r, c in q:
                if not (0 <= r < M and 0 <= c < N) or grid[r][c] != 0:
                    continue
                if r == M-1 and c == N-1:
                    return step
                grid[r][c] = 1
                t.append((r+1, c))
                t.append((r-1, c))
                t.append((r, c+1))
                t.append((r, c-1))
                t.append((r+1, c+1))
                t.append((r-1, c-1))
                t.append((r-1, c+1))
                t.append((r+1, c-1))
            q = t

        return -1
```
