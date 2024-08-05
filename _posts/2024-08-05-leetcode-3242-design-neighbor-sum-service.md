---
layout      : single
title       : LeetCode 3242. Design Neighbor Sum Service
tags        : LeetCode Easy Simulation
---
weekly contest 409。  
好久沒看到設計題。  

## 題目

輸入 n \* n 的矩陣 grid，由 [0, n<sup>2</sup>-1] 之間的**不重複**元素組成。  

實作類別 neighborSum：

- neighborSum(int [][]grid)，建構子初始化。  
- int adjacentSum(int value)，回傳 grid 中與 value 相鄰的元素和。  
    相鄰指的是 value 上、下、左、右的元素  
- int diagonalSum(int value)，回傳 grid 中與 value 對角線相鄰的元素和。  
    對角線相鄰指的是 value 左上、左下、右上、右下的元素  

## 解法

模擬題。  
以 Q1 來說行數需求偏高，最容易錯的點是打錯字。  

注意**相鄰**與**對角線相鄰**的邏輯幾乎相同，只差在枚舉的格子方位。  
因此可以將共通邏輯提出，減少行數、降低出錯機會。  

```python
class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.a = grid
        self.N = len(grid)
        self.pos = [None] * (self.N * self.N)
        for r in range(self.N):
            for c in range(self.N):
                self.pos[grid[r][c]] = [r, c]

    def adjacentSum(self, value: int) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        return self.sum_neighbors(value, dirs)

    def diagonalSum(self, value: int) -> int:
        dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        return self.sum_neighbors(value, dirs)

    def sum_neighbors(self, value, dirs):
        r, c = self.pos[value]
        res = 0
        for dx, dy in dirs:
            rr, cc = r+dx, c+dy
            if 0 <= rr < self.N and 0 <= cc < self.N:
                res += self.a[rr][cc]
        return res
```
