---
layout      : single
title       : LeetCode 3609. Minimum Moves to Reach Target in Grid
tags        : LeetCode Hard Math
---
weekly contest 457。

## 題目

<https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/description/>

## 解法

按照題意做的話，每次都有兩種方向可選，會走到很多沒用的地方去。  
雖然有重疊的子問題，但就算 dp 狀態數還是太多，不好處理。  

---

研究一下移動的性質。  
m = max(x, y)，不管是 x+m 或是 y+m，加了 m 之後一定會變成最大值。  
如果從終點往回走，可以根據 x, y 的關係推算出上一個位置。  

---

設當前位置 x, y，上次位置 px, py。  
有 m = max(px, py)。  

設 x >= y，即 x 從 px 而來。  
有 x = px+m 且 y = py，即 m = max(px, y)。  

分類討論：  

- x > 2y：  
    只能是 m = px，有 x = px+m = 2px  
    得 px = x/2  
    若 x 為奇數無解  

- x < 2y：  
    只能是 m = y，有 x = px+m = px+y  
    得 px = x-y  

- x = y：  
    最特別的情況。兩者之一必須直接回到 0  
    即從 (px, 0) 或是 (0, py) 而來，走哪條無所謂，反正是對稱的  
    若起點 sx, sy 都非零則無解  

---

x < y 的情況同理。  
利用對稱性，若 x < y 則直接交換 x, y 和 sx, sy 即可。  

時間複雜度 O(log tx + log ty)。  
空間複雜度 O(log tx + log ty)。  

```python
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        ans = dfs(tx, ty, sx, sy)
        if ans == inf:
            return -1

        return ans


def dfs(x, y, sx, sy):
    if x == sx and y == sy:
        return 0

    if x < sx or y < sy:
        return inf

    # 其中一個必須直接跳到 0
    if x == y:
        if sx == 0:
            return dfs(0, y, sx, sy) + 1
        if sy == 0:
            return dfs(x, 0, sx, sy) + 1
        return inf

    # 保證 x >= y
    if x < y:
        x, y = y, x
        sx, sy = sy, sx

    if x > y*2:
        if x % 2 == 1:
            return inf
        return dfs(x//2, y, sx, sy) + 1
    else:
        return dfs(x-y, y, sx, sy) + 1
```
