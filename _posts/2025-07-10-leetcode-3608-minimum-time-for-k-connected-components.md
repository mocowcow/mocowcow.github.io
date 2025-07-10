---
layout      : single
title       : LeetCode 3608. Minimum Time for K Connected Components
tags        : LeetCode Medium UnionFind BinarySearch Greedy Sorting
---
weekly contest 457。

## 題目

<https://leetcode.com/problems/minimum-time-for-k-connected-components/description/>

## 解法

題目就有寫連通塊，八成又是併查集。  

若刪除小於等於 x 的邊可以滿足要求，那麼刪除小於等於 x+1 也能滿足。  
x 越大，刪越多，連通塊越多；x 越小，刪越少，連通塊越少。  
答案有**單調性**，可以二分答案。  

二分要刪除的邊權 x，用併查集只連接大於 x 的邊，看是否能有 k 個連通塊。  

---

但我發現更優雅的性質。  

假設併查集支持刪除操作，本題就可以將 edges 排序，**由小到大刪除**，直到連通塊達到 k 個為止。  
我們可以將這個操作**倒過來**，等價於**由大到小加入**，在加入前檢查連通塊數量。  

記得在連完所有邊之後再次檢查是否滿足 k。  

時間複雜度 O(n log n)。  
空間複雜度 O(n)。  

```python

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=itemgetter(2), reverse=True)

        uf = UnionFind(n)
        ans = 0
        for a, b, time in edges:
            if uf.component_cnt >= k:
                ans = time
                uf.union(a, b)
            else:
                break

        if uf.component_cnt >= k:
            ans = 0

        return ans


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
