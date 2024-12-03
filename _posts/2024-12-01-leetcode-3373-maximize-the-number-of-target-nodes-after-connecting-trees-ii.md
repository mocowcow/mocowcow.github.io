---
layout      : single
title       : LeetCode 3373. Maximize the Number of Target Nodes After Connecting Trees II
tags        : LeetCode Hard Graph Tree BFS DFS Greedy DP
---
weekly contest 426。  
大概是今年最簡單的 Q4。  
吐槽一下英文版題目，明明大部分內容和 Q4 相同，偏偏要寫不同的句子、格式，浪費一大堆時間重看。  

## 題目

輸入兩棵無向樹，分別有 n 和 m 個節點，編號為 [0, n - 1] 和 [0, m - 1]。  

輸入兩個二維整數陣列 edges1 和 edges2，長度分別為 n - 1 和 m - 1。  
其中 edges1[i] = [a<sub>i</sub>, b<sub>i</sub>] 代表 a<sub>i</sub> 和 b<sub>i</sub> 之間有一條邊，而 edges2[i] = [u<sub>i</sub>, v<sub>i</sub>] 代表 u<sub>i</sub> 和 v<sub>i</sub> 之間有一條邊。  

若節點 u 和 v 之間的路徑的邊數是**偶數**，則稱 u 是 v 的**目標**。  
注意：一個節點保證是自己的**目標**。  

回傳長度 n 個整數陣列 answer，其中 answer[i] 代表將第一棵樹中的某個節點與第二棵樹中的某個節點連邊後，第一棵樹中節點 i 的**目標**數量的**最大值**。  

注意：每次查詢都是獨立的。下次連邊之前，要先把上次連的邊清除掉。  

## 解法

和 Q3 只差在**目標**的定義從 k 步內改成偶數距離。  

同樣先不考慮連邊，只考慮第一棵樹中所有節點 i 中的目標，依然可以用 bfs (或 dfs) 求出偶數距離的節點。  
但本題 n 高達 10^5，無法每個點都求一次。  

設想有棵直線的樹，呈現：  
> 1,2,3  

對於節點 1 來說，有 2 個偶數距離，1 個奇數距離。  
對於節點 2 來說，有 1 個偶數距離，2 個奇數距離。  
對於節點 3 來說，有 2 個偶數距離，1 個奇數距離。  

每一個節點的奇偶數量會和他的鄰居相反。  
我們只需要對任一節點做一次 bfs，之後透過推導出所有節點的奇偶數量，也就是**換根 dp**。  

---

再來考慮連邊，同樣題目沒有規定要連到 i 上。  

設第二棵樹從節點 0 出發，偶數距離有 even 個，奇數距離有 odd 個：  

- 把 i 連到第二棵樹的 0，會多出 odd 個偶數距離。  
- 把 i 連到第二棵樹的 0 的隔壁鄰居，會多出 even 個偶數距離。  

也就是說你想要多 even 或是 odd 都行，為答案最大化，取 mx = max(even, odd)。  
在第一棵做換根 dp 時，把 ans[i] 加上 mx。  

時間複雜度 O(n + m)。  
空間複雜度 O(n + m)。  

```python
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        N, M = len(edges1) + 1, len(edges2) + 1
        g1 = [[] for _ in range(N)]
        g2 = [[] for _ in range(M)]
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)
        for a, b in edges2:
            g2[a].append(b)
            g2[b].append(a)

        # find odd/even of tree
        def bfs(g, i):
            vis = [False] * len(g)
            q = deque()
            q.append(0)
            vis[0] = True
            cnt = [1, 0] # even, odd
            parity = 0
            while q:
                parity ^= 1
                for _ in range(len(q)):
                    curr = q.popleft()
                    for adj in g[curr]:
                        if not vis[adj]:
                            vis[adj] = True
                            q.append(adj)
                            cnt[parity] += 1
            return cnt

        tree1 = bfs(g1, 0)
        tree2 = bfs(g2, 0)
        # can add odd or even of tree2
        mx = max(tree2)
        ans = [0] * N

        def dfs(i, fa, even, odd):
            ans[i] = even + mx
            for j in g1[i]:
                if j == fa:
                    continue
                dfs(j, i, odd, even)

        dfs(0, -1, tree1[0], tree1[1])

        return ans
```

改寫成 dfs 寫法。  

```python
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        N, M = len(edges1) + 1, len(edges2) + 1
        g1 = [[] for _ in range(N)]
        g2 = [[] for _ in range(M)]
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)
        for a, b in edges2:
            g2[a].append(b)
            g2[b].append(a)

        # find odd/even of tree
        def dfs(g, i, fa, parity):
            res = [0, 0]
            res[parity] = 1
            for j in g[i]:
                if j == fa:
                    continue
                t = dfs(g, j, i, parity^1)
                res[0] += t[0]
                res[1] += t[1]
            return res

        tree1 = dfs(g1, 0, -1, 0)
        tree2 = dfs(g2, 0, -1, 0)
        # can add odd or even of tree2
        mx = max(tree2)
        ans = [0] * N

        def dfs(i, fa, even, odd):
            ans[i] = even + mx
            for j in g1[i]:
                if j == fa:
                    continue
                dfs(j, i, odd, even)

        dfs(0, -1, tree1[0], tree1[1])

        return ans
```
