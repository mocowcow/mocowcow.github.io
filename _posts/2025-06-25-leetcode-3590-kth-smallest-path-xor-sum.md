---
layout      : single
title       : LeetCode 3590. Kth Smallest Path XOR Sum
tags        : LeetCode Hard Tree DFS SortedList
---
biweekly contest 159。  
滿奇妙的題，靠自己想出來的人是真的有慧根。  

## 題目

<https://leetcode.com/problems/kth-smallest-path-xor-sum/description/>

## 解法

注意幾個小細節：  

- 路徑 XOR 值是**從 0 到 u**，而非**從 u 起算**。  
- 是求子樹**不同的** XOR 值中的第 k 小，需要去重  

---

從根節點 dfs 可以算出各節點 i 的 XOR 值。  

最暴力的做法就是用 sorted set 合併所有子節點的 XOR 值，然後找第 k 小。  
但是在樹接近鍊狀的情況下，每次合併將近 N 個節點，共要合併 N 次，複雜度 O(N^2)。  

---

有研究過併查集的同學應該很熟悉，正是**按秩合併** (union by rank)。  
又稱**啟發式合併**。但英語圈好像沒有類似的叫法。  

兩個集合 A, B 合併時，將較小者合併到較大者，所需的插入次數更少。  

考慮某節點 i 在最壞情況下會被重新插入幾次？  

- 最初 i 自成一個集合，大小為 1。  
- 合併至目標大小至少為 1 的目標集合，故合併後的集合大小至少為 2。  
- 再次合併至目標大小至少為 2 的目標集合，故合併後的集合大小至少為 4。  
- ...

可見 i 所屬的集合每次合併後大小**翻倍**。也就是說 i 至多被合併 log N 次。  
共有 N 個節點，總合併次數至多 O(N log N)。  

---

最後是回答查詢。  
按照查詢的節點 u 分組，改成離線查詢，在 dfs 合併後回答即可。  

時間複雜度 O((N \* log N \* log N) + (Q log N) )。  
空間複雜度 O(N + Q)。  

註：雖然本題應該用 sorted set，但不知道為啥用 sorted list 判斷重複再插入反而更快。  

```python

class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        N = len(par)
        Q = len(queries)
        g = [[] for _ in range(N)]
        for i in range(1, N):
            g[par[i]].append(i)

        qs = [[] for _ in range(N)]
        for qi, (u, k) in enumerate(queries):
            qs[u].append([qi, k])

        ans = [-1] * Q

        def dfs(i, xor):
            xor ^= vals[i]
            sl = SL()
            sl.add(xor)
            for j in g[i]:
                t = dfs(j, xor)
                if len(sl) < len(t):
                    sl, t = t, sl
                for x in t:
                    if x not in sl:
                        sl.add(x)
            # answer queries
            for qi, k in qs[i]:
                if len(sl) >= k:
                    ans[qi] = sl[k-1]
            return sl

        dfs(0, 0)

        return ans
```
