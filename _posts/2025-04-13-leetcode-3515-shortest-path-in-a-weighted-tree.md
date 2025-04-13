---
layout      : single
title       : LeetCode 3515. Shortest Path in a Weighted Tree
tags        : LeetCode Hard Tree DFS SegmentTree
---
biweekly contest 154。  
好久不見的 dfs 時間戳，大概超過一年沒出現。  
本來自己沒線索，但是看到大神提示就知道怎麼做了。  

## 題目

<https://leetcode.com/problems/shortest-path-in-a-weighted-tree/description/>

## 解法

難點在如何**修改路徑權重**。  

從特殊到一般，考慮鍊狀樹修改權重的時候會發生什麼事？  
設 o1 為根節點。  
> o1 -> o2 - > o3 -> o4 -> o5 ...  

若把邊 (o2, o3) 的權重增加 delta：  

- 從 o1 到 o1, o2 的路徑和不影響  
- 從 o1 到 o2, o3, o4, o5,.. 的權重都會增加 delta  

可見邊下方**子樹**中所有節點的的路徑和都會增加 delta。  

---

如何知道子樹中有那些節點？  
利用 dfs 先進後出的特性，在遞迴過程中給訪問到的節點標記**進入時間**，即 **dfs 時間戳** (可以理解成第幾個被訪問)。  
同樣地，在退出遞迴時標記**離開時間**。  

則對於節點 i 來說，位於連續區間 [tin[i]..tout[i]] 即**子樹所有節點**的時間戳。  
若通往 i 的的邊權增加 delta，則只需要把區間 [tin[i]..tout[i]] 都增加 delta。  

問題轉換成**區間修改**和**單點查詢**，可以用線段樹或是樹狀陣列。  
此處選用線段樹。  

---

最後剩下小細節，邊權是**修改成新值**，需要自己維護舊值，並計算增量 delta。  
然後 (u, v) 看不出來誰位於下方，需要利用時間戳 tin[u], tin[v] 判斷。  

注意：不要把節點的原編號和時間戳搞混！！很重要！！

時間複雜度 O((N + Q) log N)。  
空間複雜度 O(N)。  

```python

class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        seg = SegmentTree(n+5)
        g = [[] for _ in range(n+1)]
        edge_weight = Counter()
        for a, b, w in edges:
            g[a].append([b, w])
            g[b].append([a, w])
            edge_weight[(a, b)] = w

        timestamp = 0
        tin = [0] * (n+1)
        tout = [0] * (n+1)

        def dfs(i, fa, sm):
            nonlocal timestamp
            timestamp += 1
            tin[i] = timestamp
            seg.update(1, 1, n, timestamp, timestamp, sm)
            for j, w in g[i]:
                if j == fa:
                    continue
                dfs(j, i, sm+w)
            tout[i] = timestamp

        dfs(1, -1, 0)

        ans = []
        for q in queries:
            # query path sum of [1, x]
            if q[0] == 2:
                x = q[1]
                sm = seg.query(1, 1, n, tin[x], tin[x])
                ans.append(sm)
                continue

            # update weight of edge (u, v)
            _, u, v, new_w = q
            old_w = edge_weight[(u, v)]
            delta = new_w - old_w
            edge_weight[(u, v)] = new_w

            # find which is son
            if tin[u] < tin[v]:
                son = v
            else:
                son = u

            # apply update to subtree
            seg.update(1, 1, n, tin[son], tout[son], delta)

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
            self.tree[id*2] += self.lazy[id]*(M-L+1)
            self.lazy[id*2] += self.lazy[id]
            self.tree[id*2+1] += self.lazy[id]*(R-M)
            self.lazy[id*2+1] += self.lazy[id]
            self.lazy[id] = 0

    def push_up(self, id):
        """
        以左右節點更新當前節點值
        """
        self.tree[id] = self.op(self.tree[id*2], self.tree[id*2+1])

    def query(self, id, L, R, i, j):
        """
        區間查詢
        回傳[i, j]的總和
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            return self.tree[id]
        M = (L+R)//2
        self.push_down(id, L, R, M)
        res = 0
        if i <= M:
            res = self.op(res, self.query(id*2, L, M, i, j))
        if M+1 <= j:
            res = self.op(res, self.query(id*2+1, M+1, R, i, j))
        return res

    def update(self, id, L, R, i, j, val):
        """
        區間更新
        對[i, j]每個索引都增加val
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            self.tree[id] += val * (R - L + 1)
            self.lazy[id] += val
            return
        M = (L+R)//2
        self.push_down(id, L, R, M)
        if i <= M:
            self.update(id*2, L, M, i, j, val)
        if M < j:
            self.update(id*2+1, M+1, R, i, j, val)
        self.push_up(id)
```
