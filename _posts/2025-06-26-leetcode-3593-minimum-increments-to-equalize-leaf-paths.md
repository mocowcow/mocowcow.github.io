---
layout      : single
title       : LeetCode 3593. Minimum Increments to Equalize Leaf Paths
tags        : LeetCode Medium Tree DFS
---
weekly contest 455。

## 題目

<https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/description/>

## 解法

對節點 i 的子節點來說，從根節點 0 到 i 的路徑都是同一條。  
有差別的其實是子節點的下段部分，因此從葉節點向上計算路徑和更加方便。  

---

看範例 1，有兩個子節點值分別為 1, 3。  
我們只能增加節點值，所以只能把 1 改成 2，需要操作一次。  

那如果某節點有超過 2 個節點，例如路徑和 = x, y, z，其中 x <= y <= z 呢？  
很簡單，把所有子節點都改成 z。操作次數即非 z 的子節點個數。  

時間複雜度 O(N log  N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)

        ans = 0

        def dfs(i, fa):
            nonlocal ans
            vals = []
            for j in g[i]:
                if j == fa:
                    continue
                vals.append(dfs(j, i))

            # i is leaf
            if not vals:
                return cost[i]

            mx = max(vals)
            mx_cnt = sum(x == mx for x in vals)
            ans += len(vals) - mx_cnt
            return mx + cost[i]

        dfs(0, -1)

        return ans
```
