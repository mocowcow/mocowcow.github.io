---
layout      : single
title       : LeetCode 3274. Check if Two Chessboard Squares Have the Same Color
tags        : LeetCode Easy
---
weekly contest 413。  

## 題目

輸入兩個整數字串 coordinate1, coordinate2，代表 8x8 棋盤中的兩個座標。  

若兩個座標的顏色相同則回傳 true，否則回傳 false。  

## 解法

座標的行列號加起來若是偶數則是黑色、奇數則是白色。  
判斷兩座標的奇偶性即可。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        
        def f(co):
            x = ord(co[0]) - ord('a')
            y = ord(co[1]) - ord('1')
            return (x + y) % 2

        return f(coordinate1) == f(coordinate2)
```
