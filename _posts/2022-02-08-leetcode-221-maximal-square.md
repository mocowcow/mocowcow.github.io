---
layout      : single
title       : LeetCode 221. Maximal Square
tags 		: LeetCode Medium DP Matrix
---
DP教學題，很明顯知道需要二維DP，但是代表什麼意義比較難想到。

# 題目
給予M*N的矩陣，裡面元素只會是1或0。求完全由1組成的正方形最大面積可為多少。

# 解法
如果整個矩陣裡只有0，代表不可能有正方形，先過濾此情況回傳0。  
接下來開始DP。

>步驟1：定義狀態  

dp[r][c]代表讀取完matrix[r][c]之後的結果，表示以(r,c)為右下角，可以組成邊長為多少的正方形。

>步驟2：找出狀態轉移方程式  

一個邊長為x的正方形，一定可以拆分成其他邊長為x-1的小正方形，而必要條件是當前格子值為1。  
只有在matrix[r][c]為'1'時，更新dp[r][c]值，並順便更新最大邊長值。  
方程式為dp[r][c] = min(左邊的邊長,上面的邊長,左上角的邊長)+1。

>步驟3：處理base cases  

第一行及第一列無法參照其他位置，必須依照當前數字初始化。

最後回傳邊長*邊長。

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not any([x.count('1') for x in matrix]):
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0]*N for _ in range(M)]
        # base cases
        for c in range(N):
            dp[0][c] = int(matrix[0][c])
        for r in range(M):
            dp[r][0] = int(matrix[r][0])
        # transition
        side = 1
        for r in range(1, M):
            for c in range(1, N):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])+1
                    side = max(side, dp[r][c])

        return side**2
```
