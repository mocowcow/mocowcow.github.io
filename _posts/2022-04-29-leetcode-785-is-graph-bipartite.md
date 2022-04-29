--- 
layout      : single
title       : LeetCode 785. Is Graph Bipartite
tags        : LeetCode Medium Graph DFS BFS
---
每日題。還真的有併查集標籤，但這題一樣不適合，也沒必要用。

# 題目
輸入一個長度為N的二維陣列graph，代表有N個節點的無向圖，而graph[i]代表節點i的鄰接點，求此graph是否可以**二分**。  
**二分**的定義是：將所有節點分割成子集合A和子集合B，且所有相鄰的節點階屬於不同集合。

# 解法
就是點i如果是A組，那他鄰居就一定要是B；點i是B組，他鄰居一定要是A。  
AB組太麻煩了，改成01組比較好記，還沒分過組的就記-1。  

建立長度為N的陣列group，代表每個點的組別，初始為-1。  
遍歷每個點i，如果該點尚未分組，使用dfs將其分到0組，並不斷遞迴直到連通的點都分完組。若dfs過程中失敗，則直接回傳false。成功將每個點分完組則回傳true。

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def dfs(i,g):
            group[i]=g
            for j in graph[i]:
                if group[j]==-1:
                    if not dfs(j,g^1):
                        return False
                elif group[j]==g:
                    return False
            return True
        
        N=len(graph)
        group=[-1]*N
        for i in range(N):
            if group[i]==-1:
                if not dfs(i,0):
                    return False
        return True
```

改成bfs的版本，邏輯大同小異。

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:        
        N=len(graph)
        group=[-1]*N
        for i in range(N):
            if group[i]==-1:
                q=deque([(i,0)])
                while q:
                    curr,g=q.popleft()
                    group[curr]=g
                    for adj in graph[curr]:
                        if group[adj]==-1:
                            q.append((adj,g^1))
                        elif group[adj]==g:
                            return False
                        
        return True
```
