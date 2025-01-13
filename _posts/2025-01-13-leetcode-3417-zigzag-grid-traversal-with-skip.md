---
layout      : single
title       : LeetCode 3417. Zigzag Grid Traversal With Skip
tags        : LeetCode Easy Simulation
---
weekly contest 432。

## 題目

輸入 m x n 的二維矩陣 grid。  

你的任務是以 Z 字形遍歷 grid，並且跳過每個**交替**的格子。  
Z 字形遍歷指的是：  

- 從左上角格子 (0, 0) 出發。  
- 往右走直到盡頭。  
- 往下走到下一列，然後向左走到盡頭。  
- 每換一列就改變一次方向，直到全部遍歷完。  

回傳陣列 result，並按**順序**紀錄遍歷到的格子值。  

## 解法

維護一個變數 skip = 0/1，每次移動跟著交替，在 1 的時候跳過。  

至於 Z 字形可以判斷列號，偶數列號正序、奇數列號就倒序。  
更簡單的方式是在奇數列號的時候直接將整列**反轉**。  

時間複雜度 O(MN)。  
空間複雜度 O(1)。  

```python
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ans = []
        skip = 0
        for i, row in enumerate(grid):
            if i % 2 == 1:
                row.reverse()

            for x in row:
                if skip == 0:
                    ans.append(x)
                skip ^= 1

        return ans
```
