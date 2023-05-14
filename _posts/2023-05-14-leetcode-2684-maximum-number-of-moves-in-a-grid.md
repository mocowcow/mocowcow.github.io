--- 
layout      : single
title       : LeetCode 2684. Maximum Number of Moves in a Grid
tags        : LeetCode Medium Array Matrix DP DFS
---
周賽345。有點小陷阱，不只從左上角出發，而是可以從第一列的任意行出發。  

# 題目
輸入M\*N的正整數矩陣grid。  

你可以從**任意**列數的第一行出發，並遵循以下規則遍歷grid：  
- 位於格子(row, col)，你可以前往(row+1, col+1)、(row, col+1)或(row-1, col+1)，但目標格子中的值必須**嚴格大於**當前格子值  

求**最大移動次數**。  

# 解法
簡單說就是可以往右上、右或是右下方，大於當前格子的方向移動。  

定義dp(r,c)：位於(r,c)時，可以移動的最大次數。  
轉移方程式：dp(r,c) = max( dp(rr,c+1)+1 FOR ALL 0<=rr<M 且 r-1<=rr<=r+1 且 grid[r][c]<grid[rr][c+1])；若無法移動則為0。  
base case：當c等於N-1時，已經位於最後一行，無法繼續移動，直接回傳1。  

窮舉每一列的第0行作為起點，步數最大者就是答案。  

時間複雜度O(MN)。  
空間複雜度O(MN)。  

```python
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        
        @cache
        def dp(r,c):
            if c==N-1: 
                return 0
            step=0
            for rr in [r-1,r,r+1]:
                if 0<=rr<M and grid[r][c]<grid[rr][c+1]: 
                    step=max(step,dp(rr,c+1)+1)  
            return step
        
        ans=0
        for r in range(M):
            ans=max(ans,dp(r,0))
            
        return ans
```
