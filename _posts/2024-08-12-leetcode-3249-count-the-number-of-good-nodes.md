---
layout      : single
title       : LeetCode 3249. Count the Number of Good Nodes
tags        : LeetCode Medium Tree DFS
---
weekly contest 410。  

## 題目

有一棵 n 節點的**無向樹**，編號分別從 0 到 n - 1，且根節點為 0。  
輸入長度 n - 1 的二維整數陣列 edges，其中 edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表 a<sub>i</sub> 和 b<sub>i</sub> 之間存在一條邊。  

若存在一個節點，其所有子節點所構成的子樹的大小都相同，則稱為**好的**。  

求有多少**好的子節點**。  

## 解法

dfs 遍歷整棵樹。  
遞迴取得子節點子樹的大小，若完全相同則答案加 1，最後回傳當前子樹大小。  
注意：一定要對所有子節點都 dfs，不可在途中發現大小不同就終止，否則會少算答案。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        N = len(edges) + 1
        g = [[] for _ in range(N)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        ans = 0
        def dfs(i, fa):
            nonlocal ans
            sizes = []
            for j in g[i]:
                if j == fa:
                    continue
                sizes.append(dfs(j, i))
            # is good
            if len(set(sizes)) <= 1:
                ans += 1
            return sum(sizes) + 1

        dfs(0, -1)

        return ans
```
