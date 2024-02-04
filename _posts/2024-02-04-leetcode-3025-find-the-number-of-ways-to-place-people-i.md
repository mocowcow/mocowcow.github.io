---
layout      : single
title       : LeetCode 3025. Find the Number of Ways to Place People I
tags        : LeetCode Medium Array Simulation Sorting
---
雙周賽123。有點油的題目，可能是因為 Alice 和 Bob 出現太多次，這次主角變成動畫人物了。

## 題目

輸入 x \* 2 的二維陣列 points，代表平面上的某些點的整數座標點，其中 poins[i] = [x<sub>i</sub>, y<sub>i</sub>]。  

定義**右方**為 x 軸的方向，而**左方**為 x 軸的反方向；同理，**上方**為 y 軸方向，**下方**為 y 軸反方向。  

你必須安排包千束和瀧奈在內，共 n 個人的位置，每個點只能站一個人。  
千束想和瀧奈獨處，所以千束會建立一個矩形的柵欄，以自身為**左上角**，且瀧奈為**右下角**。柵欄不一定是矩形，也可能只是一條線。  
如果柵欄的**範圍內**中有其他人在，千束會很難過。  

求有幾組座標**數對**能夠分別放置千束和瀧奈，且不讓千束感到難過。  

## 解法

在測資不大的情況下，暴力法是可行的。  

枚舉所有數對 (i, j)，其中 i 是左上角，j 是右下角。  
判斷 i, j 之間的上下關係之後，再枚舉所有點 k，若沒有點存在兩者之間，則將答案加 1。  

時間複雜度 O(n^3)。  
空間複雜度 O(1)。  

```python
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i == j:
                    continue
                
                if not (x1 <= x2 and y1 >= y2):
                    continue
                
                for k, (x3, y3) in enumerate(points):
                    if k == i or k == j:
                        continue
                    if x1 <= x3 <= x2 and y1 >= y3 >= y2:
                        break
                else:
                    ans += 1
                    
        return ans
```
