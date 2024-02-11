---
layout      : single
title       : LeetCode 3033. Modify the Matrix
tags        : LeetCode Easy Array Matrix Simulation
---
周賽384。

## 題目

輸入 m\*n 的整數矩陣 matrix。  
並創建和 matrix 相等的矩陣 answer，然後將 answer 裡面的所有 -1 替換成該行中的**最大元素**。  

回傳矩陣 answer。  

## 解法

沒什麼好說，照著模擬就行，甚至可以原地修改。  

```python
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        
        for c in range(N):
            mx = -1
            for r in range(M):
                mx = max(mx, matrix[r][c])
            for r in range(M):
                if matrix[r][c] == -1:
                    matrix[r][c] = mx
                    
        return matrix
```
