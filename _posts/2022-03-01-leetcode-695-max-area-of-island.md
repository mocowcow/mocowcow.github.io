---
layout      : single
title       : LeetCode 695. Max Area of Island
tags 		: LeetCode Medium DFS Matrix
---
Study Plan - Graph Theory。  

# 題目
輸入矩陣grid，其中0代表水域，1代表陸地，求最大島嶼大小。  
一個或多個1水平或是垂直相鄰，算做同一個島嶼。且grid四周範圍外也算是水域。

# 解法
dfs稍微改一下，改成回傳陸地大小。  
若超出邊界或非陸地，回傳0；不然就是1加上四個方向的dfs。對每格都做dfs找最大值就是答案。

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < M and 0 <= c < N) or grid[r][c] != 1:
                return 0
            grid[r][c] = '#'
            area = 1
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                area += dfs(nr, nc)
            return area

        return max(dfs(r, c) for r in range(M) for c in range(N))
```
