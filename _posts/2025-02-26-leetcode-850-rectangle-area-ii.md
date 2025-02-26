---
layout      : single
title       : LeetCode 850. Rectangle Area II
tags        : LeetCode Hard Matrix HashTable
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

想像 y 軸有一條**掃描線**，由下往上移動。  
每次移動，統計 x 軸有多少線段被覆蓋。  

對於矩形 x1, y1, x2, y2 來說，當掃描線掃到 y1 時，線段 [x1, x2] 從此時開始被覆蓋；  
掃到 y2 時，線段 [x1, x2] 的覆蓋結束。  

把每個矩形轉換成覆蓋開始 / 結束的事件，以 y 軸排序。  
每次 y 軸掃瞄線移動，增加的面積即：  
> y 軸差值 \* x 軸覆蓋長度  

我們只需要維護 x 軸被覆蓋的線段，所以只有 x 軸需要離散化。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # collect coord
        # and turn rect into event
        xs = set()
        ys = set()
        events = []
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
            events.append([y1, x1, x2, 1])
            events.append([y2, x1, x2, -1])

        # discretize
        xs = sorted(xs)
        mp_x = {x: i for i, x in enumerate(xs)}

        # mark cover
        X = len(xs) - 1
        cover = [0] * X 

        # sweep line
        events.sort()
        ans = 0
        for i, (y, x1, x2, val) in enumerate(events):
            if i > 0:
                pre_y = events[i-1][0]
                y_height = y - pre_y
                for j, cnt in enumerate(cover):
                    if cnt > 0:
                        x_width = xs[j+1] - xs[j]
                        ans += x_width * y_height

            for x in range(mp_x[x1], mp_x[x2]):
                cover[x] += val

        return ans % (10 ** 9 + 7)
```
