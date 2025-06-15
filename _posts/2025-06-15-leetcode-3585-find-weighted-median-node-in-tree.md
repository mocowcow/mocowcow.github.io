---
layout      : single
title       : LeetCode 3585. Find Weighted Median Node in Tree
tags        : LeetCode Hard Tree BinaryLifting DP BinarySearch
---
weekly contest 454。  
剩五分鐘前才寫完，但是沒膽交答案。  
賽後交完四題全對，好像錯過的上分的機會。  

## 題目

<https://leetcode.com/problems/find-weighted-median-node-in-tree/description/>

## 解法

設 weight(x, y)：從 x 走到 y 的路徑權重和。

對於每個查詢 x, y：  
從 x 開始出發往 y 走，找到第一個點 target 滿足：  
> weight(x, target) >= weight(x, y) / 2  
> 即 weight(x, target) \* 2 >= weight(x, y)  

---

看到**樹上求距離**，又要查詢好幾次，大概就是**倍增**。  
我的倍增模板有三種功能，這次全都用上：  

- 求 x, y 的 lca  
- 求 x, y 的距離  
- 求 x 跳 k 步後的點  

---

從特殊到一般，先考慮最特殊、最單純的情況：  
x, y 呈鍊狀，且 y 是根節點。  

我們無法直接知道 target 是誰。  
但是可以知道從 x 跳 k 步抵達某點 temp 的路徑權重 w，進而知道是否滿足限制。  

若跳 k 步可滿足限制，則 k+1 步肯定也滿足限制；若 k 步不滿足限制，則 k-1 步肯定也不滿足限制。  
答案具有單調性，可透過**二分答案**找到第一個滿足限制的步數 k。  

每次二分需要從 x 跳 k 步，成本 O(log N)。  
共需二分 O(log N) 次，每次查詢複雜度 O(log N \* log N)。  

---

再來是比較麻煩的點：  
如果起點 x 是 y 的祖先節點、甚至兩者位於不同的子樹怎麼辦？  

例如範例二：根節 0，左右節點 1 和 2。  
倍增只能從子節點往上跳，如果查詢 x = 1, y = 2，從 1 跳到 0 就卡住了，沒辦法**拐彎**繼續跳到 2。  

---

答案很簡單，只是我腦子沒想通卡好久。  
**拐彎點**就是 lca！！  

設 x 到 lca 有 x_cnt 步。  
設 y 到 lca 有 y_cnt 步。  
討論 k 的大小：  

- k <= x_cnt，就是普通的跳 k 次  
- k > x_cnt，則先從 x 跳到 lca，然後從 lca 再跳 k - x_cnt 次  

但還是沒解決怎麼從 lca 往 y 子樹的方向跳？  
其實 lca 往下跳 need 次，等價於 y 往上跳 y_cnt - need 次。  
兩邊跳越的路徑和加起來即可。  

時間複雜度 O(Q \* log N \* log N)。  
空間複雜度 O(N log N)。  

```python
class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        bl = TreeLCA(edges)

        def solve(x, y):
            lca = bl.get_LCA(x, y)
            tot = bl.get_distance(x, y)
            x_cnt = bl.depth[x] - bl.depth[lca]
            y_cnt = bl.depth[y] - bl.depth[lca]

            # return [path_weight, target]
            def jump_k_from_x(k):
                if k <= x_cnt:
                    target = bl.jump_k(x, k)
                else:
                    need = y_cnt - (k-x_cnt)
                    target = bl.jump_k(y, need)
                w = bl.get_distance(x, target)
                return [w, target]

            # bisect for step k from x
            lo = 0
            hi = x_cnt + y_cnt
            while lo < hi:
                mid = (lo+hi) // 2
                if jump_k_from_x(mid)[0]*2 < tot:
                    lo = mid+1
                else:
                    hi = mid
            return jump_k_from_x(lo)[1]

        return [solve(*q) for q in queries]


class TreeLCA:
    def __init__(self, edges):
        N = len(edges) + 1  # 有多少點
        self.MX = N.bit_length()  # 最大跳躍次數取 log
        # 建圖
        g = [[] for _ in range(N)]
        for a, b, w in edges:
            g[a].append([b, w])
            g[b].append([a, w])
        # 建樹 樹上前綴和
        self.parent = [-1] * N
        self.depth = [0] * N
        self.ps = [0] * N

        def dfs(i, fa, dep):
            self.parent[i] = fa
            self.depth[i] = dep
            for j, w in g[i]:
                if j == fa:
                    continue
                self.ps[j] = self.ps[i] + w
                dfs(j, i, dep+1)
        dfs(0, -1, 0)
        # f[i][jump]: 從 i 跳 2^jump 次的位置
        # -1 代表沒有下一個點
        self.f = [[-1] * self.MX for _ in range(N)]
        # 初始化每個位置跳一次
        for i in range(N):
            self.f[i][0] = self.parent[i]
        # 倍增遞推
        for jump in range(1, self.MX):
            for i in range(N):
                temp = self.f[i][jump-1]
                if temp != -1:  # 必須存在中繼點
                    self.f[i][jump] = self.f[temp][jump-1]

    def get_LCA(self, x, y):
        depth = self.depth
        f = self.f
        if depth[x] > depth[y]:
            x, y = y, x
        # 把 y 調整到和 x 相同深度
        diff = depth[y] - depth[x]
        for jump in range(self.MX):
            if diff & (1 << jump):
                y = f[y][jump]
        # 已經相同
        if x == y:
            return x
        # 否則找最低的非 LCA
        for jump in reversed(range(self.MX)):
            if f[x][jump] != f[y][jump]:
                x = f[x][jump]
                y = f[y][jump]
        # 再跳一次到 LCA
        return f[x][0]

    def get_distance(self, x, y):
        lca = self.get_LCA(x, y)
        return self.ps[x] + self.ps[y] - self.ps[lca]*2

    def jump_k(self, x, k):
        """
        從 x 跳 k 次
        -1 表示不合法
        """
        for jump in range(self.MX):
            if k & (1 << jump):
                x = self.f[x][jump]
                if x == -1:  # 不能跳
                    return -1
        return x
```
