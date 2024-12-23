---
layout      : single
title       : LeetCode 3394. Check if Grid can be Cut into Sections
tags        : LeetCode Medium Sorting Greedy
---
biweekly contest 146。

## 題目

輸入整數 n，代表 n x n 的網格，原點在左下角。  
輸入二維整數陣列，代表矩形的座標，其中 rectangles[i] = [start <sub>x</sub>, start <sub>y</sub>, end <sub>x</sub>, end <sub>y</sub>] 代表一個矩形：  

- (start <sub>x</sub>, start <sub>y</sub>) 是矩形的左下角座標。  
- (end <sub>x</sub>, end <sub>y</sub>) 是矩形的右上角座標。  

所有矩形都不重疊。  
你的目標是找到可能用兩刀水平**或**垂直分割，滿足：  

- 分割出的三個區塊，裡面各**至少**有一個矩形。  
- 每個矩形只屬於一個區塊 (不能切到矩形中間)。  

## 解法

只能選水平或垂直分割，其中一種方法合法就行。  

如果垂直切，只要保證切的 x 軸上沒有矩形經過；如果水平切，只要保證切的 y 軸上沒有矩形經過。  
兩種邏輯是共通的，可以轉化為一維的區間問題。  

---

題目描述沒講清楚能不能**切邊**，但看範例確定能切在相連的邊上：  
> [0,2] 和 [2,3] 兩個矩形，可以切在 2 上。  

先按照區間左端點排序，保證靠左的區間會先出現。  
第一個區間自成一個區塊，因此第一**區塊**的右端點 mx 至少等於其右端點。  

遍歷區間 s, e：  

- 若 s 小於 mx，代表和上一個區塊**有重疊**，沒辦法切。  
    而且因為重疊，使得當前區塊的右端點更新為 max(mx, e)。  
- 若 s 大於等於 mx，代表和尚一個區塊**沒有重疊**，可以切一刀，從 s, e 開始新的區塊。  
    區塊數加 1 ，新區塊的右端點 mx 也更新成 e。  

只要切出的區塊數大於等於 3 即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xs = []
        ys = []
        for x1, y1, x2, y2 in rectangles:
            xs.append([x1, x2])
            ys.append([y1, y2])

        def ok(a):
            a.sort()
            cnt = 1
            mx = a[0][1]
            for s, e in a[1:]:
                if s >= mx:
                    cnt += 1
                mx = max(mx, e)
            return cnt >= 3

        return ok(xs) or ok(ys)
```
