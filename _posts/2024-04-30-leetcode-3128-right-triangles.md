---
layout      : single
title       : LeetCode 3128. Right Triangles
tags        : LeetCode Medium Array Matrix
---
雙周賽 129。

## 題目

輸入二維整數陣列 grid。  

求 grid 中，可以使用三個值為 1 的元素組成的**直角三角形**個數。  

注意：若三個元素滿足：兩個元素在**同一行**，且和第三個元素在**同一列**，則稱為直角三角形。  
三個元素之間不需要相鄰。  

## 解法

令**直角**做為三個元素的中心點 (r, c)，第二個元素必須在 r 列，第三個元素在 c 行。  
假設 r 列上有 a 個元素，且 c 行上有 b 個元素。根據**乘法原理**，直角 (r, c) 共可產生 (a - 1) \* (b - 1) 個三角形。  

先遍歷一次 grid，統計各行列的元素個數。  
再次遍歷，枚舉中心點計算三角形數量，並加入答案。  

時間複雜度 O(mn)。  
空間複雜度 O(m + n)。  

```python
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        col = [0] * N
        row = [0] * M
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    col[c] += 1
                    row[r] += 1
                    
        ans = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    ans += (row[r] - 1) * (col[c] - 1)
                    
        return ans
```
