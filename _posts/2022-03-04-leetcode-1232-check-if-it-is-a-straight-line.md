---
layout      : single
title       : LeetCode 1232. Check If It Is a Straight Line
tags 		: LeetCode Easy Array Stack MonotonicStack HashTable
---
Study Plan - Programming Skills。  
小小抒發一下，討論區的解答清一色都是同時檢查三點斜率的公式： 
> (y - y1) / (x - x1) = (y1 - y0) / (x1 - x0)  

這種東西，真的這麼多人第一時間會推導出這種東西嗎？

# 題目
二維陣列coordinates，coordinates[i]代表點座標(x,y)，檢查是否所有點在同一條直線上。

# 解法
若為一直線的話，任意兩點的斜率應該都會是相同的。  
先以第一、二點的斜率slope定為標準，確定其他的點之間斜率是否一致。若有不一致則回傳false；順利檢查完回傳true。  

```python
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        def slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return (y2-y1)/(x2-x1) if x2 != x1 else math.inf

        sl = slope(coordinates[0], coordinates[1])
        for p in coordinates[2:]:
            if slope(coordinates[0], p) != sl:
                return False

        return True

```
