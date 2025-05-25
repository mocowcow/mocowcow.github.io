---
layout      : single
title       : LeetCode 3558. Number of Ways to Assign Edge Weights I
tags        : LeetCode Medium Tree Math DFS DP
---
biweekly contest 157。  
dp 寫完才發現是數學。  

## 題目

<https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/description/>

## 解法

題目有點繞，反正就是說從根節點 1 出發到**最深**的某個葉節點，是誰不重要。  
先 dfs 求樹的深度。  

---

深度從 0 算起，最大深度為 mx 時，路徑上有 mx + 1 個節點、有 mx 條邊。  
該路徑上邊權可填 1 或 2，求有幾種填法能讓路徑為為奇數。  

偶數和加 1 會變奇數；加 2 維持偶數不變。  
奇數和加 1 會變偶數；加 2 維持奇數不變。  
其實就是奇偶性**改或不改**。  

---

定義 f[i][parity=0/1]：有 i 條邊，路徑和為偶數 / 奇數的填法。  

最初在只有 1 條邊時，只有 odd = 1 種奇數填法，和 even = 1 種奇數填法。  
f[1][0] = 1, f[1][1] = 1。  

加上第 2 條邊。  
可把 f[1][0] 改成奇數，也可把 f[1][1] 維持奇數。  
可把 f[1][1] 改成偶數，也可把 f[1][0] 維持偶數。  
f[2][1] = f[1][0] + f[1][1]。  
f[2][2] = f[1][0] + f[1][1]。  

發現根本兩個狀態根本一樣，每次都是前一項**乘 2** 而已。  
有 mx 條邊，就有 2^(mx-1) 種奇數選法。  
可先預處理 2 的次方。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
MOD = 10 ** 9 + 7
MX = 10 ** 5 + 5
pow2 = [0] * MX
pow2[0] = 1
for i in range(1, MX):
    pow2[i] = pow2[i-1] * 2 % MOD


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        N = len(edges) + 1
        g = [[] for _ in range(N+1)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        mx_depth = 0

        def dfs(i, fa, depth):
            nonlocal mx_depth
            if depth > mx_depth:
                mx_depth = depth
            for j in g[i]:
                if j == fa:
                    continue
                dfs(j, i, depth+1)

        dfs(1, -1, 0)

        return pow2[mx_depth-1]
```
