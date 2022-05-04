--- 
layout      : single
title       : LeetCode 778. Swim in Rising Water
tags        : LeetCode Hard Array Matrix BinarySearch BFS UnionFind Heap
---
[1970. last day where you can still cross]({% post_url 2022-05-04-leetcode-1970-last-day-where-you-can-still-cross %})的簡單版。可以二分搜、併查集，竟然還能用heap，神奇了。

# 題目
輸入一個N*N的矩陣grid，其中grid[r][c]=i，代表(r,c)的高度為i。  
在時間為t時，水位會上升到t，你可以在高度不大於t的位置任意游泳。求可以從(0,0)移動到(n-1,n-1)的最短時間。  

# 解法
講白話就是：grid[r][c]=i，格子(r,c)要等到時間i才可以走。  

先來一個併查集解法。  
將grid轉成依出現時間排序的陣列land，land[i]=時間i出現的路線。  
從時間i=0開始，依序將對應的路線(r,c)加入，並連通四方可以通行的格子。  
若左上角與右下角可以連通，則回傳i。

```python
class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        land=[0]*(N*N)
        start=(0,0)
        end=(N-1,N-1)
        uf=UnionFind()
        for r in range(N):
            for c in range(N):
                land[grid[r][c]]=(r,c)
        for i,(r,c) in enumerate(land):
            uf.parent[(r,c)]=(r,c)
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if (0<=nr<N and 0<=nc<N) and (nr,nc) in uf.parent:
                    uf.union((r,c),(nr,nc))
            if start in uf.parent and end in uf.parent and uf.find(start)==uf.find(end):
                return i
```

回來用二分搜+bfs解，查看grid[r][c]的值，小於等於day就可以走。  
下界定為0，上界定為N*N。如果mid無法成功抵達，則更新下界為mid+1；成功抵達則更新上界為mid。

```python
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        
        def canCross(day):
            q=deque([(0,0)])
            visited=set()
            visited.add((0,0))
            while q:
                r,c=q.popleft()
                if grid[r][c]>day:
                    continue
                if r==c==N-1: # reach end
                    return True
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if (0<=nr<N and 0<=nc<N) and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            return False
            
        lo=0
        hi=N*N
        while lo<hi:
            mid=(lo+hi)//2
            if not canCross(mid):
                lo=mid+1
            else:
                hi=mid
            
        return lo
```

heap解法，太神了。  
有點像是dijkstra，優先選擇日期較小的可用路徑，邊走邊更新日期最大值ans，走到終點時回傳ans。

```python
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        h=[(grid[0][0],0,0)] # elevation, r, c
        visited=set([(0,0)])
        ans=0
        while h:
            t,r,c=heappop(h)
            ans=max(ans,t)
            if r==c==N-1:
                return ans
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if (0<=nr<N and 0<=nc<N) and (nr,nc) not in visited:
                    heappush(h,(grid[nr][nc],nr,nc))
                    visited.add((nr,nc))
```
        