--- 
layout      : single
title       : LeetCode 2596. Check Knight Tour Configuration
tags        : LeetCode Medium Array Matrix Simulation
---
周賽337。這題有點小心機，不少人都中計，包括我。  

# 題目
There is a knight on an n x n chessboard. In a valid configuration, the knight starts at the top-left cell of the board and visits every cell on the board exactly once.

You are given an n x n integer matrix grid consisting of distinct integers from the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col) is the grid[row][col]th cell that the knight visited. The moves are 0-indexed.

Return true if grid represents a valid configuration of the knight's movements or false otherwise.

Note that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.

有個n\*n的棋盤。做為一個合法的配置，騎士應由**左上角出發**，且走訪每個格子**各一次**。  

輸入n\*n的整數矩陣grid，由不重複的整數[0, n\*n-1]所組成，其中grid[row][col]的值代表騎士抵達(row, col)的順序。  

若此配置合法則回傳true，否則回傳false。  

注意：騎士只能走水平1格+垂直2格，或是水平2格+垂直1格。  

# 解法
維護N\*N的陣列step，其中step[i]代表第i步抵達的位置，遍歷grid把位置填入。  

騎士必須從左上角出發，但是測資並沒有保證一定在左上角，所以要自己檢查！  
並且依序遍歷每一步移動的距離變化[dx,dy]必定屬於[2,1]或是[1,2]，否則不是合法的移動方式，直接回傳false。  

時間複雜度O(N^2)。空間複雜度O(N^2)。  

```python
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        N=len(grid)
        step=[None]*(N*N)
        
        for r in range(N):
            for c in range(N):
                step[grid[r][c]]=[r,c]
                
        if step[0]!=[0,0]:
            return False
        
        for prev,curr in pairwise(step):
            diff=[abs(prev[0]-curr[0]),abs(prev[1]-curr[1])]
            if diff not in [[1,2],[2,1]]:
                return False
            
        return True
```

或是不用絕對值處理移動量，直接把dx和dy平方，總和必定為5。  

```python
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        N=len(grid)
        step=[None]*(N*N)
        
        for r in range(N):
            for c in range(N):
                step[grid[r][c]]=[r,c]
                
        if step[0]!=[0,0]:
            return False
        
        for prev,curr in pairwise(step):
            dx=prev[0]-curr[0]
            dy=prev[1]-curr[1]
            if dx*dx+dy*dy!=5:
                return False
            
        return True
```