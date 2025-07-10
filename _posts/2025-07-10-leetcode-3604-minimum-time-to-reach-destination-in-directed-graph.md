---
layout      : single
title       : LeetCode 3604. Minimum Time to Reach Destination in Directed Graph
tags        : LeetCode Medium Graph
---
biweekly contest 160。  
可能是近來最簡單 Q3。  

## 題目

<https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/description/>

## 解法

dijkstra 模板題。  
題目沒說清楚移動成本多少，但可以從範例看出邊權是 1。  

分類討論當前時間 cost 和邊的限制 s, e 的情形：  

- cost < s ：等到 s 才開始走  
- s <=  cost <= e： 直接走  
- e < cost：不能走  

所以其實只有兩種情況。  
若超過 e 就不走；否則出發時間為 max(cost, s)。  

時間複雜度 O(N + M log M)，其中 M = len(edges)。  
空間複雜度 O(N + M)。  

```python
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b, s, e in edges:
            g[a].append([b, s, e])

        dist = [inf] * n
        dist[0] = 0
        h = [(0, 0)]
        while h:
            cost, curr = heappop(h)
            if curr == n-1:
                return cost
            if cost > dist[curr]:
                continue
            for adj, s, e in g[curr]:
                if cost > e:
                    continue
                new_cost = max(cost, s) + 1
                if new_cost < dist[adj]:
                    dist[adj] = new_cost  # important pruning
                    heappush(h, (new_cost, adj))

        return -1
```
