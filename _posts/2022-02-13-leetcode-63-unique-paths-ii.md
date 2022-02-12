---
layout      : single
title       : LeetCode 63. Unique Paths II
tags 		: LeetCode
---
DP教學系列。多加障礙物，難度沒有提升多少。

# 題目
輸入M*N的矩陣，0代表可通行，1代表障礙物。從左上角出發，每次移動只能往右或是往下走，有障礙的地方不能走，求走到右下角有多少種路線。

# 解法

>步驟1：定義狀態  

影響的變數有x,y軸，需要二維DP。  
dp[r][c]代表在(r,c)到達位置路線數。

>步驟2：找出狀態轉移方程式  

只能往右或下走，換個說法就是每個位置只能由上方或是左方過來。  
到達(r,c)的路線=到達上方路線+到達左方路線，且(r,c)位不可有障礙，只有在不為障礙時才更新，dp[r][c]=dp[r-1][c]+dp[r][c-1]。

>步驟3：處理base cases

如果在r=0或是c=0的時理應為1，但如果出現障礙的話，之後的路線就不可能通行了。  
從起點分別往右及往下掃，遇到障礙物就中斷初始化迴圈，否則值設為1。

雖然這題也可以壓縮成一維空間，但程式碼可能會有點醜，還是不壓了。

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*N for _ in range(M)]
        # init first row
        for i in range(N):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        # init first col
        for i in range(M):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for r in range(1, M):
            for c in range(1, N):
                if obstacleGrid[r][c] != 1:
                    dp[r][c] = dp[r-1][c]+dp[r][c-1]

        return dp[-1][-1]
```
