---
layout      : single
title       : LeetCode 931. Minimum Falling Path Sum
tags 		: LeetCode Medium DP Matrix Array 
---
DP教學系列。總覺得這些計數型DP應該放到教學前半段，畢竟相對容易理解，不然前面的題目有些太噁心了。

# 題目
輸入N*N的整數矩陣matrix，元素代表走到該位置的成本。從第一列任意欄出發往下走，每次可以走左下、正下或是右下方，求走到最底的最低成本是多少。

# 解法

>步驟1：定義狀態  

影響的變數有x,y軸，需要二維DP。  
dp[r][c]代表在(r,c)到達位置的最小成本。

>步驟2：找出狀態轉移方程式  

只能往左下、正下或右下走，換個說法就是每個位置只能由左上、正上或是右上過來。  
到達(r,c)的最小成本為三個來源中最取最小+當前成本，dp[r][c]=min(左上,正上,右上)+matrix[r][c]。

>步驟3：處理base cases

r=0可以從任意地點出發，dp[0][c]直接和matrix[0][c]同值。  
r>0時，且c=0或是(N-1)時會缺少一個來源，來源直接設成最大，避免被計入。

因為每次計算只會用到上一次的結果，所以只要保留上一行的DP就好，空間可以壓到一維。

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        dp = [0]*N

        for r in range(N):
            t = [0]*N
            for c in range(N):
                left = math.inf if c == 0 else dp[c-1]
                mid = dp[c]
                right = math.inf if c == N-1 else dp[c+1]
                t[c] = min(left, mid, right) + matrix[r][c]
            dp = t

        return min(dp)
```
