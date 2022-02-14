---
layout      : single
title       : LeetCode 1289. Minimum Falling Path Sum II
tags 		: LeetCode Hard DP Matrix Array
---
[這題](https://leetcode.com/problems/minimum-falling-path-sum/)的變種版本，Hard難度似乎有點過譽。

# 題目
輸入N*N的整數矩陣grid，元素代表走到該位置的成本。從第一列任意欄出發往下走，可以選擇走下一列除正下方的任一格，求走到最底的最低成本是多少。

# 解法

>步驟1：定義狀態  

影響的變數有x,y軸，需要二維DP。  
dp[r][c]代表在(r,c)到達位置的最小成本。

>步驟2：找出狀態轉移方程式  

說是不能往正下一格走，反過來說就是上一列任一個都可以是來源。  
到達(r,c)的最小成本為上一列中除了正上方的最小成本，dp[r][c]=min(dp[r-1][x] FOR ALL 0<=x<N且x!=c)+grid[r][c]。

>步驟3：處理base cases

r=0時都是起點，直接初始化dp[0]=grid[0]。

在DP轉移關係中，可以把邏輯簡化，把上一次DP結果排序，只記錄最小和次小值，在每個(r,c)時檢查(r-1,c)是否和最小值相等，若是則表示該最小值提供者是正上方，所以只能使用次小值。  
這題也一樣因為只會參考到上一列的結果，所以也可以把空間壓縮到一維。

```python
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = grid[0]

        for r in range(1, N):
            t = [0]*N
            for c in range(N):
                mn1, mn2 = sorted(dp)[0:2]
                if mn1 == dp[c]:
                    t[c] = grid[r][c]+mn2
                else:
                    t[c] = grid[r][c]+mn1
            dp = t

        return min(dp)
```
