---
layout      : single
title       : LeetCode 3372. Maximize the Number of Target Nodes After Connecting Trees I
tags        : LeetCode Medium Graph BFS
---
weekly contest 426。

## 題目

輸入兩棵無向樹，分別有 n 和 m 個節點，編號為 [0, n - 1] 和 [0, m - 1]。  

輸入兩個二維整數陣列 edges1 和 edges2，長度分別為 n - 1 和 m - 1。  
其中 edges1[i] = [a<sub>i</sub>, b<sub>i</sub>] 代表 a<sub>i</sub> 和 b<sub>i</sub> 之間有一條邊，而 edges2[i] = [u<sub>i</sub>, v<sub>i</sub>] 代表 u<sub>i</sub> 和 v<sub>i</sub> 之間有一條邊。  

另外還輸入整數 k。  
若節點 u 和 v 之間的路徑的邊數小於等於 k，則稱 u 是 v 的**目標**。  
注意：一個節點保證是自己的**目標**。  

回傳長度 n 個整數陣列 answer，其中 answer[i] 代表將第一棵樹中的某個節點與第二棵樹中的某個節點連邊後，第一棵樹中節點 i 的**目標**數量的**最大值**。  

注意：每次查詢都是獨立的。下次連邊之前，要先把上次連的邊清除掉。  

## 解法

先不考慮連邊，只考慮第一棵樹中所有節點 i 中的目標。  
要找出距離 i 至多 k 步的節點，很簡單可以想到用 bfs (dfs 也可)。  

---

再來考慮連邊，雖然題目沒有規定要連到 i 上，但為了不浪費步數，第一棵樹當然是選 i。  

i 連接到第二棵樹上後，還可以繼續走 k-1 步。  
枚舉第二棵樹的連接點 i2，同樣用 bfs 求 k-1 步可到達的節點數，並找出最大值 mx。  

ans[i] 答案即為 bfs(i) + mx。  

時間複雜度 O(m^2 + n^2)。  
空間複雜度 O(m + n)。  

```python
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        N, M = len(edges1) + 1, len(edges2) + 1
        g1 = [[] for _ in range(N)]
        g2 = [[] for _ in range(M)]
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)
        for a, b in edges2:
            g2[a].append(b)
            g2[b].append(a)
        
        def bfs(g, i, step):
            vis = [False] * len(g)
            q = deque()
            q.append(i)
            vis[i] = True
            cnt = 1
            while step > 0:
                step -= 1
                for _ in range(len(q)):
                    curr = q.popleft()
                    for adj in g[curr]:
                        if not vis[adj]:
                            vis[adj] = True
                            q.append(adj)
                            cnt += 1
            return cnt

        # find best conn node of tree2
        mx = 0
        if k > 0:
            for i in range(M):
                res = bfs(g2, i, k-1)
                mx = max(mx, res)

        ans = [0] * N
        for i in range(N):
            res = bfs(g1, i, k)
            ans[i] = res + mx

        return ans
```
