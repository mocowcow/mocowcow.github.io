---
layout      : single
title       : LeetCode 3256. Maximum Value Sum by Placing Three Rooks I
tags        : LeetCode Hard Matrix
---
biweekly contest 137。  

## 題目

輸入 m \* n 的 二維矩陣，代表一個棋盤。其中 board[i][j] 代表格子 (i, j) 的值。  

在西洋棋中，**車**可以攻擊同一行列的其他棋子。  
你需要擺放 3 個車、並保證其無法互相攻擊。  

求 3 個車所在格子值的**最大總和**。  

## 解法

先考慮最最暴力的方法：先枚舉三個不同的列、再從其中枚舉三個行。  
雖然鐵定會超時，但是可以看看哪些地方能優化。  

為了使總和盡可能大，應當優先選擇列中較大的元素。  
在運氣好的時候，三個元素的行數不會衝突，沒有問題；但最壞情況下，另外兩列的最大、次大元素都比當前列的最大元素還大，就只能選擇當列第三大的元素。  

例如：  
> [3,2,1,0]  
> [4,3,2,0]  
> [5,4,3,0]  
> 最大總和應是 1+3+5  

實際上每列只有**前三大的元素**會被使用到，其餘的永遠不可能用上。

---

之後只需要枚舉三個不同的列，然後枚舉其中前三大元素的組合，只在行數不衝突的時候更新答案即可。  

枚舉列數是 O(M^3)，之後枚舉前三大元素是 O(3^3)。  
在 M = 100 時，大概是 2e7 的計算量。但實際上 O(M^3) 常數是小於 1 的，勉強能通過。  

時間複雜度 O(M^3)。  
空間複雜度 O(M)。  

```python
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        M, N = len(board), len(board[0])

        def get_top3(row):
            pairs = [[row[j], j] for j in range(N)]
            return nlargest(3, pairs)

        ans = -inf
        rows = [get_top3(row) for row in board]
        for r1 in range(M):
            for r2 in range(r1 + 1, M):
                for r3 in range(r2 + 1, M):
                    for v1, c1 in rows[r1]:
                        for v2, c2 in rows[r2]:
                            for v3, c3 in rows[r3]:
                                if c1 != c2 and c1 != c3 and c2 != c3:
                                    ans = max(ans, v1 + v2 + v3)

        return ans
```
