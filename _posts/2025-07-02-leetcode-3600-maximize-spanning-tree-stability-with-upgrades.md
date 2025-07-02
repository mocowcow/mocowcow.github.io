---
layout      : single
title       : LeetCode 3600. Maximize Spanning Tree Stability with Upgrades
tags        : LeetCode Hard Graph Tree UnionFind BinarySearch Greedy
---
weekly contest 456。

## 題目

<https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/description/>

## 解法

**生成樹**是從一個圖中保留若干條邊，得到一個包含所有節點的**樹**。  
即 N 個節點 N-1 條邊。  

---

邊有**強度** (邊權) 以及 must = 0/1 是否必選的限制。  

首先排除沒有答案的特殊情況：  

- 原圖不連通。樹是子圖，也不可能連通  
- 必選的邊會構成環，不是樹  

使用併查集處理兩種連通狀態，若滿足任一者答案為 -1；否則一定有合法的生成樹。  

---

至多可以把 k 條**非必選邊**的強度加倍。求樹上邊的**最小值最大化**。  

最小值最大化通常可以二分答案。  
若可以找到強度都大於等於 x 的樹，則答案至少為 x；  
反之，若無法找到強度都大於等於 x 的樹，則答案必小於 x。  

需要寫一個函數 ok(limit)：判斷是否能得到邊強度都大於等於 limit 的樹。  
建樹時同樣先放必選的邊，若必選邊強度小於 limit 則不合法。  
**避免浪費加倍**，首先考慮不需要加倍就滿足 limit 的邊，若邊上兩點介於不同連通塊則將其連通。  

若依然無法完全合併，才考慮**使用加倍**。  
找到那些強度小於 limit 的邊，若加倍後可達 limit 且兩個介於不同連通塊則將其連通。  

時間複雜度 O((N + M log N) log MX)，其中 M = len(edges)，MX = 強度上限。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        all_edges = UnionFind(n)
        must_edges = UnionFind(n)
        for x, y, _, must in edges:
            all_edges.union(x, y)
            if must == 1:
                if must_edges.find(x) == must_edges.find(y):  # must 有環不合法
                    return -1
                must_edges.union(x, y)

        if all_edges.component_cnt != 1:  # 沒辦法連通
            return -1

        def ok(limit):
            uf = UnionFind(n)
            # 先連 must
            for x, y, s, must in edges:
                if must == 1 and s < limit:  # must 無法連
                    return False
                if s >= limit:
                    uf.union(x, y)

            # 再考慮沒連的，看能不能用加倍連
            rem_k = k
            for x, y, s, must in edges:
                if rem_k == 0 or uf.component_cnt == 1:
                    break
                if must == 0 and s < limit and s*2 >= limit:
                    if uf.find(x) != uf.find(y):
                        uf.union(x, y)
                        rem_k -= 1
            return uf.component_cnt == 1

        lo = 1
        hi = 10 ** 6
        while lo < hi:
            mid = (lo+hi+1) // 2
            if not ok(mid):
                hi = mid - 1
            else:
                lo = mid

        return lo


class UnionFind:
    def __init__(self, n):
        self.parent = [0] * n
        self.component_cnt = n  # 連通塊數量
        for i in range(n):
            self.parent[i] = i

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py
            self.component_cnt -= 1  # 連通塊減少 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
```
