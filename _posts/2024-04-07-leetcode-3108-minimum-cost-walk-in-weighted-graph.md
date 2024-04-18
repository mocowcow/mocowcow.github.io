---
layout      : single
title       : LeetCode 3108. Minimum Cost Walk in Weighted Graph
tags        : LeetCode Hard Array Graph UnionFind BitManipulation DFS
---
周賽 392。這題也有點問題，沒講清楚起點和終點相同要怎樣，只能猜 -1 或是 0。  
前一百名內有 8X 人都猜錯了，笑死。至少錯一次後就知道答案，沒有隱藏測資很良心了。  

2024/4/18 更新：官方竟然刪掉起終點相同的測資，重新批改一次，算是非常合理的決策。  

## 題目

有一個**無向**的**權重**圖，共有 n 個節點，編號從 0 到 n - 1。  

輸入整數 n，還有二維整數陣列 edges，其中 edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]，代表 u<sub>i</sub> 和 v<sub>i</sub> 之間存在一條權重為 w<sub>i</sub> 的邊。  

一次**移動**會經過一連串的節點和邊。每次移動從某個節點出發，並在某個節點結束。  
注意：同個節點或邊可以被**多次訪問**。  

從 u 移動到 v 的**費用**定義為：途中所經過所有邊權互相做 AND 運算後的結果。  
換句話說，如果經過的邊權為 w0, w1, w2, ..., wk，則費用是 w0 & w1 & w2 & ... & wk。  

另外輸入二維整數陣列 query，其中 query[i] = [s<sub>i</sub>, t<sub>i</sub>]。  
每次查詢，你要求出 s<sub>i</sub> 到 t<sub>i</sub> 的最小費用。若無法達成移動，則答案是 -1。  

回傳陣列 answer，其中 answer[i] 是第 i 次查詢的**最小**費用。  

## 解法

首先複習 AND 運算的特性：**只少不多**。做越多次運算，越可能使結果值變小。  

移動時，經過的邊越多，費用越可能減少。  
而且每個點、邊都可以**重複訪問**，那麼最佳解就是把**能走的都走一次**。  

---

為了知道有哪些邊可以走，首先得找出節點組成的**連通塊**。這裡使用並查集。  

首先遍歷一次 edges，把每條邊上的兩個節點連接起來。  
維護陣列 val，其中 val[i] 代表以節點 i 為根的連通塊中，所有邊權 AND 的結果。  
再遍歷第二次 edges，將邊權和對應的 val[i] 做 AND 運算。  
如此一來就能 O(1) 查詢連通塊中所有邊的 AND 結果。  

---

查詢 (s, t) 的移動費用，共有兩種情形：  

- s, t 不連通，答案 -1  
- s, t 不同但連通，答案 val[root(s)]  

時間複雜度 O(n + E + Q)，其中 E = len(edges)，Q = len(query)。  
空間複雜度 O(n)，答案空間不計入。  

```python
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            uf.union(a, b)

        val = [-1] * n
        for a, b, w in edges:
            p = uf.find(a)
            val[p] &= w
        
        ans = []
        for s, t in query:
            if uf.find(s) != uf.find(t):
                ans.append(-1)
            else:
                ans.append(val[uf.find(s)])
                
        return ans
        
        
class UnionFind:
    def __init__(self, n):
        self.parent = [0]*n
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

單純使用 DFS/BFS 也可以。  
但不同於一般的做法，不管相鄰的點有沒有訪問過，都要和邊權做 AND 運算。  

時間複雜度 O(n + E + Q)。  
空間複雜度 O(n + E)。  

```python
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append([b, w])
            g[b].append([a, w])
            
        def dfs(i): # get AND value of connected component
            res = -1
            group[i] = len(val)
            for j, w in g[i]:
                res &= w
                if group[j] == -1:
                    res &= dfs(j)
            return res
        
        group = [-1] * n 
        val = []
        for i in range(n):
            if group[i] == -1:
                val.append(dfs(i))
                
        ans = []
        for s, t in query:
            if group[s] != group[t]:
                ans.append(-1)
            else:
                ans.append(val[group[s]])
                
        return ans
```
