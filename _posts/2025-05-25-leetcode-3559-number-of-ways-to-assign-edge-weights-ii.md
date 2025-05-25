---
layout      : single
title       : LeetCode 3559. Number of Ways to Assign Edge Weights II
tags        : LeetCode Hard Tree Math DFS DP BinaryLifting
---
biweekly contest 157。  
最近很流行倍增，連出好幾次快出爛了。  

## 題目

<https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/description/>

## 解法

基本上跟 Q3 一樣，只是改成任意兩點 x, y 的路徑，然後查詢好幾次。  

x, y 兩點間的路徑數可以用 LCA 倍增來求。  
注意 x = y 時路徑數為 0，需要特判答案 0。  

時間複雜度 O((N + Q) log N)。  
空間複雜度 O(N log N)。  

```python
MOD = 10 ** 9 + 7
MX = 10 ** 5 + 5
pow2 = [0] * MX
pow2[0] = 1
for i in range(1, MX):
    pow2[i] = pow2[i-1] * 2 % MOD


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        bl = TreeLCA(edges)

        def solve(x, y):
            dis = bl.get_distance(x, y)
            if dis == 0:
                return 0
            else:
                return pow2[dis-1]

        return [solve(*q) for q in queries]


class TreeLCA:
    def __init__(self, edges):
        N = len(edges) + 5  # 有多少點
        self.MX = N.bit_length()  # 最大跳躍次數取 log
        # 建圖
        g = [[] for _ in range(N)]
        for a, b in edges:
            g[a].append([b, 1])
            g[b].append([a, 1])
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
        dfs(1, -1, 0)
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
```
