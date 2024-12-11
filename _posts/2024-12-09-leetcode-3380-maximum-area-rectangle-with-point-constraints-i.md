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

![示意圖](/3308-1/img/xxxxxx.jpg)

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

最最最暴力的做法，且跟座標值域無關。  

直接枚舉四個點，看否正好湊成矩形。  
若湊成，再掃一次全點，看哪些在矩形內。正好四個就更新答案。  

時間複雜度 O(N^5)。  
空間複雜度 O(1)。  

老實說我寫起來非常不舒服，光是變數命名就快吐了，一堆嵌套甚至要把 if 換行。  
很配服能快速寫出來的人。  

```python
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        N = len(points)
        ans = 0
        # enumerate 4 vertices
        # x1y2 x2y2
        # x1y1 x2y1
        for ll in points: # lower left
            for ur in points:# upper right
                for ul in points: # upper left
                    for lr in points: # lower right
                        if ll[0] == ul[0] and ll[1] == lr[1] \
                        and ur[0] == lr[0] and ur[1] == ul[1]:
                            # count points inside
                            x1, y1 = ll
                            x2, y2 = ur
                            cnt = 0
                            for x, y in points:
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    cnt += 1
                            # update answer if only 4 points
                            if cnt == 4:
                                w = x2-x1
                                h = y2-y1
                                ans = max(ans, w*h)

        if ans == 0:
            return -1

        return ans
```

前面四層寫成這樣，照圖施工或許比較方便。  

```python
# x3y3 x2y2
# x1y1 x4y4
for x1, y1 in points: # lower left
    for x2, y2 in points:# upper right
        for x3, y3 in points: # upper left
            for x4, y4 in points: # lower right
```

另一種比較不暴力的方式，同樣和值域無關。  

枚舉兩個點作為對角線 (可能是斜線或反斜線)，並推出相對的兩個點。  
然後掃一次全點，只統計頂點數。要是某點不在矩形外、也不是頂點，那就不合法。  

時間複雜度 O(N^3)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        N = len(points)
        ans = 0
        for p1 in points:
            for p2 in points:
                x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
                y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
                cnt = 0 # count only vertices
                for x, y in points:
                    # outside
                    if x < x1 or x > x2 or y < y1 or y > y2: 
                        continue
                    # vertex
                    if x in [x1, x2] and y in [y1, y2]:
                        cnt += 1
                    # inside but not vertex
                    else:
                        cnt = inf

                # update answer if only 4 vertices
                if cnt == 4:
                    w = x2-x1
                    h = y2-y1
                    ans = max(ans, w*h)

        if ans == 0:
            return -1

        return ans
```
