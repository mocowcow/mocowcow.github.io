---
layout      : single
title       : LeetCode 3418. Maximum Amount of Money Robot Can Earn
tags        : LeetCode Medium DP
---
weekly contest 432。  
現在連 Q2 都有 dp，難度提高不少。  

## 題目

輸入 m x n 的矩陣 coins。  
有個機器人從左上角 (0, 0) 出發，前往右下角 (m - 1, n - 1)。  
機器人每次移動只能向下或向右走。  

矩陣中每個格子 coins[i][j] 都有一個值：  

- 若 coins[i][j] >= 0，機器人獲得該值的金幣。  
- 若 coins[i][j] < 0，機器人碰到搶匪，損失該值**絕對值**的金幣。  

機器人有特殊技能，可以**感化最多 2 個**搶匪，避免當次損失。  

求機器人在路徑上可得的最大金幣數。  
注意：總金幣數可以是負數。  

## 解法

相似題 [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)。  
差別在於本題可出現負數，且有兩次機會不拿負數。  
多加一個狀態表示可不拿的次數。  

---

定義 dp(i, j, k)：從 (i, j) 走到 (m-1, n-1)，至多 k 格不選的最大路徑和。  
轉移：dp(i, j, k) = max(選+往下, 選+往右, 不選+往下, 不選+往右)。  

- 選：coins[i][j] + max(dp(i+1, j, k), dp(i, j+1, k))。  
- 滿足 coins[i][j] < 0 且 k > 0 可不選：max(dp(i+1, j, k-1), dp(i, j+1, k-1))。  

base：

- 當 i = M 或 j = N 出界，無效範圍回傳 -inf。  
- 當 i = M-1 且 j = N-1，若 coins[i][j] 為負且 k > 0，回傳 0；否則回傳 coins[i][j]。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

```python
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        M, N = len(coins), len(coins[0])

        @cache
        def dp(i, j, k):
            if i == M or j == N:
                return -inf
                
            x = coins[i][j]
            if i == M-1 and j == N-1:
                # no take
                if k > 0 and x < 0:
                    return 0
                else:
                    return x

            res = dp(i+1, j, k) + x
            res = max(res, + dp(i, j+1, k) + x)

            # no take
            if k > 0 and x < 0:
                res = max(res, + dp(i+1, j, k-1))
                res = max(res, + dp(i, j+1, k-1))
            return res 
            
        return dp(0, 0, 2)
```
