---
layout      : single
title       : LeetCode 3393. Count Paths With the Given XOR Value
tags        : LeetCode Medium Matrix BitManipulation DP 
---
biweekly contest 146。

## 題目

輸入 m x n 二維整數陣列 grid，還有整數 k。  

你的目標是計算從左上格子 (0, 0) 出發到右下格子 (m - 1, n - 1)，且滿足條件的路徑數：  

- 當你位於 (i, j) 時，可以往右或往下走，即 (i, j + 1) 或 (i + 1, j)。  
- 路徑中所有數字的 XOR 值必須等於 k。  

求有多少滿足條件的路徑。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

相似題 [62. unique paths]({% post_url 2022-02-12-leetcode-62-unique-paths %})。  
只是多一個路徑的 XOR 值限制。  

定義 dp(i, j, val)：當前 XOR 值為 val，從 (i, j) 走到右下角的合法路徑數。  
轉移：dp(i, j, val) = dp(i+1, j, val^grid[i+1][j]) + dp(i, j+1, val^grid[i][j+1])。  
base：當 (i, j) 等於 (m-1, n-1) 時，若 val 正好為 k，則有合法方案數 1；否則為 0。  

時間複雜度 O(M \* N \* MX)，其中 MX = 最大 XOR 值。  
空間複雜度 O(M \* N \* MX)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])

        @cache
        def dp(i, j, val):
            if i == M-1 and j == N-1:
                return int(val == k)

            res = 0
            if i+1 < M:
                res = dp(i+1, j, val ^ grid[i+1][j])
            if j+1 < N:
                res += dp(i, j+1, val ^ grid[i][j+1])
            return res % MOD

        return dp(0, 0, grid[0][0])
```

注意本題保證 k 小於 16，也就是最大 15 = 0b1111。  
不超過 15 的數互相 XOR 也只會在 [0, 15] 的範圍內，因此遞推參數要開 16 格。  

但如果 k 的最大值二進制不完全是 1 位元，做完 XOR 後很有可能超過 k。例如：  
> k 上限 2  
> 1 XOR 2 = 3  

因此大小 MX 應該是取決於 k 與 grid 內元素的最大位元長度 bit_len，把每個位都設為 1，也就是 2^bitlen 格。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])

        mx = k
        for row in grid:
            for x in row:
                if x > mx:
                    mx = x

        MX = 1 << mx.bit_length()
        f = [[[0] * MX for _ in range(N)] for _ in range(M)]
        f[M-1][N-1][k] = 1

        for i in reversed(range(M)):
            for j in reversed(range(N)):
                if i == M-1 and j == N-1:
                    continue
                for val in range(MX):
                    res = 0
                    if i+1 < M:
                        res = f[i+1][j][val ^ grid[i+1][j]]
                    if j+1 < N:
                        res += f[i][j+1][val ^ grid[i][j+1]]
                    f[i][j][val] = res % MOD

        return f[0][0][grid[0][0]]
```
