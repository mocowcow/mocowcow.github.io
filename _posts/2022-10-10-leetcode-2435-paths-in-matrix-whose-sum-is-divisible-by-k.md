--- 
layout      : single
title       : LeetCode 2435. Paths in Matrix Whose Sum Is Divisible by K
tags        : LeetCode Hard Array Medium DP
---
周賽314。非常標準的路徑計數dp題，又是一次開心的周賽通關。  

# 題目
輸入m\*n的整數矩陣grid和整數k。你從(0,0)出發，想要前往(M-1,N-1)，且只能向下或向右移動。  

求路徑上元素總和可被k整除的路徑數。答案很大，先模10^9+7後回傳。  

# 解法
每個位置只能向下或向右走；換句話說，每個格子只能由上方或左方走來。  
而路徑和必需被k整除，意味著我們依照路徑和對k取餘數來分類，只有餘數為0者可以被k整除。  

定義dp(r,c)：從(0,0)出發，抵達(r,c)的所有路徑中，0\~k-1為餘數的的路徑各有幾種。回傳長度為k的陣列代表各路徑數。  
轉移方程式：dp(r,c)[i]代表餘數為i的路徑，v代表當前位置值加上來源餘數後重新取餘，則dp(r,c)[v]=dp(r,c)[i]+dp(r,c)[i]，其中0<=i<k。  
base cases：若r或c小於0則超出矩陣邊界，回傳長度為k的空陣列；若位於起點(r,c)，則直接在起點值的餘數dp(0,0)[v]初始為1後回傳。  

矩陣長度為M，寬度為N，共有M\*N種狀態，每次計算需k次轉移，時空間複雜度皆為O(M\*N\*k)。  

```python
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD=10**9+7
        M,N=len(grid),len(grid[0])
        
        @cache
        def dp(r,c):
            ans=[0]*k
            if r<0 or c<0:
                return ans
            if r==c==0:
                v=grid[0][0]%k
                ans[v]=1
                return ans
            up=dp(r-1,c)
            left=dp(r,c-1)
            for i in range(k):
                v=(grid[r][c]+i)%k
                ans[v]=(up[i]+left[i])%MOD
            return ans
        
        return dp(M-1,N-1)[0]
```
