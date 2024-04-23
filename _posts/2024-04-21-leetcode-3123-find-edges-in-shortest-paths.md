---
layout      : single
title       : LeetCode 3123. Find Edges in Shortest Paths
tags        : LeetCode Hard Array Graph BFS Heap
---
周賽 394。久違的無 BUG 通關，終於又打回 2400 分了。  

## 題目

有個 n 節點的**無向**權重圖，節點編號從 0 到 n - 1。  
有 m 條邊，輸入二維整數陣列 edges，其中 edges[i] = [a<sub>i</sub>, b<sub>i</sub>, w<sub>i</sub>]，代表 a<sub>i</sub> 和 b<sub>i</sub> 之間存在一條權重為 w<sub>i</sub> 的邊。  

對於圖中從節點 0 出發到節點 n - 1 的**所有**最短路徑中，有哪些邊**至少**屬於一條最短路。  
回傳陣列 answer，其中 answer[i] = true 代表邊 edge[i] 能構成最短路；否則 answer[i] = false。  

注意：圖可能不連通。  

## 解法

從 0 出發到 n - 1 的最短路徑，很直覺就是 dijkstra。  
但在過程中，並不保證先碰到的邊一定是最短的，無法判斷哪條邊構成最短路。  

設 dist(u, v) 為兩點的最短距離，且 dist(0, n - 1) = target。  
若某條權重為 w 的邊 [a, b] 能構成最短路，則以下兩者之一必定成立：  

- dist(0, a) + w + dist(b, n - 1)  == target  
- dist(0, b) + w + dist(a, n - 1)  == target  

為了知道從 **0 到任意點**的最短距離，需要從 0 出發跑一次 dijkstra。  
為了知道從**任意點到 n - 1**的最短距離，也需要從 n - 1 出發再跑一次 dijkstra。  
之後只需要枚舉每條邊 edges[i]，並按照上述公式判斷即可。  

注意：若 python 使用 inf 作為最短距離的初始值，記得特判 **0 和 n - 1 是否連通**，否則會誤判。  

時間複雜度 O(n + m log m)。  
空間複雜度 O(n + m)。  

```python
class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        M = len(edges)
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append([b, w])
            g[b].append([a, w])
            
        dist1 = dijkstra(g, n, 0) # 0 to any
        dist2 = dijkstra(g, n, n - 1) # n-1 to any
        ans = [False] * M
        target = dist1[n - 1]
        
        if target == inf: # unreachable
            return ans
        
        for i, (a, b, w) in enumerate(edges):
            dist = min(
                dist1[a] + dist2[b], # [0, a, b, n-1]
                dist1[b] + dist2[a]  # [0, b, a, n-1]
            )
            if dist + w == target:
                ans[i] = True
        
        return ans 
    
def dijkstra(g, n, src):
    dist = [inf] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        cost, curr = heappop(heap)
        if cost > dist[curr]:
            continue
        dist[curr] = cost
        for adj, c in g[curr]:
            new_cost = cost + c
            if new_cost < dist[adj]:
                dist[adj] = new_cost  # important pruning
                heappush(heap, (new_cost, adj))
    return dist
```

dijkstra 只能求起點到其他任意點的最短距離。  
假設已知 dist(0, i) = target。  

如果 i 存在滿足 dist(0, i) = dist(0, j) + w 的鄰接點 j，則**代表 j 可以成為最短路的中介點**。  
連接 i 和 j 的邊就是我們要找的答案。為了知道是哪條邊，建圖的時候要保存邊的索引 ei。  

而對於 dist(0, i) 來說，滿足條件的中介點 j 可能不只一個，這意味著每個 j 點都可以再次找到其他中介點，因此需要靠 dfs 遞迴到出發點 0 為止。  
注意：即使相鄰的 j 點已經訪問過，也還是要檢查與其連接的邊 ei，因為可能不只一條最短路徑。  

時間複雜度 O(n + m log m)。  
空間複雜度 O(n + m)。  

```python
class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        M = len(edges)
        g = [[] for _ in range(n)]
        for ei, (a, b, w) in enumerate(edges):
            g[a].append([b, w, ei])
            g[b].append([a, w, ei])
            
        dist = dijkstra(g, n, 0) # 0 to any
        ans = [False] * M
        
        if dist[n - 1] == inf: # unreachable
            return ans
        
        vis = [False] * n
        def dfs(i):
            if vis[i]:
                return
            vis[i] = True
            for j, w, ei in g[i]:
                if dist[i] == dist[j] + w:
                    ans[ei] = True
                    dfs(j)
        
        dfs(n - 1)
        
        return ans 
    
def dijkstra(g, n, src):
    dist = [inf] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        cost, curr = heappop(heap)
        if cost > dist[curr]:
            continue
        dist[curr] = cost
        for adj, c, _ in g[curr]:
            new_cost = cost + c
            if new_cost < dist[adj]:
                dist[adj] = new_cost  # important pruning
                heappush(heap, (new_cost, adj))
    return dist
```
