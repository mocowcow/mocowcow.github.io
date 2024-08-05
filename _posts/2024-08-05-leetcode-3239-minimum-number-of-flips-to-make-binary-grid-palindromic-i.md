---
layout      : single
title       : LeetCode 3239. Minimum Number of Flips to Make Binary Grid Palindromic I
tags        : LeetCode Medium Simulation
---
biweekly contest 136。  

## 題目

輸入 m \* n 的二進位矩陣 grid。  

你可以將矩陣中任意格子的 0 翻轉成 1，或是 0 翻轉成 1。  

求**最少**需要翻轉幾次，才能使得矩陣中所有列**或**所有行都回文。  

## 解法

回文指的是正反向閱讀的順序都相同，每個元素都會**對稱**到另一個元素。  
對應到的元素對不同則需要翻面，至於翻哪個則不重要。  

暴力模擬，分別枚舉以行列為基準的回文需要多少次翻面。  

```python
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        # row palindromic
        row_diff = 0
        for r in range(M):
            for c in range(N // 2):
                if grid[r][c] != grid[r][N-1-c]:
                    row_diff += 1

        # col palindromic
        col_diff = 0
        for c in range(N):
            for r in range(M // 2):
                if grid[r][c] != grid[M-1-r][c]:
                    col_diff += 1

        return min(row_diff, col_diff)
```
