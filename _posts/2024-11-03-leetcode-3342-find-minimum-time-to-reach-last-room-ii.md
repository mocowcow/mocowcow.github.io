---
layout      : single
title       : LeetCode 3342. Find Minimum Time to Reach Last Room II
tags        : LeetCode Medium Matrix Graph BFS
---
weekly contest 422。  
跟上一題差不多，有點偷懶。  

## 題目

有個迷宮有 n x m 個房間，以網格狀表示。  

輸入 n x m 二維整數陣列 moveTime，其中 moveTime[i][j] 代表你在這個時間**以後**才可以**移動前往**。  
你在時間 t = 0 時從房間 (0, 0) 出發，每次可以移動到一個**相鄰**的房間。  
每次移動耗時為 1 秒、2 秒、 1 秒，如此**不斷交替**。  

求抵達房間 (n - 1, m - 1) 所需的**最少**時間。  

若兩個房間同享一個牆壁 (水平或垂直皆可)，則視為**相鄰**的。  

## 解法

和 Q2 差別在於移動的時間成本會根據步數改變。  
步數為奇數時成本 1、偶數時成本 2。  

假設想從 (0, 0) 移動到 (0, 1) 時，為奇數步數 x，成本 1。  
無論怎麼繞路，前往 (0, 1) 的步數依然是 x+2y 的奇數。  

也就是說，目標位置 (r, c) 的**列數**加**行數**的奇偶性等同於步數的奇偶性。  
按照此方式決定時間成本即可。  

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
            # next step is (r+c+1)
            move_cost = 1 if (r+c+1) % 2 == 1 else 2
            for dx, dy in pairwise([0,1,0,-1,0]):
                rr, cc = r+dx, c+dy
                if 0 <= rr < N and 0 <= cc < M:
                    new_cost = max(cost, moveTime[rr][cc]) + move_cost
                    if new_cost < dist[rr][cc]:
                        dist[rr][cc] = new_cost  # important pruning
                        heappush(heap, [new_cost, rr, cc])

        return dist[-1][-1]
```
