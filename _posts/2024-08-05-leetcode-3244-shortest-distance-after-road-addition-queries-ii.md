---
layout      : single
title       : LeetCode 3244. Shortest Distance After Road Addition Queries II
tags        : LeetCode Hard SegmentTree
---
weekly contest 409。  

## 題目

輸入整數 n 以及二維整數陣列 queries。  

有 n 個城市，編號分別由 0 到 n - 1。  
最初，所有編號滿足 0 <= i < n - 1 的城市 i，都存在一條通往城市 i + 1 的**無向**道路。  

queries[i] = [u<sub>i</sub>, v<sub>i</sub>] 代表**新增**一條 u<sub>i</sub> 往 v<sub>i</sub> 的**無向**道路。  
對於每次查詢，你必須在新增道路後，查詢城市 0 到城市 n - 1 的最短距離。  

保證沒有任何查詢滿足 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。  

回傳陣列 answer，其中 answer[i] 代表第 i 次查詢的結果。  

## 解法

和上一題比起來，除了測資範圍變大之外，還多了個限制：  
> 任意兩個路徑之間不可能部分交集，只能是**無交集**或是**包含**  

因為不存在交錯的路徑，這代表可以**貪心**的選擇前往編號最大的城市 j。  

---

換句話說，每當新增了一條路徑 (x, y)，則界於 [x+1, y-1] 區間內的所有城市就不會訪問到了。  
我們只需要維護**哪些城市被刪除**，而答案就是剩餘的城市數減去 1。  

每次新增路徑後，需要**區間修改**連續的城市，並且**區間查詢**所有城市中有哪些被刪除。  
此處使用**線段樹**。  

時間複雜度 O(Q log n)。  
空間複雜度 O(n)。  

```python

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        seg = SegmentTree(n)
        ans = []
        for x, y in queries:
            if x + 1 <= y - 1:
                seg.update(1, 0, n-1, x+1, y-1, 1)
            ans.append(n - seg.tree[1] - 1)

        return ans


class SegmentTree:

    def __init__(self, n):
        self.tree = [0]*(n*4)
        self.lazy = [0]*(n*4)

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return a+b

    def push_down(self, id, L, R, M):
        """
        將區間懶標加到答案中
        下推懶標記給左右子樹
        """
        if self.lazy[id]:
            self.tree[id*2] = (M-L+1)
            self.lazy[id*2] = 1
            self.tree[id*2+1] = (R-M)
            self.lazy[id*2+1] = 1
            self.lazy[id] = 0

    def push_up(self, id):
        """
        以左右節點更新當前節點值
        """
        self.tree[id] = self.op(self.tree[id*2], self.tree[id*2+1])

    def update(self, id, L, R, i, j, val):
        """
        區間更新
        對[i, j]每個索引都變成 1
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            self.tree[id] = (R - L + 1)
            self.lazy[id] = 1
            return
        M = (L+R)//2
        self.push_down(id, L, R, M)
        if i <= M:
            self.update(id*2, L, M, i, j, val)
        if M < j:
            self.update(id*2+1, M+1, R, i, j, val)
        self.push_up(id)
```
