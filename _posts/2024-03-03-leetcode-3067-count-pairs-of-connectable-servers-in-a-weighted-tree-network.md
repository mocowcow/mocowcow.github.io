---
layout      : single
title       : LeetCode 3067. Count Pairs of Connectable Servers in a Weighted Tree Network
tags        : LeetCode Medium Array Graph DFS
---
雙周賽125。感覺題目描述不太好，對於輸入的邊使用 **weight**，但是求答案的條件又講 **distance**，有點混淆。  

## 題目

有一個**無根**的樹，共有 n 個節點，代表 n 台伺服器，編號分別從 0 到 n-1。  
輸入二維整數陣列 edges，其中 edges[i] = [a<sub>i</sub>, b<sub>i</sub>, weight<sub>i</sub>]，代表 a<sub>i</sub> 和 b<sub>i</sub> 之間存在**權重**為 weight<sub>i</sub> 一條邊。  
另外還有整數 signalSpeed。  

若兩台伺服器 a, b 可以透過另一台伺服器 c **連線**，必須滿足：  

- a < b 且 a != c 且 b != c  
- c 到 a 路徑的**權重和**可被 signalSpeed 整除  
- c 到 b 路徑的**權重和**可被 signalSpeed 整除  
- c 到 a 路徑和 c 到 b 路徑不可**共用相同的邊**  

回傳長度為 n 的陣列 count，其中 count[i] 代表可透過伺服器 i **連線**的伺服器對**數量**。  

## 解法

透過某伺服器 c **連線**，可以把 c 視作這棵樹的根節點，而 a, b 都是 c 的子孫節點。  
但要求 a, b 不可共邊，則兩點必須分屬**不同的子樹**。  

並且，從根節點前往 a, b 的路徑權重總和還要被 signalSpeed 整除，因此遍歷子樹時也要記錄權重和。  

至於 a < b，只是要避免 (a, b) 和 (b, a) 兩種重複計算。  

---

維護變數 tot，代表已知的合法節點。  
枚舉所有根節點 root，並枚舉其各子樹中各有 cnt 個合法節點。  
根據乘法原理，此 cnt 個節點可以和 tot 個節點組成 cnt \* tot 個數對，加入count[root]中，然後把 cnt 累計入 tot。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        N = len(edges) + 1
        g = [[] for _ in range(N)]
        for a, b, w in edges:
            g[a].append([b, w])
            g[b].append([a, w])
            
        # count good nodes 
        def dfs(i, fa, w_sum):
            good = 0
            if w_sum % signalSpeed == 0: # good
                good += 1
            for j, w in g[i]:
                if j == fa:
                    continue
                good += dfs(j, i, w_sum + w)
            return good
            
        ans = [0] * N
        for root in range(N):
            tot = 0
            for j, w in g[root]:
                cnt = dfs(j, root, w) 
                ans[root] += tot * cnt
                tot += cnt
            
        return ans
```
