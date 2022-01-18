---
layout      : single
title       : LeetCode 1463. Cherry Pickup II
tags 		: LeetCode
---
# 題目
給一個矩陣，每格的值代表櫻桃數量，有兩個機器人分別從左上、右上角出發，求最多可以拿到多少櫻桃。  
機器人每次移動只能往左下、正下或是右下移動。

# 解法
當初一直以為需要走兩趟，想半天也不知第二號機器人如何確認格子是否被一號機器人走過，
看提示才驚覺可以同時表示兩機器人的位置。  
採top-down方式由第一列往下走，遞迴求下一層的最佳解。

```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        @lru_cache(None)
        def dp(r, c1, c2):
            if c1 < 0 or c2 < 0 or c1 >= N or c2 >= N:
                return -math.inf
            cherry = grid[r][c1]
            if c1 != c2:
                cherry += grid[r][c2]
            best = 0
            # enumerate all combs if has more row
            if r < M-1:
                for i in range(c1-1, c1+2):  # [c1-1, c1, c1+1]
                    for j in range(c2-1, c2+2):  # [c2-1, c2, c2+1]
                        best = max(best, dp(r+1, i, j))

            return cherry+best

        return dp(0, 0, N-1)
```
