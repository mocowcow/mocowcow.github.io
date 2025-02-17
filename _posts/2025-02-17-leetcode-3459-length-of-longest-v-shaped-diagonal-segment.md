---
layout      : single
title       : LeetCode 3459. Length of Longest V-Shaped Diagonal Segment
tags        : LeetCode Hard Matrix DP
---
weekly contest 437。  
比 Q3 還簡單的 Q4。  
可惜我被 Q3 卡死根本沒看這題。  

## 題目

<https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/description/>

## 解法

其實就是求最長路徑。有以下限制：  

- 路徑是斜的  
- 第一格是元素 1  
- 之後元素是 2,0,2,0,.. 交替  
- **至多**可右轉一次 (也可不轉)

---

兩條不同路徑右轉後可能走到相同路徑上，有**重疊的子問題**，考慮 dp。  
定義 dp(i, j, dir, is_turned, target)：從 (i, j) 出發，方向為 dir 的最長路徑。  
is_turned = False/True 代表是否已右轉過；限制 grid[i][j] = target。  

枚舉所有 grid[i][j] = 1 為起點，再枚舉四個方向，直接從下一步的位置開始 dp，即可保證路徑中只有 2,0 交替。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

```python
DIRS = [[-1, 1], [1, 1], [1, -1], [-1, -1]]


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        @cache
        def dp(i, j, dir, is_turned, target):
            if not (0 <= i < M and 0 <= j < N):
                return 0
            if grid[i][j] != target:
                return 0

            dx, dy = DIRS[dir]
            res = dp(i+dx, j+dy, dir, is_turned, 2-target)
            if not is_turned:
                dir = (dir+1) % 4
                dx, dy = DIRS[dir]
            res = max(res, dp(i+dx, j+dy, dir, True, 2-target))
            return res + 1

        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    for dir in range(4):
                        dx, dy = DIRS[dir]
                        ans = max(ans, dp(i+dx, j+dy, dir, False, 2) + 1)

        return ans
```
