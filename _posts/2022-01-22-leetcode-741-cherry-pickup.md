---
layout      : single
title       : LeetCode 741. Cherry Pickup
tags 		: LeetCode Hard DP
---
# 題目
N*N的矩陣，0表示空格位，1表示櫻桃，-1是障礙不可過。  
先從左上角出發，只能往下或是往右走，到達右下角後，再走回起點，只能往左或往上。  
每顆櫻桃只能拿一次，求最多可收集多少櫻桃。

# 解法
有個非常重要的關鍵：一趟來回路程，其實和兩趟單程路程是相同意思，而且先後順序並不影響結果。那麼把問題簡化成從起點往下走兩次就很清楚了。  
起點為(0,0)，若經過m次移動，則m=r1+c1=r2+c2，通過移項得r1+c1-c2=r2，可省略一個參數。  
base case為右下角落，直接回傳是否有櫻桃；否則回傳當回合櫻桃+下回合最佳解。

```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)

        @lru_cache(None)
        def dp(r, c1, c2):
            r2 = r+c1-c2
            if c1 >= N or c2 >= N or r == N or r2 == N or grid[r][c1] == -1 or grid[r2][c2] == -1:
                return -math.inf
            if r == c1 == N-1:  # right bottom
                return grid[-1][-1]
            cherry = grid[r][c1]
            if c1 != c2:
                cherry += grid[r2][c2]
            best = max(dp(r+1, c1, c2),  # down, down
                       dp(r+1, c1, c2+1),  # down, right
                       dp(r, c1+1, c2+1),  # right, right
                       dp(r, c1+1, c2))  # right, down
            return cherry+best

        return max(dp(0, 0, 0), 0)
```
