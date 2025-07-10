---
layout      : single
title       : LeetCode 3607. Power Grid Maintenance
tags        : LeetCode Medium UnionFind
---
weekly contest 457。

## 題目

<https://leetcode.com/problems/power-grid-maintenance/description/>

## 解法

若干個發電廠，某些透過纜線連接在一起。
有兩種操作：  

- 查詢發電廠 x，按照描述回答  
- 關閉發電廠 x  

被查詢電廠 x 要由連通的**未關閉**且**編號最小**的電廠回答。  
這是**連通塊**問題，直覺想到**併查集**。  

先按照併查集連接電廠，然後按照所屬連通塊分組。  
分組後，每組的電廠編號正好是由大到小。  

---

但是電廠關閉順序不定，可以用 sorted list 維護。  
注意：題目沒有保證 x 不會重複關閉，小心檢查。  

另一個思路是：我們只在乎**當前最小**的電廠是否關閉。  
每次關閉電廠只先做標記，等到回答詢問時才檢查，若編號最小的電廠被標記則不斷刪除。這叫做**懶刪除**。  

時間複雜度 O(c log c + Q)。  
空間複雜度 O(c log c)。  

```python
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c+1)
        for a, b in connections:
            uf.union(a, b)

        groups = defaultdict(deque)
        for i in range(1, c+1):
            groups[uf.find(i)].append(i)

        online = [True] * (c+1)
        ans = []
        for q_type, x in queries:
            if q_type == 2:
                online[x] = False
                continue

            if online[x]:
                ans.append(x)
                continue

            g = uf.find(x)
            q = groups[g]
            while q and not online[q[0]]:
                q.popleft()

            if q:
                ans.append(q[0])
            else:
                ans.append(-1)

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
