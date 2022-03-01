---
layout      : single
title       : LeetCode 733. Flood Fill
tags 		: LeetCode Easy DFS Matrix
---
Study Plan - Graph Theory - Day 1 - Matrix Related Problems。  

# 題目
輸入矩陣image，其中元素代表不同顏色。將(sr,sc)格子與相連的同色格子全部改成newColor。

# 解法
先確認原本的顏色oldColor，如果跟目標顏色相同就不用改了。  
dfs函數檢查(r,c)是否為oldColor，或是則改成newColor，再對四周dfs。

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        M, N = len(image), len(image[0])

        def dfs(r, c):
            if not (0 <= r < M and 0 <= c < N) or image[r][c] != oldColor:
                return
            image[r][c] = newColor
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                dfs(nr, nc)

        oldColor = image[sr][sc]
        if oldColor != newColor:
            dfs(sr, sc)

        return image
```
