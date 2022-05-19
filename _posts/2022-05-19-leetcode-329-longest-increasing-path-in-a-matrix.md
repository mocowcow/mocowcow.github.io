--- 
layout      : single
title       : LeetCode 329. Longest Increasing Path in a Matrix
tags        : LeetCode Hard Graph Matrix DFS DP BFS TopologySort
---
每日題。過了半年後，竟然想到和之前不同的解法，代表有進步。

# 題目
輸入m*n的矩陣matrix，回傳matrix中最長遞增路徑的長度。
在每個位置，你可以往上下左右四個方向移動，但不可以是斜角移動，或是超出邊界。

# 解法
題目雖然只說遞增路徑，但根據例題，下一步的位置一定要大於當前位置，實際上是**嚴格遞增**。  

假設我們在某個位置(r,c)=5，其四周只有一個較大的格子6，而從(r,c)出發的最長路徑一定包含6，可以看出遞迴的關係式。  
定義dp(r,c)：從(r,c)出發，可以得到的最長遞增路徑長度。  
轉移方程式：dp(r,c)=1+max(dfs(nr,nc)) WHERE (nr,nc)位於(r,c)四周 且matrix[r][c]<matrix[nr][nc]  
base case：四周沒有更大的值，長度為1。  

試著對從matrix中每個位置出發做dfs，若獲得更大的長度，則更新ans。

```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M,N=len(matrix),len(matrix[0])
        ans=1
        
        @lru_cache(None)
        def dfs(r,c):
            step=1
            for nr,nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if (0<=nr<M and 0<=nc<N) and matrix[nr][nc]>matrix[r][c]:
                    step=max(step,dfs(nr,nc)+1)
            return step
        
        for r in range(M):
            for c in range(N):
                ans=max(ans,dfs(r,c))
                
        return ans
```

也可以以拓樸排序的角度來分析。  
因為每個格子可以藉由四周較小的格子抵達，所以我們必須選擇從**沒有入口的點**出發，往其他高處走，並將抵達處的**入口數**扣掉1。如果該點入口處變成0了，就可以繼續從那邊前往其他點。  
這邊所說的**入口數**，術語就叫做**入度(indegree)**。  

```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M,N=len(matrix),len(matrix[0])
        indegree=defaultdict(int)
        q=deque()
        step=0

        for r in range(M):
            for c in range(N):
                for nr,nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                    if (0<=nr<M and 0<=nc<N) and matrix[nr][nc]>matrix[r][c]:
                        indegree[(nr,nc)]+=1

        for r in range(M):
            for c in range(N):
                if indegree[(r,c)]==0:
                    q.append((r,c))

        while q:
            step+=1
            for _ in range(len(q)):
                r,c=q.popleft()
                for nr,nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                    if (0<=nr<M and 0<=nc<N) and matrix[nr][nc]>matrix[r][c]:
                        indegree[(nr,nc)]-=1
                        if indegree[(nr,nc)]==0:
                            q.append((nr,nc))

        return step
```