---
layout      : single
title       : LeetCode 2812. Find the Safest Path in a Grid
tags        : LeetCode Medium Array Matrix BFS UnionFind HashTable
---
周賽357。再次確認我真的很會並查集。  

## 題目

輸入n\*n二維矩陣grid，其中(r,c)代表：  

- grid\[r][c] = 1，代表有小偷  
- grid\[r][c] = 0，代表空格子  

你最初位於格子(0,0)。每次移動，你可以移動到相鄰的格子，有小偷的格子也可以。  

路徑的**安全度**指的是路徑中所有格子和任意小偷的**最短**曼哈頓距離。  

求抵達格子(n-1, n-1)的路徑**最大安全度**為多少。  

## 解法

測資只告訴你那些位置有小偷，但我們需要知道每個格子距離小偷的最短距離。  
先找到所有小偷位置，開始bfs，計算出所有格子的**安全度**。  

因為要求安全度越高越好，就從最高的格子開始走。如果只靠安全度x以上的格子無法抵達終點，就降低標準為x-1、x-2...。  
而快速判斷起點與終點是否連通，就用到我們的好朋友**並查集**。  

依照預處理好的**安全度**將所有格子分組，以遞減順序將每批格子加入並查集。檢查起點與終點是否連通，若連通則回傳當前安全度，否則繼續降低安全度。  

總共n^2個格子，但最差情況下只有一個小偷在角落，會產生2n種安全度。  
我採用的並查集沒有按秩合併，每次合併均攤大約是O(log 2n)，共需要合併n^2次。  
時間複雜度O(n^2 log n)。如果按至合併可以優化到O(n^2)。  
時間複雜度O(n^2)。  

```python
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N=len(grid)
        start=(0,0)
        end=(N-1,N-1)
        fa={}
        
        def find(x):
            if fa[x]!=x:
                fa[x]=find(fa[x])
            return fa[x]
        
        def union(a,b):
            f1=find(a)
            f2=find(b)
            if f1!=f2:
                fa[f1]=f2
        
        # mark thief
        safe=[[inf]*N for _ in range(N)]
        g=defaultdict(list)
        q=deque()
        for r in range(N):
            for c in range(N):
                if grid[r][c]==1:
                    q.append([r,c,0])
                    safe[r][c]=0
        
        # bfs safeness from thief
        while q:
            r,c,sf=q.popleft()
            g[sf].append((r,c))
            for dx,dy in pairwise([0,1,0,-1,0]):
                rr,cc=r+dx,c+dy
                if 0<=rr<N and 0<=cc<N and safe[rr][cc]==inf:
                    q.append([rr,cc,sf+1])
                    safe[rr][cc]=sf+1
                
        for k in sorted(g.keys(),reverse=True):
            for r,c in g[k]:
                fa[(r,c)]=(r,c)
                for dx,dy in pairwise([0,1,0,-1,0]):
                    rr,cc=r+dx,c+dy
                    if (rr,cc) in fa:
                        union((rr,cc),(r,c))
            
            if start in fa and end in fa and find(start)==find(end):
                return k
```
