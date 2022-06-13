--- 
layout      : single
title       : LeetCode 2304. Minimum Path Cost in a Grid
tags        : LeetCode Medium Array Matrix DP
---
周賽297。這題描述有夠雜的，看了半天才搞懂他想搞什麼，難怪AC人數增加超慢。

# 題目
輸入索引從0開始的m*n整數矩陣grid，其中格子的值分別為0\~m\*n-1的不同整數組成。你可以從每列中的所有位置移動到下一列的任意位置。注意，最後一列無法移動。  
另外還有索引從0開始的(m\*n)\*n的二維陣列moveCost，其中moveCost[i][j]代表從值為i的位置移動到下一列第j行格子的成本。從最後一列格子的成本可以忽略不管。  

**路徑成本**是所有訪問過的格子值加上移動成本的總和。求從第一列任意位置出發，抵達最後一列任意位置的最小路徑成本。  

# 解法
個人認為把每個**格子的值**改稱為**格子的編號**更加容易理解。  
而每個格子的路徑成本，就是**來源編號+來源到當前的移動成本+當前編號**。  

定義dp[r][c]為：抵達grid[r][c]的最小路徑成本。  
轉移方程式：dp[r][c]=min(來源編號+來源到當前的移動成本+當前編號)  
base case：當r=0時，都是起點，沒有來源，成本即為其編號。  

從最上方開始往下DP，列舉每個位置作為來源，更新目標位置的最低成本。因為每個格子可以走到下一列N個格子，時間複雜度為O(M\*N^2)。 

```python
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        dp=[[inf]*N for _ in range(M)]
        dp[0]=grid[0]
        
        for r in range(M-1):
            for c in range(N):
                curr=grid[r][c]
                for k in range(N):
                    dp[r+1][k]=min(dp[r+1][k],dp[r][c]+grid[r+1][k]+moveCost[curr][k])
        
        return min(dp[-1])
```
