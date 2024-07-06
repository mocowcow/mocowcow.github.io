---
layout      : single
title       : LeetCode 1245. Tree Diameter
tags        : LeetCode Medium Array Graph Tree DP DFS BFS TopologySort 
---
上次周賽有用到樹的直徑，趁機會補一下題解。  

## 題目

**樹的直徑**指的是樹中最長路徑的邊數。  

有一個 n 節點的無向樹，編號分別從 0 到 n - 1。  
輸入二維整數陣列 edges，其中 edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表 a<sub>i</sub> 和 b<sub>i</sub> 之間存在一條邊。  

求樹的直徑。  

## 解法

**無向樹**其實是一種**無向圖**，可以任意選擇節點做樹根。  
想通這點後清晰很多。  

---

本題固定選擇 0 做為根節點。  

直徑是必定是由兩個節點所組成的最長路徑，有可能是：  

- 根節點出發，走到某個葉節點  
- 某個葉節點出發，走到另一個葉節點  

考慮每個節點做為子樹時，與直徑的關係：  

- 直徑在當前節點**轉彎**。子樹中**兩條最長路徑**構成直徑  
- 直徑不在當前節點**轉彎**。而是由最長的一條，在更上層的位置才轉彎  

---

因此我們在求每個子樹的最大深度時，可以順便透過**兩條最大深度**來更新直徑，並回傳最大深度，供祖先節點使用。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        N = len(edges) + 1
        g = [[] for _ in range(N)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        res = 0
        def dp(i, fa):
            nonlocal res
            mx1 = mx2 = 0
            for j in g[i]:
                if j == fa:
                    continue
                t = dp(j, i)
                if t > mx1:
                    mx1, mx2 = t, mx1
                elif t > mx2:
                    mx2 = t
            res = max(res, mx1 + mx2) # update diameter
            return mx1 + 1 # max depth

        dp(0, -1)
        
        return res
```
