---
layout      : single
title       : LeetCode 200. Number of Islands
tags 		: LeetCode Medium DFS Matrix
---
Study Plan - Graph Theory - Day 1 - Matrix Related Problems。  

# 題目
輸入二維陣列grid，其中'0'代表水域，'1'代表陸地，求有多少個島嶼。  
一個或多個'1'水平或是垂直相鄰，算做同一個島嶼。且grid四周範圍外也算是水域。

# 解法
寫一個dfs(r,c)函數，若(r,c)為陸地則砍掉，然後向四周檢查，進而砍掉整個島。  
維護一個變數cnt，對所有格子檢查是否為陸地，若是則cnt+1，然後用dfs把小島砍掉。

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < M and 0 <= c < N) or grid[r][c] != '1':
                return
            grid[r][c] = '#'
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                dfs(nr, nc)

        cnt = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)

        return cnt
```
