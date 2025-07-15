---
layout      : single
title       : LeetCode 3613. Minimize Maximum Component Cost
tags        : LeetCode Medium UnionFind Sorting Greedy
---
weekly contest 458。
最近併查集有點多。  

## 題目

<https://leetcode.com/problems/minimize-maximum-component-cost/description/>

## 解法

相似題 [3608. minimum time for k connected components]({% post_url 2025-07-10-leetcode-3608-minimum-time-for-k-connected-components %})。  

---

成本是**連通塊內最大邊權**。  
答案要求所有連通塊內的**最大成本最小化**。  

雖然出現關鍵字最大值最小化，可以二分答案，但其實不需要。  

若超過 k 個連通塊則不斷連邊，則按照邊權由小到大嘗試連邊。  
兩個連通塊合併後，其成本不可能變小，因此答案也不可能會更小。  

記得特判初始節點數量就小於等於 k。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if n <= k:
            return 0

        edges.sort(key=itemgetter(2))
        uf = UnionFind(n)
        for a, b, c in edges:
            uf.union(a, b)
            if uf.component_cnt <= k:
                return c



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
