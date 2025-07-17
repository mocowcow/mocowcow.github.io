---
layout      : single
title       : LeetCode 3615. Longest Palindromic Path in Graph
tags        : LeetCode Hard DFS DP BitManipulation Bitmask
---
weekly contest 458。  
又是複雜度妙妙屋，而且還卡常數。  

## 題目

<https://leetcode.com/problems/longest-palindromic-path-in-graph/description/>

## 解法

從特殊到一般，先從最特殊的情況考慮：一條鍊。  
如果用普通 dfs 做的話，無法紀錄經過的節點字元，很難搞成回文。  

以前在做回文題型時，常用的技巧是**中心擴展法**。  
枚舉中心點，然後找旁邊兩個相同字元的節點同時走出去。  

因為不允許重複走，所以需要紀錄走過的節點。  
並且 n = 14 很適合用 bitmask 維護。  
我們需要紀錄左右端點 i, j 以及走過的 mask。  

---

雖然 mask 紀錄了走過的點，但實際上可能不只一種走法。試想：  
> n = 3 都是 "a"，而且都有連邊  
> 合法路徑有 [0,1,2], [0,2,1], [1,0,2], [1,2,0], ..  

不同走法可能得到相同的 mask，有**重疊的子問題**，考慮 dp。  
定義 dp(i, j, mask)：路徑左右端點為 i, j，且已走過 mask 時可擴展的最大長度。  

枚舉奇數中心入口 dp(i, i, mask)、偶數中心入口 dp(i, j, mask)，更新答案最大值。  

---

狀態有 n \* n \* 2^n 種。  
每個狀態需至多轉移 2^n 次。  

時間複雜度 O(n^4 \* 2^n)。  
空間複雜度 O(n^2 \* 2^n)。  

乍看之下很多，但很多狀態都是無效的，畢竟要形成路徑才能出現在 mask，而且擴展的順序也受限於字元。  

但這樣還是會超時。  
注意 dp(i, j, mask) 和 dp(j, i, mask) 是等價的，誰左誰右無所謂。  
我們只需要計算其中一個，節省一半的計算量。  

```python

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        @cache
        def dp(i, j, mask):
            if i > j:  # 優化，只計算 i < j
                return dp(j, i, mask)
            res = 0
            for a in g[i]:
                a_mask = 1 << a
                if a_mask & mask:
                    continue
                for b in g[j]:
                    b_mask = 1 << b
                    if a == b or b_mask & mask or label[a] != label[b]:
                        continue
                    new_mask = mask | a_mask | b_mask
                    res = max(res, dp(a, b, new_mask) + 2)
            return res

        ans = 0
        # 一個中心點
        for i in range(n):
            mask = 1 << i
            ans = max(ans, dp(i, i, mask) + 1)

        # 兩個中心點
        for i, j in edges:
            if label[i] == label[j]:
                mask = 1 << i
                mask |= 1 << j
                ans = max(ans, dp(i, j, mask) + 2)

        return ans
```
