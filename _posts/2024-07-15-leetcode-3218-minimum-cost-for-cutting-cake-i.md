---
layout      : single
title       : LeetCode 3218. Minimum Cost for Cutting Cake I
tags        : LeetCode Medium Array DP Greedy Sorting
---
周賽 406。

## 題目

有個 m x n 的蛋糕需要切成數塊 1 x 1 的小塊。  

輸入整數 m, n，還有兩個陣列：  

- 大小為 m - 1 的 horizontalCut，其中 horizontalCut[i] 代表在第 i 條水平線分割的成本  
- 大小為 n - 1 的 verticalCut，其中 verticalCut[j] 代表在第 j 條垂直線分割的成本  

每次操作，你可以任選一塊不為 1 x 1 大小的蛋糕，並且：  

- 在第 i 條水平線分割，成本為 horizontalCut[i]  
- 在第 j 條垂直線分割，成本為 verticalCut[j]  

每次分割操作後，蛋糕都會變成兩塊獨立的小蛋糕，且分割成本不會改變。  

求把所有蛋糕切成 1 x 1 的**最低成本**。  

## 解法

每次分割後都會變成兩塊**更小且獨立**的蛋糕，具有重疊的子問題，因此考慮 dp。  
為了知道分割成本，我們需要知道當前的小蛋糕屬於原本的哪塊位置。  

定義 dp(r1, r2, c1, c2)：當前蛋糕屬於原本的第 r1\~r2 列，以及第 c1\~c2 行。  
轉移：所有水平 / 垂直分割方式中的最小值。  

- 水平分割：  
    枚舉 [r1, r2 - 1] 之間的所有分割線 r，分成上下兩塊。  
- 垂直分割：  
    枚舉 [c1, c2 - 1] 之間的所有分割線 c，分成左右兩塊。  

base：當前 r1 = r2 且 c1 = c2 時，大小為 1 x 1。不需分割，回傳 0。  

時間複雜度 O(n^2 \* m^2 \* max(n, m))。  
空間複雜度 O(n^2 \* m^2)。  

```python
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        @cache
        def dp(r1, r2, c1, c2):
            if r1 == r2 and c1 == c2:
                return 0
            res = inf
            for r in range(r1, r2):
                res = min(res, dp(r1, r, c1, c2) + dp(r + 1, r2, c1, c2) + horizontalCut[r])
            for c in range(c1, c2):
                res = min(res, dp(r1, r2, c1, c) + dp(r1, r2, c + 1, c2) + verticalCut[c])
            return res
        
        return dp(0, m - 1, 0, n - 1)
```
