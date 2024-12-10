---
layout      : single
title       : LeetCode 3380. Maximum Area Rectangle With Point Constraints I
tags        : LeetCode Medium Geometry Simulation
---
weekly contest 427。  
這種算座標的題我真的有些障礙，雖然只打模擬賽，但還是寫到心態有點崩。  

## 題目

輸入整數陣列 points，其中 points[i] = [x<sub>i</sub>, y<sub>i</sub>] 代表無限平面上的一個座標點。  

你的目標是找到最大的矩形面積，滿足：  

- 四個頂點必須是陣列中的座標點。  
- 在矩形內部或是邊界上不可有其他點。  
- 矩形的邊與座標軸平行。  

回傳**最大面積**，若不存在則回傳 -1。  

## 解法

好險平面不大，點也不多，暴力模擬就行。  
不過暴力的方法很多種，而且都沒有好寫到哪裡去。  

---

我一開始的想法是枚舉所有的點作為左下角，分別往上、右找第一個碰到的點。  
如果都有找到，再算出右上角的座標，然後算整個面積裡面有多少點。  

後來才發現其實枚舉右上角，往左、往下找更順眼順手。  

枚舉 N 個點，每次找矩形需要 O(2\*MX) + O(MX^2)。  

時間複雜度 O(N \* MX^2)，其中 MX = 最大軸座標，此為 101。  
空間複雜度 O(MX^2)。  

```python
MX = 101
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        a = [[0] * MX for _ in range(MX)]
        for x, y in points:
            a[x][y] = 1
            
        ans = -inf
        for x2, y2 in points:
            x = x2-1
            y = y2-1
            while x >= 0 and a[x][y2] == 0:
                x -= 1
            while y >= 0 and a[x2][y] == 0:
                y -= 1
            if x >= 0 and y >= 0 and a[x][y] == 1:
                # count point in rectangle
                cnt = 0
                for i in range(x, x2+1):
                    for j in range(y, y2+1):
                        cnt += a[i][j]
                            
                # update answer if only 4 points
                if cnt == 4:
                    w = x2-x
                    h = y2-y
                    ans = max(ans, w*h)

        if ans == -inf:
            return -1

        return ans
```
