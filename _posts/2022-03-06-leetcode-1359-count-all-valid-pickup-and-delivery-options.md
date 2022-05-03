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
那麼新的順序中可以由上次取貨的順序中，加取第pick個貨。再加入上次送貨的順序中，加送第(deli-pick)個貨。  
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

2022-5-3更新。  
複習一下排列組合，終於搞懂數學解法，難怪一堆人說這題簡單。我得向數學老師道個歉。  

dp(n)代表有n個包裹的配送方式。
n=1時，只有一種方式(P1,D1)。  
n=2時，現在有3個空位可以插入。我們有兩種插法：  
1. P2和D2塞到第i個空位  
2. P2塞到第i個空格，D2塞到第i+1個空位  
   
第一種方式，就是C(3,1)=3種，第二種方式，就是C(3,2)=3種，加起來總共6種方式可以插入P2和D2。
所以dp(2)=dp(1)*6=6種。  

n=3時，有5個空位可以插入。  
第一種方式，C(5,1)=5種，第二種方式，C(5,2)=10種，共15種。  
dp(3)=dp(2)*15=90種。  

C(n,1)一定是N，不用多管。但是C(n,2)就麻煩一點，看看成不能簡化：  
> C(n,2) = n! / (2!*(n-2)!)  
> n!和(n-2)!約分掉，只剩下n*(n-1)，2!等於2  
> 變成只剩下n*(n-1)/2  

```python
class Solution:
    def countOrders(self, n: int) -> int:
        dp=1
        MOD=10**9+7
        for i in range(2,n+1):
            slot=i*2-1
            way=slot
            way+=slot*(slot-1)//2 # C(slot,2) = slot!/(2!*(slot-2)!) = slot*(slot-1)/2
            dp=(dp*way)%MOD
            
        return dp
```