---
layout      : single
title       : LeetCode 3143. Maximum Points Inside the Square
tags        : LeetCode Medium Array String Geometry HashTable Sorting
---
雙周賽 130。好像滿多作法的，最佳做法竟然是 O(N)，非常神奇。  

## 題目

輸入二維整數陣列 points 還有字串 s，其中 points[i] 代表第 i 個點的座標，且 s[i] 代表第 i 個點的**標籤**。  

一個**有效的**正方形必須以原點 (0, 0) 為中心，邊與數軸平行，且包含的點**不可**有相同標籤。  

求**有效**正方形**最多**可以包含幾個點。  

注意：  

- 在邊上的點也視作被包含  
- 正方形的邊長可以是 0  

## 解法

仔細觀察發現，對於座標 (x, y) 的點，他會被邊長為 max(x, y) 的正方形包含。  

先將點按照 max(x, y) 分組。  
從小到大枚舉組別，試著將組中的所有點加入。若出現重複標籤就退出循環，否則將組內的點個數加入答案。  
注意：一組中可能就包含兩個同樣的標籤，先檢查完才能更新答案。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        d = defaultdict(list)
        for i, (x, y) in enumerate(points):
            val = max(abs(x), abs(y))
            d[val].append(s[i])
            
        vis = set()
        ans = 0
        for k, v in sorted(d.items()):
            for c in v:
                if c in vis:
                    return ans
                vis.add(c)
            ans += len(v)
        
        return ans
```
