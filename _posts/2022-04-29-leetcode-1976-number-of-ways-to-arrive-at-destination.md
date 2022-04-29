--- 
layout      : single
title       : LeetCode 1976. Number of Ways to Arrive at Destination
tags        : LeetCode Medium Graph DP BFS
---
以前沒寫出來的，今天再試試，原來又是dijkstra變種。

# 題目
輸入整數n，及二維陣列roads，代表有n個節點的無向連通圖。roads[i]=[a,b,time]，代表a和b點的距離為time。  
求由0出發，抵達n-1點的**最短路徑有幾種**。

# 解法
最短路徑八成還是dijkstra，但是又要求有幾種方式，就要加上計數DP。  
陣列dis紀錄從0出發，抵達某點的最短距離。陣列cnt用來計算有幾種方式抵達。  
固定從0出發，所以dis[0]要初始為0距離，cnt[0]初始為1種。  
每次取出總距離最短的點curr，對所有鄰接點adj檢查是否能更新最短路徑，若成功更新，則將cnt[adj]設為cnt[curr]，並將此adj和其新距離加入heap；若此路徑距離與原最短距離相等，則路徑計數增加cnt[curr]次；若新路徑大於最短距離則不處理。  
等heap處理完就可以回傳cnt[n-1]，或是要在bfs中提前結束也可以。

```python
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9+7
        g = defaultdict(list)
        for a, b, t in roads:
            g[a].append((b, t))
            g[b].append((a, t))
        dis = [math.inf]*n
        dis[0] = 0
        cnt = [0]*n
        cnt[0] = 1
        heap = [(0, 0)]
        while heap:
            time, curr = heappop(heap)
            for adj, cost in g[curr]:
                newTime = time+cost
                if newTime < dis[adj]:
                    dis[adj] = newTime
                    cnt[adj] = cnt[curr]
                    heappush(heap, (newTime, adj))
                elif newTime == dis[adj]:
                    cnt[adj] += cnt[curr]
                    
        return cnt[n-1] % MOD
```
