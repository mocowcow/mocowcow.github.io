---
layout      : single
title       : LeetCode 3276. Select Cells in Grid With Maximum Score
tags        : LeetCode Hard DP BitManipulation Bitmask HashTable
---
weekly contest 413。  

## 題目

輸入二維正整數矩陣 grid。  

你必需從矩陣中選擇一或多個格子，滿足：  

- 選擇的格子列號不可相同。  
- 選擇的格子值不可相同。  

你的**分數**為所選格子值的**總和**。  
求可達到的**最大分數**。  

## 解法

從範例二很明顯看出，優先選擇最大值的**貪心策略**並不管用。  
肯定要使用 dp，枚舉選哪個比較好。  

第一直覺是枚舉第 i 行中要選哪個元素，但還需要額外的狀態表示哪些值選過。  
定義 dp(i, mask)：從第 grid[i..N-1] 可選的最大分數，且 mask 為**已選值**的狀態。  
但格子值的值域多達 100 種元素，共需 2^100 種狀態，好像也不太可行。  

---

既然**從列選擇值**不可行，那就換一個角度，改成**從值選擇列**。  

定義 dp(i, mask) 從值為 [i..100] 中的格子中可選的最大分數，且 mask 為**已選列**的狀態。  
轉移：dp(i, mask) = max(選, 不選)。  
    - 不選：dp(i+1, mask)。  
    - 選：max(dp(i+1, new_mask) + i)，其中 new_mask = mask | (1<<r)，且第 r 列未選過。  
base：當 i>MX 時，超過有效值域，回傳 0。  

先遍歷一次 grid，將所有格子的列號依照值域來分組。  
答案入口為 dp(1, 0)。  

時間複雜度 O(MN \* 2^M)。  
空間複雜度 O(MX \* 2^M)，其中 MX = max(grid[i][j])。  

```python
MX = 100
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        d = [[] for _ in range(MX + 1)]
        for r in range(M):
            for c in range(N):
                x = grid[r][c]
                d[x].append(r)

        @cache
        def dp(i, mask):
            if i > MX:
                return 0
            res = dp(i + 1, mask)
            for r in d[i]:
                if mask & (1 << r) != 0:
                    continue
                new_mask = mask | (1 << r)
                res = max(res, dp(i + 1, new_mask) + i)
            return res

        return dp(1, 0)
```
