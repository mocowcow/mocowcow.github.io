---
layout      : single
title       : LeetCode 3493. Properties Graph
tags        : LeetCode Medium Graph UnionFind HashTable
---
weekly contes 442。

## 題目

<https://leetcode.com/problems/properties-graph/description/>

## 解法

並查集模板題。  
暴力枚舉 properties[i], properties[j] 求交集，若交集大小 >= k 則合併 i 和 j。  
最後統計連通塊數量。  

時間複雜度 O(N^2 \* M)。  
空間複雜度 O(NM)。  

```python
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        N = len(properties)
        uf = UnionFind(N)
        pps = [set(x) for x in properties]
        for i in range(N):
            for j in range(i+1, N):
                if len(pps[i] & pps[j]) >= k:
                    uf.union(i, j)

        s = set()
        for i in range(N):
            s.add(uf.find(i))

        return len(s)
        

class UnionFind:
    def __init__(self, n):
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
```
