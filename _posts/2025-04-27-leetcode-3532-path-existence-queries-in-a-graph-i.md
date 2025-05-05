---
layout      : single
title       : LeetCode 3532. Path Existence Queries in a Graph I
tags        : LeetCode Medium Graph UnionFind
---
weekly contest 447。

## 題目

<https://leetcode.com/problems/path-existence-queries-in-a-graph-i/description/>

## 解法

最初想法是對每個 nums[i] 找到所有滿足 i < j 且 nums[j] - nums[i] <= maxDiff 的 j 將其連通。  
但在 maxDiff 很大的情況下複雜度為 O(n^2)，不可行。  

---

觀察發現：若 i 與 j 能連通，有索引 k 滿足 i < k < j，則 i 肯定可以連 k、且 k 可以連 j。  

- 我們只問 u, v 是否**連通**，不管距離。  
- 本題 nums 是**有序**的，因此能夠互相連通的索引都會聚集在一起。  

因此若要檢查 i 要連 j 是否連通，只須確保 [i,i+1], [i+1,i+2],.. [j-1,j] 都相連通。  

---

使用併查集，枚舉所有相鄰索引對，若絕對差小於 maxDiff 則將其連通。  

時間複雜度 O(n log n)。  
空間複雜度 O(n)。  

```python
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        for i in range(n-1):
            j = i+1
            if nums[j] - nums[i] <= maxDiff:
                uf.union(i, j)

        ans = []
        for x, y in queries:
            ans.append(uf.find(x) == uf.find(y))

        return ans


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

有個更簡單的想法，不需要併查集。  

以 left[i] 表示 i 往左可達的最遠位置。  
在 i 無法往左時，left[i] = i；  
否則一旦能抵達 i-1，則也可達 left[i-1]。  

每次查詢檢查 left[x], left[y] 是否相同即可。  

時間複雜度 O(n)。  
空間複雜度 O(n)。  

```python
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        left = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                left[i] = left[i-1]
            else:
                left[i] = i

        ans = []
        for u, v in queries:
            ans.append(left[u] == left[v])

        return ans
```
