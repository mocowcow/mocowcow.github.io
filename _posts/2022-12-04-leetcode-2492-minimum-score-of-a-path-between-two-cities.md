--- 
layout      : single
title       : LeetCode 2492. Minimum Score of a Path Between Two Cities
tags        : LeetCode Medium Array Graph DFS HashTable
---
周賽322。花了一些時間才搞懂題目講什麼，但還是恥辱WA一次。  

# 題目
輸入整數n，代表n個城市，編號分別為1\~n。  
還有二維整數陣列roads，其中roads[i] = [a<sub>i</sub>, b<sub>i</sub>, distance<sub>i</sub>]，代表a<sub>i</sub>, b<sub>i</sub>之間存在一條距離為distance<sub>i</sub>的**雙向**路徑。  
每個城市不一定存在連外道路。  

介於兩個城市間的路徑，其**分數**取決於所經道路中的**最小距離**。  

求城市1前往城市n的**最小路徑分數**為多少。  

備註：  
- 路徑指的是兩個城市中的一連串道路  
- 路徑中可以包含同樣的道路**數次**，也可以多次訪問城市1和n  
- 測資保證城市1和n之間至少存在一條路徑  

# 解法
題目希望的是盡可能走**距離較短的道路**，而不在意總移動距離，就算走到很多不需要的城市也沒關係。  
所以我們從1開始出發，把所有能走的**道路**全部走過一遍，其中距離最短的道路就是答案。  

寫一個dfs(i)函數，把城市i所有的路都走一次，然後把道路的距離加到路徑path中。最後path中最小值就是答案。  
注意：是**所有道路**，而非**所有城市**，一定要在dfs進入某城市i之後才標記visited，否則會漏掉某些道路沒走過。  

時間複雜度為O(M+N)，其中M為道路總數，N為城市總數。因為道路是雙向的，所以每條最多走兩次。  
空間複雜度一樣O(M+N)，需要N個城市的visited陣列，加上M條道路建圖。  

```python
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g=defaultdict(list)
        for a,b,dis in roads:
            g[a].append([b,dis])
            g[b].append([a,dis])
        
        vis=[False]*(n+1)
        path=[]
        
        def dfs(i):
            if vis[i]:return 
            vis[i]=True
            for j,dis in g[i]:
                    path.append(dis)
                    dfs(j)
            
        dfs(1)
                    
        return min(path)
```
