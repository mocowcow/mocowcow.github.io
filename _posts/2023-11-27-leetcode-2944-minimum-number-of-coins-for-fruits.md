---
layout      : single
title       : LeetCode 2944. Minimum Number of Coins for Fruits
tags        : LeetCode Medium Array DP MonotonicQueue
---
雙周賽118。這題描述也挺爛的，範例也很爛，看半天才知道他想幹嘛。  

## 題目

有一間水果店，賣幾種不同的水果。  

輸入索引從1開始的陣列prices，其中prices[i]代表第i個水果的價格。  

水果店的報價如下：  

- 若你付prices[i]購買第i個水果，則接下來的i個水果都可以免費  

注意：即使你**能免費**拿第j個水果，也依然可以選擇付費以取得優惠。  

求購買所有水果所需的**最少花費**。  

## 解法

> If you purchase the ith fruit at prices[i] coins, you can get the next i fruits for free.  

題目也沒說要按照什麼順序買，鬼才知道next i是什麼意思。看範例才確定是指從i開始往右邊數i個。  
買了水果只有右邊的會免費，因此由左到右遍歷每個水果i。i可以選擇付費或不付費，考慮dp。  

定義dp(i,free)：依序購買第i\~N個水果，且當前免費次數剩下free次時，所需的最小花費。  
轉移方程式：dp(i,free) = max(付費, 免費)  
付費=dp(i+1,i)+prices[i-1]；免費=dp(i+1,free-1)  
base case：當free<0時，代表免費次數不夠，回傳inf；當i>N代表水果買完，回傳0。  

時間複雜度O(N^2)，其中N為prices長度，同時也是免費次數的最大值。  
空間複雜度O(N^2)。  

```python
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        N=len(prices)
        
        @cache
        def dp(i,free):
            if free<0:
                return inf
            if i>N:
                return 0
            pay=dp(i+1,i)+prices[i-1]
            free=dp(i+1,free-1)
            return min(pay,free)
        
        return dp(1,0)
```

換個方式來思考，不是計算免費次數，而是直接跳過免費的水果。  

定義dp(i)：依序購買第i\~N個水果，所需的最小花費。  
轉移方程式：dp(i)=min(dp(i+free+1)) FOR ALL 0<=free<=i  
base case：當i>N代表水果買完，回傳0。  

狀態只剩下N個，但每個狀態最多轉移N次。時間複雜度不變，空間變小。  
時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        N=len(prices)
        
        @cache
        def dp(i):
            if i>N:
                return 0
            res=inf
            for free in range(i+1):
                res=min(res,dp(i+free+1))
            return res+prices[i-1]
            
        return dp(1)
```

改寫成遞推。  

```python
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        N=len(prices)
        dp=[0]*(N+2)
        for i in reversed(range(1,N+1)):
            res=inf            
            for free in range(i+1):
                if i+free+1>=len(dp):
                    break
                res=min(res,dp[i+free+1])
            dp[i]=res+prices[i-1]
            
        return dp[1]
```

注意到dp[i]從dp[i+1, i\*2+1]任一轉移而來；  
然後dp[i+1]從dp[i+1+1, (i+1)\*2+1]任一轉移。  

發現dp[i]和dp[i+1]的轉移來源有大量重疊。只要把出界的部分刪掉，然後多一個dp[i+1]就好。  
我們只要選擇這些來源中**成本最小**者，這邊可以用單調隊列進行優化，如此一來，每個狀態可以O(1)轉移。  

單調隊列主要有三步驟：  

1. 刪除過期(出界)的  
2. 刪除比最新選項還沒用的  
3. 加入最新選項  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        N=len(prices)
        dp=[0]*(N+2)
        q=deque()
        q.append([N+1,0]) # [idx, cost]
        for i in reversed(range(1,N+1)):
            # out of bound
            while q and q[0][0]>i*2+1:
                q.popleft()
            # monotonic increasing
            while q and dp[i+1]<q[-1][1]:
                q.pop()
            q.append([i+1,dp[i+1]])
            dp[i]=q[0][1]+prices[i-1]
            
        return dp[1]
```
