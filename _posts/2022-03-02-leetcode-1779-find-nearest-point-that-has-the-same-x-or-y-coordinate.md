---
layout      : single
title       : LeetCode 1779. Find Nearest Point That Has the Same X or Y Coordinate
tags 		: LeetCode Easy Array
---
Study Plan - Programming Skills。

# 題目
二維陣列points代表座標(xi,yi)，求與(x,y)垂直或是水平的最短**曼哈頓距離**的點是幾號。若有數個點距離相同則以編號小的優先。  
曼哈頓距離公式為abs(x1-x2)+abs(y1-y2)。  

# 解法
照著描述做就可以了。

```python
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dis = math.inf
        ans = -1
        for i, (px, py) in enumerate(points):
            if x == px or y == py:
                manDis = abs(x-px)+abs(y-py)
                if manDis < dis:
                    dis = manDis
                    ans = i

        return ans
```
