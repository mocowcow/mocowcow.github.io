---
layout      : single
title       : LeetCode 3530. Maximum Profit from Valid Topological Order in DAG
tags        : LeetCode Hard BitManipulation Bitmask DP
---
biweekly contest 155。  
標題有拓樸排序，就傻傻的被騙去做了，而且還漏看測資。  
結果就是 WA 好幾次。  

## 題目

<https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/description/>

## 解法

照拓樸排序的限制下選擇節點。  
從 order = 1 開始數，第 order 個選的節點 i 利潤為 order \*  scores[i]。  

---

為什麼直接做拓樸排序不行？舉個簡單的例子：  
> n = 4, edges = [[0,1], [2,3]], scores = [1,1,1,500]  

最初只有節點 0 或 2 可以選，分數都是 1。  
0 後面的節點 1 分數還是 1；但 2 後面的節點 3 分數高達是 500。  
我們不知道後方的 scores[i] 有多大，因此沒有辦法貪心決定最佳路線。  

---

注意到 n 上限 22。  
我們無法貪心求解，因此考慮暴力枚舉所有順序求最大值。  

說到暴力就想到**回溯**。  
可以維護各節點入度，實現拓樸排序，並枚舉選擇順序。  
可是 n! = 23! 還是太大，依然會超時。  

---

從特殊到一般，先考慮所有節點都沒有入度的情況，可以任意順序選擇。  
不同的選法可能得到相同的剩餘節點，有**重疊的子問題**，考慮 dp。  
而 22 個節點，可用 bitmask 表示選擇的狀態，其中第 i 個 bit 設為 1 表示節點 i 已選過。  

定義 dp(mask)：剩餘節點為 mask 時，可得到的最大利潤。  

order 當前由 mask 中的 1 bit 數再加 1 可得。  

至於入度比較麻煩。  
原本使用狀壓 dp 搭配回溯維護入度，也不知道到底該不該過，提交 4 次超時 2 次。  
後來發現也能用 mask 維護各節點的父節點，例如：  
> edges[i] = [0,1]  
> 節點 0 連向節點 1
> 將 fa_mask[1] 的第 0 個 bit 設為 1  
> 即 fa_mask[1] |= (1<<i)  

每個狀態枚舉下一個選擇的節點 i，若 mask & fa_mask[i] 不等於 fa_mask[i] 則代表尚有父節點未選。  

---

遍歷 edges 維護各節點的父節點 fa_mask。  
答案入口 dp(0)。  

時間複雜度 O(m + (n \* 2^n) )。  
空間複雜度 O(2^n)。  

```python
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        FULL = (1 << n) - 1

        fa_mask = [0] * n
        for a, b in edges:
            fa_mask[b] |= 1 << a

        @cache
        def dp(mask):
            if mask == FULL:
                return 0
            res = 0
            order = 1 + mask.bit_count()
            for i in range(n):
                bit = 1 << i
                if mask & bit > 0:
                    continue
                # fa node still alive
                if mask & fa_mask[i] != fa_mask[i]:
                    continue
                t = dp(mask | bit)
                res = max(res, order*score[i] + t)
            return res

        return dp(0)
```
