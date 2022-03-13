---
layout      : single
title       : LeetCode 2201. Count Artifacts That Can Be Extracted
tags 		: LeetCode Medium Array Matirx HashTable
---
周賽284。經典的自己嚇死自己，題目真的要看清楚。

# 題目
有一塊n*n的土地，裡面有好幾個文物artifacts，其中artifacts[i]=[r1,c1,r2,c2]，代表文物所佔的範圍左上及右下角。  
dig=[r,c]為開挖的地方，求有幾個文物可以被完整挖出來。

# 解法
一開始看到artifacts和dig長度上限為10^5，想說慘了暴力法大概沒辦法過，結果搞2D前綴和搞了半天才發現，所有文物都不會重疊，且每個文物最大只會有4的面積。那麼暴力法worst case也頂多是O(N^2)了。  
開一個n*n的表格，初始為1，代表有覆土。遍歷所有dig，把該位置的土挖掉，直更新成0。  
再來計算文物數量，遍歷所有文物，檢查是否範圍內是否都為0，若是則出土數+1。

```python
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        mud = [[1]*1002 for _ in range(1002)]

        for x, y in dig:
            mud[x][y] = 0

        cnt = 0
        for r1, c1, r2, c2 in artifacts:
            ex = True
            for r in range(r1, r2+1):
                if any(mud[r][c1:c2+1]):
                    ex = False
                    break
            if ex:
                cnt += 1

        return cnt

```
