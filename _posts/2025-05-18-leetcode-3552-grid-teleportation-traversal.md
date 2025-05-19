---
layout      : single
title       : LeetCode 3552. Grid Teleportation Traversal
tags        : LeetCode Medium
---
weekly contest 450。  
BFS + 傳送門，總記得有做過相似題，一時找不到。  

## 題目

<https://leetcode.com/problems/grid-teleportation-traversal/description/>

## 解法

只能走 '.'，不能走 '#'。  
單純不管字母就是普通的 BFS 求最短路。  

---

字母之間可以成本 0 移動，且相同字母可能出現多次。  
每次可移動方向相當於 4 個相鄰格子，還有相同子母的格子。  

題目還限制每個傳送字母**至多使用一次**。  
假設有三個 A，記做 A1, A2, A3。  
從 A1 跳到 A2 再跳到 A3 是不合法的。  
但是也沒必要，真要跳的話直接 A1 到 A3 就好，經過其他中繼點沒意義。  

預處理所有相同字母的格子，之後用於求最短路。  
在最差情況下，所有格子的字母都相同、可互相傳送，每格都枚舉傳送位置複雜度高達 O((MN)^2)。  
根據上述結論，傳送時經過其他點沒意義，也就是說同樣字母**跳第二次也沒意義**。  
對於每個字母，只有第一次碰到時需要處理。  

---

普通移動成本 1，傳送成本 0。  
有不同的移動成本，需要優先處理成本更低的路徑，故改用 dijkstra。  

時間複雜度 O(MN log MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        M, N = len(matrix), len(matrix[0])

        # build teleport
        jump = defaultdict(list)
        for r in range(M):
            for c in range(N):
                x = matrix[r][c]
                if x in ".#":
                    continue
                jump[x].append((r, c))

        dist = [[inf] * N for _ in range(M)]
        dist[0][0] = 0
        h = [(0, 0, 0)]  # cost, r, c
        while h:
            cost, r, c = heappop(h)
            if r == M-1 and c == N-1:
                return cost
            if cost > dist[r][c]:
                continue

            # jump
            x = matrix[r][c]
            if x in jump:
                for (rr, cc) in jump[x]:
                    if cost < dist[rr][cc]:
                        dist[rr][cc] = cost
                        heappush(h, (cost, rr, cc))
                del jump[x]  # can only jump once

            # move
            for dx, dy in pairwise([0, 1, 0, -1, 0]):
                rr, cc = r+dx, c+dy
                if rr < 0 or rr == M or cc < 0 or cc == N or matrix[rr][cc] == "#":
                    continue
                new_cost = cost + 1
                if new_cost < dist[rr][cc]:
                    dist[rr][cc] = new_cost  # important pruning
                    heappush(h, (new_cost, rr, cc))

        return -1
```
