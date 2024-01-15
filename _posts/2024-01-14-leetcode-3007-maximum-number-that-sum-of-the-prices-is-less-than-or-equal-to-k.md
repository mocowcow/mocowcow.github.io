---
layout      : single
title       : LeetCode 3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K
tags        : LeetCode Medium Math String DP BitManipulation BinarySearch
---
周賽380。

## 題目

輸入整數 k 和 x。  

s 是一個整數 num 的二進位表示，**索引從 1 開始**。 num 的價格是滿足 i % x == 0 且 s[i] 是 1 的個數。  

求能夠滿足 1\~num 之間所有數的**價格總和**小於等於 k 的**最大** num 值。  

注意：  

- 二進位是從右向左數。例如 s = 11000, s[4] 是 1，而 s[2] 是 0  

## 解法

[233. number of digit one]({% post_url 2022-08-16-leetcode-233-number-of-digit-one %})

題目要求 1\~num 的總價小於等於 k，總價其實具有**單調性**，會隨著 num 單調遞增。  
若 1\~x 的總價超過 k，則答案不可能是 x 以上的值；反之，若 1\~x 總價不足 k ，則答案至少會是 x。  
因此我們可以透過二分答案來找到適當的 num。  

現在的問題變成：怎麼求 **1\~num 之間**能被 x 整除的 1 位元有幾個？  
看到這個 1\~num 之間，就想到我們的老朋友**數位dp**，基本上就和 [233. number of digit one]({% post_url 2022-08-16-leetcode-233-number-of-digit-one %}) 作法差不多，只是要計算一下當前是第幾個 bit。  

---

計算複雜度之前，還有另一個問題：num 的可能上界為多少？  
我也不知道怎麼算，但是測出來大概是 10^15，跟 k 的上限差不多。大概需要二分 O(log k)次，每次二分都要做一次數位dp。  

根據 num 的最大值 k，其二進位長度同為 O(log k)。  
同時，一個二進位表示中也最多擁有 O(log k) 個 1。  
每次數位dp 總共有 O(log k)^2 個狀態，每個狀態轉移一次。  

時間複雜度 O((log k)^3)。  
空間複雜度 O((log k)^2)。  

```python
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:

        def ok(mid):
            s = bin(mid)[2:]
            N = len(s)

            @cache
            def dp(i, is_limit, cnt1):
                if i == N:
                    return cnt1
                bit = N - 1 - i + 1
                res = 0
                down = 0
                up = 1 if not is_limit else int(s[i])
                for j in range(down, up + 1):
                    new_cnt1 = cnt1 + 1 if bit % x == 0 and j == 1 else cnt1
                    new_limit = is_limit and j == up
                    res += dp(i + 1, new_limit,  new_cnt1)
                return res
            return dp(0, True, 0) <= k

        lo = 1
        hi = 10**15
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if not ok(mid):
                hi = mid - 1
            else:
                lo = mid

        return lo
```
