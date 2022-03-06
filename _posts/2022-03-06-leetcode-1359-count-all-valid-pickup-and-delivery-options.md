---
layout      : single
title       : LeetCode 1359. Count All Valid Pickup and Delivery Options
tags 		: LeetCode Hard DP Math
---
每日題。數學解太噁心了，學不來。

# 題目
你是送貨員，有n個貨物要送，每個貨物[i]一定要先取貨才能送貨，求取貨n次+送貨n次順序共有幾種。答案要MOD 10^9+7。

# 解法
送第n次的順序是由n-1次的順序中挑選兩個位置插入取/送貨行程，因此可以用DP來算。  
影響的狀態有取貨和送貨數兩個，使用二維DP。定義dp(pick,deli)為剩下取pick次、送deli次處理的順序種類。  
那麼新的順序中可以由上次取貨的順序中，隨意位置插入新的取貨各pick種。再加入上次送貨的順序中，再取新貨後插入新的送貨。  
轉移方程式為dp(pick,deli)=pick\*dp(pick-1,deli)+(deli-pick)\*dp(pick,deli-1)。  
base cases有：pick和deli為0，代表事情都做完了，回傳1。若pick或deli小於0(多做事)，或是deli小於pick(還沒取貨就送貨)，都是不可能的情況，回傳0。  

```python
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9+7

        @lru_cache(None)
        def dp(pick, deli):
            if pick < 0 or deli < 0 or deli < pick:
                return 0
            if pick == deli == 0:
                return 1
            ans = pick*dp(pick-1, deli)
            ans += (deli-pick)*dp(pick, deli-1)
            return ans % MOD

        return dp(n, n)

```
