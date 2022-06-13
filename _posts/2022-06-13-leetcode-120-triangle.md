--- 
layout      : single
title       : LeetCode 120. Triangle
tags        : LeetCode Medium Array DP
---
每日題。這題如果按照題意往下走會很麻煩，換個方向會簡單非常多。  

# 題目
輸入二維triangle。回傳從最上方走到最下方的最小路徑總和。  
當你位於索引i，每次向下走可以選擇走到下一列的第i或是i+1個位置。  

# 解法
這個三角形總共有N列，第0列有1個元素，第1列有2個元素，以此類推。  
為了方便起見，建立N*N的陣列dp，初始化為inf，代表不合法的位置。然後把三角形第一列的元素填入dp[0][0]。  
每次從i向下可以選擇i或是i+1，換句話說，i有可能是從上一列的i或是i-1走過來的。但是除了i=0時，只能從i來。  

定義dp[r][c]：抵達triangle[r][c]的最小路徑總和。  
轉移方程式dp[r][c]=min(dp[r-1][c],dp[r-1][c-1])+triangle[r][c]  
base cases：dp[0][0]為起點，直接設為triangle[0][0]的值。對於其他列c=0時，直接選用dp[r-1][c]。  

計算出每個位置的最小路徑總和後，因為走到最下方任一格都可以，所以回傳dp[-1]中最小值。  

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N=len(triangle)
        dp=[[inf]*N for _ in range(N)]
        dp[0][0]=triangle[0][0]
        
        for r in range(1,N):
            for c in range(r+1):
                if c==0:
                    dp[r][c]=dp[r-1][c]+triangle[r][c]
                else:
                    dp[r][c]=min(dp[r-1][c],dp[r-1][c-1])+triangle[r][c]

        return min(dp[-1])
```



```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N=len(triangle)
        
        for r in range(N-2,-1,-1):
            for c in range(r+1):
                triangle[r][c]+=min(triangle[r+1][c],triangle[r+1][c+1])
                
        return triangle[0][0]
```
