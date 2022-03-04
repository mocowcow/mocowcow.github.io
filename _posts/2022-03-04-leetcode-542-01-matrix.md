---
layout      : single
title       : LeetCode 542. 01 Matrix
tags 		: LeetCode LeetCode Medium Matrix BFS
---
Study Plan - Graph Theory。  

# 題目
矩陣mat，只會出現1和0，計算每格距離最近的0多遠。  

# 解法
建立相同矩陣ans紀錄最小距離，初始值設為無限大。從每個開始0元素做BFS，初始距離為1，每移動一格距離+1，並順便更新最小距離。

```python
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        ans = [[math.inf]*N for _ in range(M)]
        q = []
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    q.append((i, j))
        dist = 0
        while q:
            t = []
            for r, c in q:
                if not (0 <= r < M and 0 <= c < N) or ans[r][c] <= dist:
                    continue
                ans[r][c] = dist
                t.append((r+1, c))
                t.append((r-1, c))
                t.append((r, c+1))
                t.append((r, c-1))
            dist += 1
            q = t

        return ans
```
