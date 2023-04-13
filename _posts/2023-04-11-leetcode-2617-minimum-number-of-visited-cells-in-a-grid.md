--- 
layout      : single
title       : LeetCode 2617. Minimum Number of Visited Cells in a Grid
tags        : LeetCode Hard Array Matrix Heap SortedList
---
周賽339。和上週的Q4有點類似，都會重複訪問到同一個位置數次，需要用一些方法優化。  

# 題目
輸入m\*n的整數矩陣grid。你一開始從**左上角**(0, 0)出發。  

當你位於(i, j)時，你可以移動到以下任意格子：  
- (i, k)，其中j < k <= grid[i][j] + j  
- (k, j)，其中i < k <= grid[i][j] + i  

求抵達**右下角**(m-1, n-1)的最小移動次數。若無法抵達則回傳-1。  

# 解法
如果照著普通的BFS做法的話，複雜度會高達O(MNk)，大概是10^10次運算，肯定超時。  

先考慮只能向右走的情形，例如：  
> grid = [[2,2,2,0]]  
> (0,0)為起點，步數1  
> (0,1)可以從(0,0)抵達，步數2  
> (0,2)可以從(0,0)抵達，步數2；或是從(0,1)抵達，步數3  
> (0,3)可以從(0,1)抵達，步數3；或是從(0,2)抵達，步數4  

對於每個點(r,c)，要選擇其左方**步數最小**，且移動距離足夠的上一點。  

為了維護每一列中已經訪問過、且步數最小的點，可以對每一列都使用一個min heap。  
同理，對每一行也使用一個min heap，記錄該行訪問過的列數。  
當我們在(r,c)時，就從第r列左方某一點過來，或是從第c列上方某一點過來，取步數最小者。  
如果(r,c)是可抵達的，則將(r,c)及其最小步數加入**對應行列**的min heap，以供之後的位置使用。  

每個位置最多入heap兩次，分別為O(log M)和O(log N)，總共MN個元素。  
時間複雜度O(MN \* log(M+N))。空間複雜度O(MN)。  

```python
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        row=[[] for _ in range(M)] # step, c
        col=[[] for _ in range(N)] # step, r
        dist=[[inf]*N for _ in range(M)]
        dist[0][0]=1
        
        for r in range(M):
            for c in range(N):
                # pop invalid col source
                h=row[r]
                while h and h[0][1]+grid[r][h[0][1]]<c:
                    heappop(h)
                    
                # update (r,c) from same row
                if h:
                    dist[r][c]=min(dist[r][c],h[0][0]+1)
                    
                # pop invalid row source
                h=col[c]
                while h and h[0][1]+grid[h[0][1]][c]<r:
                    heappop(h)
                    
                # update (r,c) from same col
                if h:
                    dist[r][c]=min(dist[r][c],h[0][0]+1)
        
                # go down or right
                if dist[r][c]!=inf:
                    heappush(row[r],(dist[r][c],c))
                    heappush(col[c],(dist[r][c],r))

        if dist[-1][-1]==inf:
            return -1
        
        return dist[-1][-1]
```

上面的heap方法是維護走過的節點，在訪問到新的(r,c)時，從已經訪問的點找到合法的來源。  

另一個思路是照著[2612. minimum reverse operations]({% post_url 2023-04-07-leetcode-2612-minimum-reverse-operations %})的方法，對每個行列都使用一個sorted list，維護該行列中可以訪問的位置，並把訪問過的位置刪除掉。  

時間複雜度O(MN \* log(M+N))。空間複雜度O(MN)。  

```python
from sortedcontainers import SortedList

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        row=[SortedList(range(N)) for _ in range(M)]
        col=[SortedList(range(M)) for _ in range(N)]
        q=deque()
        q.append((0,0))
        step=1
        
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                if r==M-1 and c==N-1:
                    return step
                
                val=grid[r][c]
                t=[]
                for cc in row[r].irange(c+1,c+val):
                    t.append((r,cc))
                
                for rr in col[c].irange(r+1,r+val):
                    t.append((rr,c))

                for r,c in t:
                    q.append((r,c))                    
                    row[r].remove(c)
                    col[c].remove(r)

            step+=1
            
        return -1
```

今天才見識到sorted list的真正威力。  
如果要找出一個閉區間[s,e]內的所有元素，可以使用irange(min,max)方法，會回傳一個疊代器。  

```python
t=[]
for x in sl.irange(s,e):
    t.append(x)
    # do something...
for x in t:
    sl.remove(x)
```

但是要同時刪除這些元素的話，必須另外儲存，等到疊代完後再刪除；或是直接把疊代器轉成list，這樣就不會噴錯了。  

```python
for x in list(sl.irange(s,e));
    sl.remove(x)
    # do something...
```