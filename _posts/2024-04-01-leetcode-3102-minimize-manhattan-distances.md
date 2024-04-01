---
layout      : single
title       : LeetCode 3102. Minimize Manhattan Distances
tags        : LeetCode Hard Array Math Geometry SortedList
---
周賽 391。看關鍵字猜題翻車了，我看到**最大值最小化**就想著二分答案，結果根本不是。  

## 題目

輸入陣列 poins，代表二維平面上的某些整數坐標，其中 points[i] = [x<sub>i</sub>, y<sub>i</sub>]。  

定義兩點之間的距離為他們的**曼哈頓距離**。  

求正好移除一個點之後，剩餘點中的任意兩點之間的**最大**距離的**最小值**。  

## 解法

先來看看曼哈頓距離的公式：  

- \|x1 - x2\| + \|y2 - y2\|  

好像沒辦法直接拿來用。這種給定公式的題目，很多都要靠移項或是重排變數，進而消除變數之間的關聯。  
總之先把礙事的絕對值處理掉。  

---

對於 x 軸距離差來說，根據 x1 和 x2 的大小不同，有可能是 (x1 - x2) 或是 (x2 - x1)；對於 y 軸同理。  
將絕對值拆掉後，相當於以下四個公式取最大值：  

- (x1 - x2) + (y1 - y2)  
- (x2 - x1) + (y1 - y2)  
- (x1 - x2) + (y2 - y1)  
- (x2 - x1) + (y2 - y1)  

為了降低兩個點的關聯性，把來自同個坐標的變數放到一起：  

- x1 - x2 + y1 - y2 變成 x1 + y1 - x2 - y2  
- x2 - x1 + y1 - y2 變成 -x1 + y1 + x2 - y2  
- x1 - x2 + y2 - y1 變成 x1 - y1 - x2 + y2  
- x2 - x1 + y2 - y1 變成 -x1 - y1 + x2 + y2  

並且基於**對稱性**，(p1, p2) 等價於 (p2, p1)，所以第一和第四項等價、第二和第三項等價。  
再把係數提出來：  

- (x1 + y1) - (x2 + y2)  
- -(x1 - y1) + (x2 - y2)  

最後，座標 (x, y) 被分解成 (x + y) 和 (x - y)，只要透過他們就能求出兩點距離。  

---

剛才推出的是兩點之間的距離，那要怎麼找到**任意兩點**的最大值？  
其實很簡單，為了使結果最大化，當然是代入他們的最大/最小值。  

先求出所有點的 (x + y) 及 (x - y) 值，以**有序容器**保存，方便查詢極值。分別記做 A 和 B。  
枚舉需要被移除的坐標 points[i] = (x, y)，先從 A 和 B 中暫時移除對應的值，依照上述公式求出最大距離，並更新答案最小值，然後再把剛才移除的值加回去。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        A = SL() # x + y
        B = SL() # x - y
        
        def add(x, y):
            A.add(x + y)
            B.add(x - y)
        
        def remove(x, y):
            A.remove(x + y)
            B.remove(x - y)
        
        for x, y in points:
            add(x, y)
            
        ans = inf
        for x, y in points:
            remove(x, y)
            dis = max(
                A[-1] - A[0], # max(x1 + y1) - min(x2 + y2) 
                -B[0] + B[-1]  # -min(x1 - y1) + max(x2 - y2)  
            )
            ans = min(ans, dis)
            add(x, y)
            
        return ans
```
