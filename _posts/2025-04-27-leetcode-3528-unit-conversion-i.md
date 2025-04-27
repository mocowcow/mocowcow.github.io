---
layout      : single
title       : LeetCode 3528. Unit Conversion I
tags        : LeetCode Medium Graph Tree DFS
---
biweekly contest 155。

## 題目

<https://leetcode.com/problems/unit-conversion-i/description/>

## 解法

題目包裝的很用心，一眼還看不太出來是什麼。  
注意看測資限制，保證每種單位**只有一種**轉換的方式組合。  

把每個單位當作節點，每個節點只有一個入口，代表這是一棵**樹**，根節點是 0。  
按照 conversions 建樹，遍歷節點同時計算乘積即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
MOD = 10 ** 9 + 7

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        N = len(conversions) + 1
        g = [[] for _ in range(N)]
        for a, b, w in conversions:
            g[a].append([b, w])

        ans = [0] * N

        def dfs(i, val):
            ans[i] = val
            for j, w in g[i]:
                dfs(j, val*w % MOD)

        dfs(0, 1)

        return ans
```
