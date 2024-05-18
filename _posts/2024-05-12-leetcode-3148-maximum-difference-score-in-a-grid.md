---
layout      : single
title       : LeetCode 3148. Maximum Difference Score in a Grid
tags        : LeetCode Medium Array Matrix DP
---
周賽 397。

## 題目

輸入 m \* n 的正整數矩陣 grid。  
你可以從一個格子移動正下方或是正右方的**任意**格子。  
從值為 c1 的格子移動到值為 c2 的格子，將獲得 c2 - c1 分。  

你可以從**任意**格子出發，且移動**至少一次**。  

求可獲得的**最大分數**。  

## 解法

可以往右或往下走，換句話說，每個格子只能**從上**或**從左**走來。  
問題轉換成：枚舉所有格子做為終點，找到**最大分數**。  
不同的格子可能經過同一個格子，有重疊子問題，考慮 dp。  

定義 dp(r, c)：以格子 (r, c) 為終點的最大分數。  
轉移：dp(r, c) = max(上方, 左方)  

- 上方 = max(dp(r0, c) + grid[r][c] - grid[r0][c] ) FOR ALL 0 <= r0 < r  
- 上左 = max(dp(r, c0) + grid[r][c] - grid[r][c0] ) FOR ALL 0 <= c0 < c  
base：dp(0, 0) 沒有轉移來源，不能做為終點，答案為 -inf。  

---

但是每次一個格子的轉移來源有 M + N 個，總共有 MN 個格子要計算。  
複雜度高達 O(MN * (M + N))，要想辦法優化。  

每當從格子 (r, c) 轉移到下一個格子時，會對下個格子的分數貢獻 dp(r, c) - grid[r][c]，然後再加上下一個格子的值。  
我們不在乎到底是從哪個格子轉移而來，只在乎誰**貢獻最高**。  
因此計算出 dp(r, c) 之後，以 (r, c) 當作新的轉移來源，更新**同行列的最大值**，以供後續其他格子使用。  

維護陣列 rmax, cmax 分別代表各行列的最大轉移來源。  
轉移： dp(r, c) = max(rmax[r], cmax[c]) + grid[r][c]  

注意：以 (r, c) 更新轉移來源時，**可以當作新的起點**，所以更新時要取 max(0, dp[r][c]) - grid[r][c]。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0] * N for _ in range(M)]
        rmax = [-inf] * M
        cmax = [-inf] * N
        ans = -inf
        for r in range(M):
            for c in range(N):
                dp[r][c] = max(rmax[r], cmax[c]) + grid[r][c]
                ans = max(ans, dp[r][c])
                rmax[r] = max(rmax[r], max(0, dp[r][c]) - grid[r][c])
                cmax[c] = max(cmax[c], max(0, dp[r][c]) - grid[r][c])
                
        return ans
```

試想移動的路徑的值分別為為 [a, b, c, d]，那麼最終分數是 (b - a) + (c - b) + (d - c)。  
結果中間的部分都消掉了，最後變成 d - a。  
問題轉換成：對於每個格子，從左上方向選擇任一出發點。  

枚舉所有格子作為終點，並更新答案最大值。  
注意：出發點不可等於當前格子，必須先計算答案後才更新最小值。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0] * N for _ in range(M)]
        ans = -inf
        for r in range(M):
            for c in range(N):
                up = dp[r - 1][c] if r > 0 else inf
                left = dp[r][c - 1] if c > 0 else inf
                # update answer
                ans = max(ans, grid[r][c] - min(up, left))
                # then update min
                dp[r][c] = min(up, left, grid[r][c])
                
        return ans
```
