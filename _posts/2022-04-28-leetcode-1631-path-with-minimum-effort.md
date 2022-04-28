--- 
layout      : single
title       : LeetCode 1631. Path With Minimum Effort
tags        : LeetCode Medium Array Matrix Heap BFS
---
每日題。開始覺得這陣子團隊是要搞併查集系列，但說實話這題真的不太適合用併查集，硬要用也沒什麼意思。

# 題目
你是一個登山者，要找一條最**努力值**要求最小的路徑。  
輸入M*N的矩陣heights，而heights[r][c]代表該位置的高度。你從最左上角出發，目的地是最右下角，可以往上下左右任意移動。  
而一條路徑的**努力值**，是所經路上兩個相鄰位置高度的最大絕對差，例如路徑高度為[1,5,6]，努力值為abs(5-1)=4。

# 解法
這題不是求最短路徑，BFS不能用，DFS亂走一定會超時，想了快半小時才領悟要用heap。  
有點像是djikstra的變形，原本是先走最短的路徑，這邊改成先走努力值最小的路徑。  
visited矩陣紀錄各位置是否已經處理過，初始化將(0,0,0)加入heap中，代表(r,c,最大努力值)，開始變種djikstra：  
1. 找到沒有處理過的點r,c及最大努力值ef  
2. 如果剛好是終點，回傳ef  
3. 標記(r,c)為已處理，對四周的有效位置更新最大努力值，並加入heap中  

```python
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        M,N=len(heights),len(heights[0])
        endx,endy=M-1,N-1
        visited=[[False]*N for _ in range(M)]
        h=[(0,0,0)] # r, c, max effort
        while h:
            ef,r,c=heappop(h)
            if visited[r][c]:
                continue
            if r==endx and c==endy:
                return ef
            visited[r][c]=True
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < M and 0 <= nc < N:
                    nef=abs(heights[r][c]-heights[nr][nc])
                    nef=max(nef,ef)
                    heappush(h,(nef,nr,nc))
```
