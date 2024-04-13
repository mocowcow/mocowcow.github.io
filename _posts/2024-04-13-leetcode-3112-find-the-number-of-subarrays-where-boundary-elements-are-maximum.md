---
layout      : single
title       : LeetCode 3112. Find the Number of Subarrays Where Boundary Elements Are Maximum
tags        : LeetCode Medium Array Sorting Greedy
---
雙周賽 128。範例非常有良心，甚至還給出 w = 0 時的情況。  

## 題目

輸入二維整數陣列 points，其中 points[i] = [x<sub>i</sub>, y<sub>i</sub>]。另外還有整數 w。  
你的目標是用數個長方形蓋住所有點。  

每個長方形的左下角座標為 (x1, 0)、右上角座標為 (x2, y2)，其中 x1 <= x2, y2 >= 0，且 x2 - x1 <= w。  
如果一個點位於長方形的範圍內，或是其邊界上，都視作被覆蓋。  

求最少需要幾個長方形才能覆蓋所有點。  

注意：一個點可以被多個長方形覆蓋。  

## 解法

題目只有限定長方形的最多為 w，但高度不限。相當於可以忽視 y 座標。  
長方形寬度越寬，可能覆蓋的點越多。為了使用盡可能少的長方形，所以每個其寬度都設為最大值 w。  

看看範例附圖，很明顯發現，如果位於 xi 的點沒有被覆蓋，則以 xi 為左邊界放置長方形。  
如此一來，位於區間 [xi, xi + w] 內的所有點都可以被覆蓋到。  

首先將 points 以 x 軸遞增排序。  
維護覆蓋範圍的右邊界 last，並由左到右遍歷所有點的 x 座標。如果 x 超出覆蓋範圍 last，則答案加 1，並放置新的長方形，更新右邊界 last。  

時間複雜度 O(N log N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        ans = 0
        last = -inf
        for x, _ in points:
            if x > last:
                ans += 1
                last = x + w 
                
        return ans
```
