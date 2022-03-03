---
layout      : single
title       : LeetCode 417. Pacific Atlantic Water Flow
tags 		: LeetCode Medium Matrix DFS
---
Study Plan - Graph Theory。  

# 題目
矩陣heights，其中整數代表高度。上方及左方為太平洋，下方及右方為大西洋。  
假設降雨時，雨水可以從高處流入低處，求那些位置的水同時可以流入兩個海洋。  

# 解法
抽換概念，試想兩邊海洋的水只能逆勢往上爬，看可以爬到哪裡。  
布林矩陣at和pa表示兩海洋可以爬到哪，並對第一列和第一行做太平洋dfs，最後列和最後行做大西洋dfs。最後把可以同時流入兩洋的位置加入答案。

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        at = [[False]*N for _ in range(M)]
        pa = [[False]*N for _ in range(M)]

        def dfs(r, c, h, ocean):
            if not (0 <= r < M and 0 <= c < N) or ocean[r][c]:
                return
            if heights[r][c] < h:
                return
            ocean[r][c] = True
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                dfs(nr, nc, heights[r][c], ocean)

        for r in range(M):
            dfs(r, 0, 0, pa)
            dfs(r, N-1, 0, at)
        for c in range(N):
            dfs(0, c, 0, pa)
            dfs(M-1, c, 0, at)

        ans = []
        for r in range(M):
            for c in range(N):
                if pa[r][c] and at[r][c]:
                    ans.append((r, c))

        return ans
```
