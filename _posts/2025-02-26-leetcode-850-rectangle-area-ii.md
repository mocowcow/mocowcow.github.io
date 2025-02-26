---
layout      : single
title       : LeetCode 850. Rectangle Area II
tags        : LeetCode Hard
---

以前只知道一種做法，原來有兩種更快的優化。  
趕緊來還債。  

## 題目

<https://leetcode.com/problems/rectangle-area-ii/description/>

## 解法

矩形至多 N = 200 個，但是座標值域卻高達 10^9。  
先找出可能出現的 x, y 軸座標，進行**離散化**，依序對應到 0\~ 2N-1 的值域。  

若去重後的 x 軸座標有 X 個，那麼其構成的區間線段會有 X-1 個；y 軸同理，有 Y-1 個線段。  
可視作 (X-1) \* (Y-1) 的矩陣 cover  

再次遍歷所有矩形，按照離散化後的座標，將對應到的部分標記覆蓋。  
最後再遍歷矩陣，若 cover[i][j] 已被覆蓋，則查詢原本對應的座標，將面積加入答案中。  

時間複雜度 O(N^3)。  
空間複雜度 O(N^2)。  

```python
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # collect coord
        xs = set()
        ys = set()
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
            ys.add(y1)
            ys.add(y2)

        # discretize
        xs = sorted(xs)
        ys = sorted(ys)
        mp_x = {x: i for i, x in enumerate(xs)}
        mp_y = {y: j for j, y in enumerate(ys)}

        # mark cover
        X = len(xs) - 1
        Y = len(ys) - 1
        cover = [[0] * Y for _ in range(X)]
        for x1, y1, x2, y2 in rectangles:
            for x in range(mp_x[x1], mp_x[x2]):
                for y in range(mp_y[y1], mp_y[y2]):
                    cover[x][y] = 1

        # calc cover area
        ans = 0
        for x in range(X):
            for y in range(Y):
                if cover[x][y]:
                    x_width = xs[x+1] - xs[x]
                    y_height = ys[y+1] - ys[y]
                    ans += x_width * y_height

        return ans % (10 ** 9 + 7)
```
