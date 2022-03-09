---
layout      : single
title       : LeetCode 1466. Reorder Routes to Make All Paths Lead to the City Zero
tags 		: LeetCode Medium DFS Graph
---
這題也挺有趣的，第一次碰到這種概念。

# 題目
一個有向圖，有n個城市以及n-1個單向道路連結。你可以轉換任意道路的方向，求最少需要幾次轉向才能讓所有城市都能前往0號城市。

# 解法
想了一陣子沒啥頭緒，看了提示如醍醐灌頂。  
先把所有道路當作是雙向的看待，從城市0開始DFS，每個城市都只抵達一次。如果經過的方向和初始的不同，則轉向次數+1，

```python
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)
        origin = set()
        for a, b in connections:
            g[a].append(b)
            g[b].append(a)
            origin.add((a, b))

        re = 0
        visited = set()

        def dfs(i):
            nonlocal re
            visited.add(i)
            for x in g[i]:
                if x in visited:
                    continue
                if (x, i) not in origin:
                    re += 1
                dfs(x)

        dfs(0)

        return re

```
