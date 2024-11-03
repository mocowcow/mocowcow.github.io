---
layout      : single
title       : LeetCode 3341. Find Minimum Time to Reach Last Room I
tags        : LeetCode Medium Matrix Graph BFS
---
weekly contest 422。  
竟然用 n x m 而不是慣用的 m x n，感覺不太舒服。  

## 題目

有個迷宮有 n x m 個房間，以網格狀表示。  

輸入 n x m 二維整數陣列 moveTime，其中 moveTime[i][j] 代表你在這個時間**以後**才可以**移動前往**。  
你在時間 t = 0 時從房間 (0, 0) 出發，每次可以移動到一個**相鄰**的房間。  
每次移動耗時為 1 秒。  

求抵達房間 (n - 1, m - 1) 所需的**最少**時間。  

若兩個房間同享一個牆壁 (水平或垂直皆可)，則視為**相鄰**的。  

## 解法

看到**最短路**、邊權不同，就知道是 djikstra。  
直接在二維矩陣上求最短路即可。  

時間複雜度 O(NM log NM)。  
空間複雜度 O(NM)。  

```python
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N, M = len(moveTime), len(moveTime[0])

        vis = [[False] * M for _ in range(N)]
        dist = [[inf] * M for _ in range(N)]
        heap = [[0, 0, 0]] # cost, r, c
        while heap:
            cost, r, c = heappop(heap)
            if cost > dist[r][c]:
                continue
            dist[r][c] = cost
            for dx, dy in pairwise([0,1,0,-1,0]):
                rr, cc = r+dx, c+dy
                if 0 <= rr < N and 0 <= cc < M:
                    new_cost = max(cost, moveTime[rr][cc]) + 1
                    if new_cost < dist[rr][cc]:
                        dist[rr][cc] = new_cost  # important pruning
                        heappush(heap, [new_cost, rr, cc])

        return dist[-1][-1]
```
