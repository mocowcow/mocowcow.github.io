--- 
layout      : single
title       : LeetCode 2642. Design Graph With Shortest Path Calculator
tags        : LeetCode Hard Array Graph BFS DP
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

其實floyd也可以用在這題，只是我對他不夠熟悉，一時間沒想出來。  

floyd的矩陣dp[k][i][j]定義為：在加入第k個點後，從i到j的最短路徑。而dp[k]會從dp[k-1]轉移而來，第一維的空間可以壓縮掉。  

之後每次呼叫addEdge時都會加入一條新的邊[a,b]，如果這條邊能夠讓某些路徑變小，那他們**肯定要經過[a,b]**。所以窮舉所有路徑[i,j]，並以[a,b]作為中繼點更新最短距離，所生成的路徑即為[i,a,b,j]。  

有些細節需要注意：  
- 在加入一條新的邊[a,b]，其成本為c時，可以先檢查現有的[i][j]是否小於c？若小於c，則不管如何都不可能更小，可以直接跳出  
- dp[a][b]在窮舉[i,j]的時，i=a且j=b時就會更新到，不必刻意寫出來。若自己寫，又沒有檢查dp[a][b]當前值就會出錯  

時間複雜度O(n^3+q*(n^2))，其中q為addEdge的呼叫次數。空間複雜度O(n^2)。  

```python
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.dp=[[inf]*n for _ in range(n)]
        
        for i in range(n):
            self.dp[i][i]=0
        
        for a,b,c in edges:
            self.dp[a][b]=c
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    new_dist=self.dp[i][k]+self.dp[k][j]
                    if new_dist<self.dp[i][j]:
                        self.dp[i][j]=new_dist

    def addEdge(self, edge: List[int]) -> None:
        a,b,c=edge

        # 比現有路徑還差就不更新了
        if self.dp[a][b]<c:
            return 

        # self.dp[a][b]=c
        for i in range(self.n):
            for j in range(self.n):
                    new_dist=self.dp[i][a]+self.dp[b][j]+c
                    if new_dist<self.dp[i][j]:
                        self.dp[i][j]=new_dist
    
    def shortestPath(self, node1: int, node2: int) -> int:
        ans=self.dp[node1][node2]

        if ans==inf :
            return -1
        
        return ans
```