--- 
layout      : single
title       : LeetCode 2290. Minimum Obstacle Removal to Reach Corner
tags        : LeetCode Hard Array Matrix Graph BFS
---
周賽295。當時用了dijkstra最短路徑，結果不知道為啥TLE，還是隱藏測資。但也沒看到其他人被隱藏測資卡，奇怪。

# 題目
輸入m*n的整數二維陣列grid。每個格子以下列兩種數字組成：  
- 0代表空格  
- 1代表可以被移除的障礙物  

你可以從每個位置向上下左右四方任意移動。  
回傳從左上角(0,0)移動到右下角(m-1,n-1)所需要移除的最小障礙物數量。  

# 解法
看到有人說這題的最佳解是M*N，第一時間還以為他說錯了，沒想到是真的。  
這種方法叫做**0-1 BFS**，又稱**雙向佇列BFS**，用於只有兩種權重的graph。  

在這題裡面可以把空格當作權重0，而障礙物權重1，而我們需要求最短路徑，當然是優先走完所有的0。  
那我們在某個位置(r,c)時，試著向周圍BFS，若鄰居的權重為0，則將其押回deque的左端；不為0則押到右端。  
如此一來能夠確保相同成本的路徑都優先被處理完，之後才會處理次小的路徑。  

```python
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        DIRS=[[0,1],[0,-1],[1,0],[-1,0]]
        visited=[[False]*N for _ in range(M)]
        q=deque()
        q.append([0,0,grid[0][0]])
        
        while q:
            r,c,rmv=q.popleft()
            if r==M-1 and c==N-1:
                return rmv
            for dx,dy in DIRS:
                nr,nc=r+dx,c+dy
                if not (0<=nr<M and 0<=nc<N) or visited[nr][nc]:
                    continue
                visited[nr][nc]=True
                if grid[nr][nc]==0:
                    q.appendleft([nr,nc,rmv])
                else:
                    q.append([nr,nc,rmv+1])
```

試著再寫一次dijkstra，竟然過了，速度還和上面那種差不多，大概是我多做了太多不需要的事。  

```python
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        DIRS=[[0,1],[0,-1],[1,0],[-1,0]]
        visited=[[False]*N for _ in range(M)]
        visited[0][0]=True
        h=[(grid[0][0],0,0)]
        
        while h:
            rmv,r,c=heappop(h)
            if r==M-1 and c==N-1:
                return rmv
            for dx,dy in DIRS:
                nr,nc=r+dx,c+dy
                if not (0<=nr<M and 0<=nc<N) or visited[nr][nc]:
                    continue
                visited[nr][nc]=True
                heappush(h,(rmv+grid[nr][nc],nr,nc))
```