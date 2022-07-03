--- 
layout      : single
title       : LeetCode 2328. Number of Increasing Paths in a Grid
tags        : LeetCode Hard Array Matrix DFS DP
---
周賽300。這Q4比Q3還簡單，從開始到AC也才花8分鐘，解完整個信心又恢復，衝回去把Q3解完。

# 題目
輸入m*n整數矩陣grid，你可以從任何格子移動到其四周相鄰的其他格子。  
你可以從任意格子出發和結尾，求grid中有多少**嚴格遞增路徑**，答案很大，模10^9+7後回傳。  

若兩條路徑順序沒有完全相同，則視為是不同的。  

# 解法
每個位置的結尾數量，相依於其值嚴格低於本身的相鄰格子。  

定義dp(r,c)：以(r,c)結尾的嚴格上升路徑數量。  
轉移方程式：dp(r,c)=1+sum(dp(rr,cc) FOR ALL grid[rr][cc]<grid[r][c])  
base case：四周格子都比當前大，只能自己出發自己結尾，路徑數1。  

最後列舉所有格子(r,c)，並將其結尾的路徑數加到ans中。  

```python
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        MOD=10**9+7
        ans=0
        
        @cache
        def dfs(r,c):
            cnt=1
            for dx,dy in zip([1,0,-1,0],[0,1,0,-1]):
                rr=r+dx
                cc=c+dy
                if (0<=rr<M and 0<=cc<N) and grid[rr][cc]<grid[r][c]:
                    cnt+=dfs(rr,cc)
            return cnt%MOD
        
        for r in range(M):
            for c in range(N):
                ans=(ans+dfs(r,c))%MOD
                
        return ans
```
