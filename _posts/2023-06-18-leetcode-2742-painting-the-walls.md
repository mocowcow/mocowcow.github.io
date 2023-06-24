--- 
layout      : single
title       : LeetCode 2742. Painting the Walls
tags        : LeetCode Hard Array DP
---
周賽350。根本沒想到是dp，明明這幾天正在複習背包系列，有點難受。  

# 題目
輸入兩個長度為n的整數陣列cost和time，代表粉刷各個牆壁的成本和時間。  
你有兩個油漆工可用：  
- **付費**油漆工對第i個牆壁粉刷，需要花費time[i]單位時間，並收取cost[i]的費用  
- **免費**油漆工可以用1單位時間粉刷**任意**一個牆壁，且不收取費用。但只限**收費油漆工**工作時，才能使用**免費油漆工**  

求粉刷全部牆壁所需的**最小成本**。  

# 解法
大概可以理解成：**付費**的花多少時間，**免費**的就可以刷幾面牆。  

本來想用貪心法+雙指針優先選CP值最高的牆付費刷，盡可能爭取更多的**免費時間**，但碰到這種情況就無解：  
> cost = [2,1], time = [100,1]  
> cost[0]的CP值最高，選了成本是2  
> 但是選cost[1]，拿免費時間去刷cost[0]，成本1  

在不能確定規律的情況下，只好考慮這些牆用**付費**或**免費**時的最小成本，也就是**選**或**不選**。  
第i面牆有兩種選擇：  
- 選付費，成本會多出cost[i]，免費次數增加time[i]  
- 不選付費(免費)，成本不變，免費次數減少1  

定義dp(i,free)：刷第i\~N-1面牆，且剩下free次免費次數時的最小成本。  
轉移方程式：dp(i,free) = min(dp(i+1, free+time[i])+cost[i], dp(i+1,free-1))  
base cases：當i=N，全部牆都粉刷完，若free小於0，代表免費額度不夠用，不合法，回傳inf；否則回傳0。  

注意：最多只有N=500面牆，超過牆壁數量的的免費次數都是無意義的，所以免費額度要和N取最小值。  

共有N面牆，免費額度介於[-N,N]之間，時間複雜度O(N^2)。  
空間複雜度O(N^2)。  

```python
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N=len(cost)
        
        @cache
        def dp(i,free):
            if i==N and free<0:
                return inf
            if i==N:
                return 0
            return min(
                dp(i+1,free-1),
                dp(i+1,free+min(N,free+time[i]))+cost[i]
            )
        
        return dp(0,0)
```

對於處理超過N的免費次數，還有兩種方法：  
1. 處理付費時不處理，改在遞迴開頭檢查，如果free大於N，直接回傳dp(i,N)  
2. 如果free次數可以刷完剩下的牆，直接剪枝，回傳0  

```python
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N=len(cost)
        
        @cache
        def dp(i,free):
            if free>=(N-i): # paint all for free
                return 0
            if i==N:
                return inf
            return min(
                dp(i+1,free-1),
                dp(i+1,free+time[i])+cost[i]
            )
        
        return dp(0,0)
```

上面講了好幾次**選**或**不選**，聽起來很像01背包，其實稍微轉換一下定義就真的是背包問題。  
把粉刷完的**牆壁個數**視為背包空間，也就是免費+付費必須大於等於N面牆。  
每付費刷一面牆，還能免費刷cost[i]面牆。選了第i面牆，總共可以裝下cost[i]+1面牆。  

定義dp(i,wall)：在第0\~i面牆中，還有wall面要刷時的最小成本。  
轉移方程式：dp(i,wall) = min(dp(i+1,wall-1-time[i])+cost[i], dp(i+1,wall))  
base case：當wall小於等於0，代表全部刷完了(可能還多刷)，回傳0；否則當i<0，沒牆壁可刷但卻刷不夠，不合法，回傳inf。  

時間複雜度O(N^2)。  
空間複雜度O(N^2)。  

```python
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N=len(cost)
        # paid count + free count >= N
        # total paid time >= free count
        # total paid time >= N - paid count
        # total paid time + paid count >= N
        
        @cache
        def dp(i,wall):
            if wall<=0:
                return 0
            if i<0:
                return inf
            return min(
                dp(i-1,wall-1-time[i])+cost[i],
                dp(i-1,wall)
            )
        
        return dp(N-1,N)
```

轉換成遞推。因為對於i來說只會從i-1的狀態轉移，可以把第一個維度壓縮掉。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N=len(cost)

#         dp=[[0]*(N+1) for _ in range(N+1)]
#         for i in range(1,N+1):
#             dp[0][i]=inf
        
#         for i in range(1,N+1):
#             c,t=cost[i-1],time[i-1]
#             for wall in range(N+1):
#                 dp[i][wall]=min(
#                     dp[i-1][max(0,wall-1-t)]+c,
#                     dp[i-1][wall]
#                 )
                
#         return dp[N][N]

        dp=[0]*(N+1)
        for i in range(1,N+1):
            dp[i]=inf
               
        for c,t in zip(cost,time):
            for wall in reversed(range(N+1)):
                dp[wall]=min(dp[wall],dp[max(0,wall-1-t)]+c)
                
        return dp[N]
```
