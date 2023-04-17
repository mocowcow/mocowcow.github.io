--- 
layout      : single
title       : LeetCode 2642. Design Graph With Shortest Path Calculator
tags        : LeetCode Hard Array Graph BFS
---
雙周賽102。看錯測資範圍，用floyd-warshall不小心超時一次，可惜。  

# 題目
有個n節點的**有向權重**圖，節點編號分別為0\~n-1。  
陣列edges代表初始的邊，其中edges[i] = [fromi, toi, edgeCosti]代表一條從fromi到toi的邊，且成本為costi。  

實作類別Graph：  
- 建構子Graph(int n, int[][] edges)，初始化n個節點和edges中的所有邊  
- addEdge(int[] edge)，將edge加入圖中，其中edge = [from, to, edgeCost]。保證兩節點之間最多一條邊  
- int shortestPath(int node1, int node2)，回傳node1到node2的**最小**成本。若不存在路徑則回傳-1  
    
# 解法
說到最短路徑，很容易想到floyd或是dijkstra。  

先看看測資，最多n=100個點，n\*n=10000個邊，最多呼叫方法100次。  
floyd每次計算要O(n^3)，但是之後還要加入新的邊，那麼加入100次邊是會超時的；而dijkstra計算一次是O(E + V log V)，計算100次大約在10^6次運算，可以接受。  

接下來就只要實現原版的dijkstra最短路演算法就可以了。  

addEdge時間複雜度O(1)，shortestPath時間複雜度O(E + V log V)。  

整體時間複雜度O(q*(E + V log V))，其中q為shortestPath呼叫次數。空間複雜度O(E + V)。  

```python
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.g=[[] for _ in range(n)]
        for e in edges:
            self.addEdge(e)
            
    def addEdge(self, edge: List[int]) -> None:
        a,b,c=edge
        self.g[a].append([b,c])

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1==node2:
            return 0
        dist=[inf]*self.n
        h=[]
        heappush(h,[0,node1])
        while h:
            cost,i=heappop(h)
            if i==node2:
                return cost
            if dist[i]<=cost:
                continue
            dist[i]=cost
            for j,c in self.g[i]:
                heappush(h,[cost+c,j])
        return -1
```
