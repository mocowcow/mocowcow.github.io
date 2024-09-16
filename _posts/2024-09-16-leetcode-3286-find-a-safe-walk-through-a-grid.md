---
layout      : single
title       : LeetCode 3286. Find a Safe Walk Through a Grid
tags        : LeetCode Medium Graph BFS
---
biweekly contest 139。  
比賽時馬上連想到相似題 [2290. minimum obstacle removal to reach corner]({% post_url 2022-05-31-leetcode-2290-minimum-obstacle-removal-to-reach-corner %})。  
隔了兩年還有印象，感覺真不錯。  

## 題目

輸入 m \* n 的二進位矩陣 grid，還有整數 health。  

你從左上角 (0, 0) 出發，要前往右下角 (m - 1, n - 1)。  

你在 health 保持正數時，可以移動到上下左右相鄰的格。  
若 grid[i][j] = 1，則代表在格子 (i, j) 上會使 health 減少 1。  

若抵達右下角時 能剩下 1 或更多 health，回傳 true；否則回傳 false。  

## 解法

把格子上的值看做**權重**，以圖論方向思考。  
需要找到一條**權重加總**小於 health 的路徑，直接考慮**最短路**。  

直接上 dijkstra，判斷從左上到右下角做短路是否小於 health 即可。  

時間複雜度 O(MN log MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        M, N = len(grid), len(grid[0])

        dist = [[inf] * N for _ in range(M)]
        dist[0][0] = grid[0][0]
        h = [[grid[0][0], 0, 0]]
        while h:
            cost, r, c = heappop(h)
            if r == M-1 and c == N-1:
                break
            if cost > dist[r][c]:
                continue
            for dx, dy in pairwise([0,1,0,-1,0]):
                rr, cc = r+dx, c+dy
                if not (0 <= rr < M and 0 <= cc < N):
                    continue
                new_cost = cost + grid[rr][cc]
                if new_cost < dist[rr][cc]:
                    dist[rr][cc] = new_cost
                    heappush(h, [new_cost, rr, cc])

        return dist[M-1][N-1] < health
```

觀察發現 grid 中的權重只有 0 和 1 兩種，可以做 **0-1 bfs**。  
走到邊權為 0 的相鄰格子時，將其加回隊首；走到不為 0 的相鄰格子則加到對尾。  
如此可以保證先將較小的路徑處理完，而且比起 heap 更加有效率。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        M, N = len(grid), len(grid[0])

        dist = [[inf] * N for _ in range(M)]
        dist[0][0] = grid[0][0]
        q = deque()
        q.append([grid[0][0], 0, 0])
        while q:
            cost, r, c = q.popleft()
            if r == M-1 and c == N-1:
                break
            for dx, dy in pairwise([0,1,0,-1,0]):
                rr, cc = r+dx, c+dy
                if not (0 <= rr < M and 0 <= cc < N):
                    continue
                if dist[rr][cc] == inf:
                    new_cost = cost + grid[rr][cc]
                    if grid[rr][cc] == 0: # add to head
                        q.appendleft([new_cost, rr, cc])
                    else: # add to tail
                        q.append([new_cost, rr, cc])
                    dist[rr][cc] = new_cost

        return dist[M-1][N-1] < health
```
