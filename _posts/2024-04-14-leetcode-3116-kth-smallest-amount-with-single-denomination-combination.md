---
layout      : single
title       : LeetCode 3116. Kth Smallest Amount With Single Denomination Combination
tags        : LeetCode Hard Array Math BinarySearch BitManipulation BitManipulation
---
周賽 393。  
相似題 [878. nth magical number]({% post_url 2022-05-05-leetcode-878-nth-magical-number %})。  

## 題目

輸入整數陣列 coins，代表不同的硬幣面額。另外還有一個整數 k。  

你擁有無限個各面額的硬幣。但是你**不能**混用不同的面額來組成金額。  

求你可以湊出的**第 k 小**的金額。  

## 解法

先從簡單的例子開始研究。  
在只有一種硬幣面額 v 時，答案就是 k \* v。  

那如果有 A, B 兩種面額呢？  
我們沒辦法很直接的知道需要多少，畢竟根據 A, B 值不同，有時候可以湊出相同的金額。  

先透過簡單的除法算出 [1, x] 範圍內，A, B 的倍數各有 (x / A) 和 (x / B) 個。  
但這些數可能有**交集**，也就是**公倍數**。  
設 A, B 的最小公倍數為 lcmAB，則 [1, x] 內可被或 A, B 整除的數共有 cnt = (x / A) + (x / B) + (x / lcmAB) 個。  
而 cnt 的值會隨著 x 一同增加，具有**單調性**，因此可以透過**二分答案**找出 cnt = k 所需的 x 最小值。  

---

根據**排容原理**，兩個集合時，A∪B = A + B - A∩B。  
三個集合時，A∪B∪C = A + B + C - A∩B - A∩C - A∩B + A∩B∩C。  
但是本題最多高達 15 個硬幣面額，要暴力寫死 15 個集合的聯集公式好像不太現實，手會先斷掉。  

其實有一個規律：枚舉集合 S = {A, B, C..} 的所有子集。如果子集大小是奇數，則將此子集加入結果；否則從結果中扣除。  
以四個集合聯集為例：加入 4 個大小 1 的子集、扣除 6 個大小 2 的子集、加入 4 個大小 3 的子集、扣除 1 個大小 4 的子集。  

如此一來，我們最多只需要枚舉 2^15 個子集，並以其 lcm 計算聯集的大小。  

---

最後來把上述流程整合起來。  

維護函數 ok(x)：判斷 [1, x] 區間內，硬幣面額倍數 cnt 是否滿足 k 個。  
以 bitmask 枚舉各子集，計算 lcm 後和 x 進行計算。  

再套一個二分搜尋，透過 ok(mid) 找最小值。  
因為最小的整數是 1，下界 lo = 1。  
最差情況下只有面額 25 的硬幣，且 k = 2 \* 10^9，故上界 hi = 10^11。  

複雜度有點難算，姑且先跳過不管。  

```python
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        N = len(coins)
        
        def ok(x):
            cnt = 0
            for mask in range(1, 1 << N): # enumerate subsets
                lcm_val = 1
                sign = -1 if mask.bit_count() % 2 == 0 else 1
                for i in range(N):
                    if mask & (1 << i):
                        lcm_val = lcm(lcm_val, coins[i])
                cnt += sign * (x // lcm_val)
            return cnt >= k
        
        lo = 1
        hi = 10 ** 11
        while lo < hi:
            mid = (lo + hi) // 2
            if not ok(mid):
                lo = mid + 1
            else:
                hi = mid
                
        return lo
```
