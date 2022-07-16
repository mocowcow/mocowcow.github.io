--- 
layout      : single
title       : LeetCode 576. Out of Boundary Paths
tags        : LeetCode Medium DP
---
每日題。好久以前曾經做過，但是今天發現完全不同的觀點。  

# 題目
輸入m*n的矩陣grid。有一顆球位於[startRow, startColumn]。你可以將球移動到grid中相鄰的四個方格(有可能超出邊界)，且最多進行maxMove次移動。  
求將球移出邊界的路徑數量。答案可能很大，需模10^9+7後回傳。

# 解法
以前我是逆向思考，計算有多少種方法能夠從邊界外面抵達某格子。  
每一格(r,c)能夠能夠從四方向走過來，如果旁邊是邊界則路徑+1，否則加上邊界現有的路徑數。  
最後回傳dp[startRow, startColumn]的路徑數即可。  

```python
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD=10**9+7
        dp=[[0]*n for _ in range(m)]
        
        for _ in range(maxMove):
            t=[[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    up=1 if r==0 else dp[r-1][c]
                    down=1 if r==m-1 else dp[r+1][c]
                    left=1 if c==0 else dp[r][c-1]
                    right=1 if c==n-1 else dp[r][c+1]
                    t[r][c]=(up+down+left+right)%MOD
            dp=t
            
        return dp[startRow][startColumn]
```

或是順著題意，從(startRow, startColumn)出發，每次試著向四周相鄰的格子加上當前的路徑數；若是與邊界相鄰，則在答案加上當前路徑數。  
這種方法比較好想到，但是寫起來感覺就比較醜，兩種各有利弊，時間複雜度都是O(m\*n\*maxMove)，空間可壓縮至O(m\*n)。  

```python
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD=10**9+7
        ans=0
        dp=[[0]*n for _ in range(m)]
        dp[startRow][startColumn]=1
        
        for i in range(maxMove):
            t=[[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    for dx,dy in zip([1,0,-1,0],[0,1,0,-1]):
                        rr=r+dx
                        cc=c+dy
                        if not(0<=rr<m and 0<=cc<n):
                            ans=(ans+dp[r][c])%MOD
                        else:
                            t[rr][cc]=(t[rr][cc]+dp[r][c])%MOD
            dp=t            
 
        return ans
```