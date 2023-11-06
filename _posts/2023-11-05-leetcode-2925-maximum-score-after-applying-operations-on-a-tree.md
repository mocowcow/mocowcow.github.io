---
layout      : single
title       : LeetCode 2925. Maximum Score After Applying Operations on a Tree
tags        : LeetCode Medium Array Graph Tree DP DFS
---
周賽370。上次有樹狀dp，這次也有。  

## 題目

有個n節點的無向樹，節點編號從0\~n-1，且根節點為0。  
輸入二維整數陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表a<sub>i</sub>和b<sub>i</sub>之間存在一條邊。  

另外還有長度n的整數陣列values，其中values[i]代表第i個節點的**價值**。  

你的初始分數為0。每次操作，你可以：  

- 選擇任意節點i  
- 得到values[i]分  
- 將values[i]變成0  

若從根節點出發至**任意葉節點**的路徑**價值總合**都不為0，則稱此樹是**健康的**。  

求任意次操作後，在樹依然**健康**的情況下，可以獲得的**最大分數**。  

## 解法

所有路徑都是從0出發的，以下將0到i的路徑簡稱**i的路徑**。  

只要路徑中包含價值不為0的節點，則此**路徑健康**。  
假設路徑i是健康的，若j是i的子節點，則路徑j也一定是健康的。  

對於每個節點，我們有兩種選擇：  

1. 拿分數，子節點路徑健康**保持現狀**  
2. 不拿分數，所有子節點路徑都**變健康**  

我們沒有一定的標準去決定節點的分數拿不拿，故考慮dp。  

定義dp(i,health)：以節點i為子樹，且祖先節點的健康狀態為health，**保持所有路徑健康**的情況下，所能夠得到的最大分數。  
轉移方程式：max(拿分數, 不拿分數)  
拿分數=values[i]+sum(dp(j,True))；不拿分數=sum(dp(j,health))
base case：若i為葉節點，且祖先路徑都不健康，則必須**不拿values[i]**。  

每個路徑只有健康/不健康兩種狀態，每個狀態轉移兩次。  
時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        N=len(edges)+1
        g=[[] for _ in range(N)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        @cache
        def dp(i,fa,health):
            # leaf and no health
            # must keep values[i] to make it healthy
            if len(g[i])==1 and g[i][0]==fa and not health:
                return 0
            
            take=values[i]
            notake=0
            for j in g[i]:
                if j==fa:continue
                take+=dp(j,i,health)
                notake+=dp(j,i,True)
            return max(take,notake)
        
        ans=dp(0,-1,False)
        dp.cache_clear()
        
        return ans
```

另外一種方式是逆向思考，將問題轉換成：使得樹健康的**最小成本**。  
values總和扣掉最小成本正好就是能得到分數的最大值。  

定義dp(i)：使得以i為根的子樹健康的最小成本。  
轉移方程式：dp(i)=min(拿分數, 不拿分數)  
拿分數=values[i]；不拿分數=sum(dp(j))  
base case：當i為葉節點，必須**拿**才能使得樹健康。  

這裡的拿/不拿定義和上面相反，拿了才能使樹健康，不拿則必須讓子樹另外找分數拿。  
而且遞迴的順序固定，不需要記憶化。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        N=len(edges)+1
        g=[[] for _ in range(N)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
    
        # convert problem:
        # min cost to make tree healthy
        def dp(i,fa):
            if len(g[i])==1 and fa==g[i][0]: # leaf
                return values[i]
            
            take=values[i]
            notake=0
            for j in g[i]:
                if j==fa:continue
                notake+=dp(j,i)
            return min(take,notake)
        
        return sum(values)-dp(0,-1)
```
