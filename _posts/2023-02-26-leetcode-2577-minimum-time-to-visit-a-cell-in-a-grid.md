--- 
layout      : single
title       : LeetCode 2577. Minimum Time to Visit a Cell In a Grid
tags        : LeetCode Hard Array Matrix Graph Heap
---
周賽334。算差值的公式改半天，時間結束後才AC，好氣。  

# 題目
輸入由**非負整數**所組成的m\*n的矩陣grid。其中grid[row][col]代表可以抵達格子(row, col)的最早時間，代表你只能在**大於等於**grid[row][col]的時間抵達格子(row, col)。  

第0秒時，你從最左上角格子出發。你**必須移動**至上下左右**任意**一個相鄰的格子(不可停留)，每次移動耗時1秒鐘。  

求抵達最右下角的**最早**時間。若無法抵達則回傳-1。  

# 解法
先過濾掉唯一一種無法抵達的狀況：起點的右邊和下面一格都不為1。除此以外的狀況，都可以透過來回移動來等待新的路徑出現。  

如果使用普通的bfs，無法處理來回移動這種操作，因為會造成大量的重複計算。所以改成直接計算出相鄰格子的**最早抵達時間**，也就是需要來回移動幾次。  

有了每個格子的**最早抵達時間**，就可以透過djikstra最短路徑演算法，依照最小的時間順序來處理各個路徑，如果抵達右下角直接回傳當前時間。  

當時間為t，前往相鄰格子的情形有兩種，分類討論一下：  
- 移動後時間為t+1，而相鄰的格子值小於等於t+1，則抵達時間為t+1  
- 若格子值大於t+1，則需要先在原地來回走若干次。抵達時間為t+1+來回步數  

時間複雜度O(MN log MN)。空間複雜度O(MN)。  

```python
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        
        M,N=len(grid),len(grid[0])
        vis=[[False]*N for _ in range(M)]
        h=[[0,0,0]] # time, row, col
        
        while True:
            t,r,c=heappop(h)
            if vis[r][c]:continue
            if r==M-1 and c==N-1:return t
            vis[r][c]=True
            for dx,dy in zip([1,0,-1,0],[0,1,0,-1]):
                rr,cc=r+dx,c+dy
                if 0<=rr<M and 0<=cc<N and not vis[rr][cc]:
                    if t+1>=grid[rr][cc]:
                        heappush(h,[t+1,rr,cc])
                    else:
                        need=(grid[rr][cc]-(t+1))
                        if need&1:
                            need+=1
                        heappush(h,[t+1+need,rr,cc])
```
