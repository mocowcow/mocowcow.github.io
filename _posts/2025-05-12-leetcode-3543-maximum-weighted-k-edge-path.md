---
layout      : single
title       : LeetCode 3543. Maximum Weighted K-Edge Path
tags        : LeetCode Medium DP HashTable BitManipulation Bitmask
---
biweekly contest 156。  
又是複雜度妙妙屋，提交前都不知道會不會超時。  

## 題目

<https://leetcode.com/problems/maximum-weighted-k-edge-path/>

## 解法

求任意起點走 k 步可得到的**小於 t** 的**最大**路徑和。  

選擇不同的起點，卻有可能得到相同的終點及路徑和。  
有**重疊的子問題**，考慮 dp。  

定義 dp(i, sm, step)：當前位於節點 i，路徑和為 sm，再走 step 步可得到的最大路徑和。  
枚舉所有可走的下一個位置 j，更新答案最大值。  
走完 step 步後，若 sm < t 則答案為 t；否則為 -1。  

---

枚舉所有節點 i 為起點，答案為 dp(i, 0, k) 取最大值。  

時間複雜度 O(nkt)。  
空間複雜度 O(nkt)。  

nkt = 300 \* 300 \* 600 = 5e7。  
雖然看起來會超時，但其實對於 dp(i,sm, step) 來說，sm 不太可能填滿 t 種，實際上沒有這麼多狀態。  

```python
class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append([b, w])

        @cache
        def dp(i, sm, step):
            if step == 0:
                if sm < t:
                    return sm
                return -1
            res = -1
            for j, w in g[i]:
                res = max(res, dp(j, sm+w, step-1))
            return res

        ans = -1
        for i in range(n):
            ans = max(ans, dp(i, 0, k))

        return ans
```

看官方提示是叫我們定義 dp[i][step]：走 step 步停在節點 i 的有效路徑和集合。  
可用刷表法更新。  
若存在一條 i 往 j 且邊權為 w 的邊，則以 dp[i][step] + w 更新 dp[j][step+1]。  

時間複雜度 O(nkt)。  
空間複雜度 O(nkt)。  

```python
class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append([b, w])

        # dp[i][step] = {}
        # end at node i with certain steps
        dp = [[set() for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0].add(0)

        for step in range(k):
            for i in range(n):
                for j, w in g[i]:
                    for x in dp[i][step]:
                        if x+w < t:
                            dp[j][step+1].add(x+w)

        ans = -1
        for i in range(n):
            for x in dp[i][k]:
                ans = max(ans, x)

        return ans
```

集合可以用 bitset 進行優化。  

bitset 中第 i 個位元代表路徑長度 i。  
取 bit_length - 1 可得最高位。  

為了受限於 t，bitset 只需保留最小的 t 個位元。  

時間複雜度 O(nkt / w)，其中 w = 32 或 64。  
空間複雜度 O(nkt / w)。

```python
class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append([b, w])


        T_MASK = (1 << t) - 1
        # dp[i][step] = {}
        # end at node i with certain steps
        dp = [[0] * (k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1

        for step in range(k):
            for i in range(n):
                for j, w in g[i]:
                    dp[j][step+1] |= dp[i][step] << w
                    dp[j][step+1] &= T_MASK

        ans = -1
        for i in range(n):
            x = dp[i][k]
            ans = max(ans, x.bit_length() - 1)

        return ans
```
