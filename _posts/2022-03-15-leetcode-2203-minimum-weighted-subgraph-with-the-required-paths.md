---
layout      : single
title       : LeetCode 2203. Minimum Weighted Subgraph With the Required Paths
tags 		: LeetCode Hard Graph BFS
---
周賽284。  
被第三題搞快半死途中有來摸一下，知道用dijkstra，當時以為src1和src2一定會連成直線，沒想到src1和src2也可以只在dest交會，只過了21/78測資，又回去被第三題搞了。

# 題目
一個有向圖g，總共有n個點，編號為0~n-1，egdes為單向路線及權重。g的子圖必須能從src1和src2出發抵達dest，求最小總路徑權重為多少。若不可能達成則回傳-1。

# 解法
dijkstra演算法可以求某一點到其他點的最短距離。  
題目等價於：從src1和src2到某一個點i集合，再從i抵達dest，要選哪個i可以將權重最小化。  

先對兩個起點各做一次dijkstra，就知道在哪集合最划算。那麼要怎麼知道哪點前往dest最快？  
如果從每個別都做一次dijkstra，總共會是O(N*E log E)，鐵定超時。但如果將所有edges反過來，就相當於從dest前往其他點的最短距離。  
這樣就很簡單了，跑三次dijkstra拿到三個最短距離表格，看哪個i位置可以找到最小的和就是答案。

```python
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        def dijkstra(g, n, src):  # graph with n nodes start from src
            table = [math.inf]*(n)
            heap = [(0, src)]
            while heap:
                time, curr = heappop(heap)
                if time < table[curr]:
                    table[curr] = time
                    for adj, cost in g[curr]:
                        heappush(heap, (time+cost, adj))

            return table

        g = defaultdict(list)
        g_rev = defaultdict(list)
        for a, b, cost in edges:
            g[a].append((b, cost))
            g_rev[b].append((a, cost))

        t1 = dijkstra(g, n, src1)
        t2 = dijkstra(g, n, src2)
        t_dest = dijkstra(g_rev, n, dest)

        ans = math.inf
        for i in range(n):
            ans = min(ans, t1[i]+t2[i]+t_dest[i])

        return ans if ans != math.inf else -1
        
```

