---
layout      : single
title       : LeetCode 3275. K-th Nearest Obstacle Queries
tags        : LeetCode Medium SortedList
---
weekly contest 413。  

## 題目

最初有個**空的** 2D 平面。  

輸入正整數 k。還有二維陣列 queries：  

- queries[i] = [x, y]，在座標 (x, y) 處建造障礙物。保證建造點一定是空的。  

每次查詢後，你必需找到距離原點**第 k 近**的障礙物。  

回傳整數陣列 results，其中 results[i] 代表第 i 次查詢後，**第 k 近**障礙物的距離；若不足 k 個障礙物則 results[i] = -1。  

座標 (x, y) 距離遠點的距離為 \|x\| + \|y\|。  

## 解法

有序容器值接維護所有障礙物的距離即可。  

時間複雜度 O(N log k)。  
空間複雜度 O(k)。  

```python
from sortedcontainers import SortedList as SL
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        ans = []
        sl = SL()
        for x, y in queries:
            dist = abs(x) + abs(y)
            sl.add(dist)
            if len(sl) > k:
                sl.pop(k)
            if len(sl) < k:
                ans.append(-1)
            else:
                ans.append(sl[k - 1])

        return ans
```
