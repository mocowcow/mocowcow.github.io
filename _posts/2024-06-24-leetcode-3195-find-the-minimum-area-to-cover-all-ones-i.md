---
layout      : single
title       : LeetCode 3195. Find the Minimum Area to Cover All Ones I
tags        : LeetCode Medium Array Matrix Greedy
---
周賽 403。

## 題目

輸入二維二進位陣列 grid。  
找出一個可以包含矩陣中所有 1 的矩形範圍，且具有最小的面積。  

求矩形的**最小**可能面積。  

## 解法

若矩陣中某個位置 grid[r][c] 是 1，他必須要被矩形包含。  
所以矩形的上邊界 up 必須小於等於 r、下邊界必須大於 r；  
同理，左邊界必須小於等於 c、右邊界必須大於等於 c。  

遍歷矩陣所有元素，若 grid[r][c] 為 1 則按照此方式更新邊界極值。  
最後矩形寬度 w = right - left + 1、高度 h = down - up + 1，答案為 w * h。  

時間複雜度 O(MN)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        up = inf
        down = -inf
        left = inf
        right = -inf

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    up = min(up, r)
                    down = max(down, r)
                    left = min(left, c)
                    right = max(right, c)

        w = right - left + 1
        h = down - up + 1

        return w * h
```
