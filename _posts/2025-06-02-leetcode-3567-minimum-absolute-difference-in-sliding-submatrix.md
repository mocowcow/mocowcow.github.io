---
layout      : single
title       : LeetCode 3567. Minimum Absolute Difference in Sliding Submatrix
tags        : LeetCode Medium Simulation Sorting
---
weekly contest 452。

## 題目

<https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/description/>

## 解法

矩陣大小 N = 30，暴力枚舉所有 k\*k 子矩陣，去重排序後判斷絕對差。  
注意有個小坑點：若矩陣中元素都相同，則答案為 0。  

有 (N-k+1) \* (M-k+1) 個子矩陣。  
子矩陣有 k^2 個元素需要排序。  

時間複雜度 O((N-k+1) \* (M-k+1) \* k^2 log k)。  
空間複雜度 O(k^2)。  

```python
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])

        ans = [[0]*(N-k+1) for _ in range(M-k+1)]
        for r in range(M-k+1):
            for c in range(N-k+1):
                s = set()
                for i in range(r, r+k):
                    for j in range(c, c+k):
                        s.add(grid[i][j])
                if len(s) > 1:
                    ans[r][c] = min(y-x for x, y in pairwise(sorted(s)))

        return ans
```
