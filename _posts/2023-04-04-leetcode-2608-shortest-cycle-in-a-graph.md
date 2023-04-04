--- 
layout      : single
title       : LeetCode 2608. Shortest Cycle in a Graph
tags        : LeetCode Hard Array Graph BFS
---
雙周賽101。我一直卡在不知道如何處理奇數環和偶數環。正確應該在入佇列之前就判斷環，而不是進去後才判斷，有夠尷尬。  
最近官方水準越來越垃圾，不抓作弊就算了，還直接這種google名稱就可以找到答案的題目，直接冒出兩三千個作弊哥貼答案，誠實的同學們真的被打個半死。  

# 題目
有個n節點的雙向圖，節點編號分別為0\~n-1。  
二維陣列edges代表圖中的邊，其中edges[i] = [u<sub>i</sub>, v<sub>i</sub>]代表頂點u<sub>i</sub>和v<sub>i</sub>之間存在一條邊。  
兩節點之間最多只會有一條邊，且節點不會有邊連到自己。  

求圖中**最短**的環長度。如果沒有環則回傳-1。  

# 解法
若一個圖中存在多個環，使用dfs沒辦法保證一定走到最短的路徑，故無法找到最小環。  
使用bfs的話，從某個節點出發，只要某個節點被**訪問第二次**，必定是由兩條不同的路徑抵達，而這兩條路徑連接起來正好是一個環。  

但根據出發點的不同，最先找到的環也不同。所以必須窮舉每個節點做為出發點各bfs一次，看哪個環最小。  

![示意圖](/assets/img/2608.jpg)

在bfs時還有另一個問題：要如何判斷一個點是**自己剛走過的**，還是**別條路徑走過的**？  
只要在佇列中額外維護一個父節點變數fa，窮舉相鄰節點j時，若j=fa則略過不處理。若不為父節點且已經被訪問過，則代表找到環，以兩條路徑的長度加上1即為環長。   

時間複雜度O(N^2)。空間複雜度O(N+M)。  

```python
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g=[[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def bfs(i):
            dist=[-1]*n
            q=deque()
            q.append([i,-1]) # curr, fa
            step=0
            
            while q:
                for _ in range(len(q)):
                    i,fa=q.popleft()
                    dist[i]=step
                    for j in g[i]:
                        if j==fa:
                            continue
                        if dist[j]==-1: # unvisited
                            q.append([j,i])
                        else: # cycle found
                            return 1+dist[j]+dist[i]
                step+=1
            return inf

        ans=inf
        for i in range(n):
            ans=min(ans,bfs(i))
        
        if ans==inf:
            return -1
        
        return ans
```
