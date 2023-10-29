---
layout      : single
title       : LeetCode 2920. Maximum Points After Collecting Coins From All Nodes
tags        : LeetCode Hard Array Tree Graph DP Math
---
周賽369。久違的無BUG四題AK。  

## 題目

有棵n節點的無向樹，節點編號從0\~n-1，且根節點為0。  
輸入二維整數陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表a<sub>i</sub>和b<sub>i</sub>之間存在一條邊。  

另外還有長度n的整數陣列coins，其中coins[i]代表第i條邊上的硬幣數量。還有整數k。  

你從根節點出發收集所有硬幣。只有當某節點的所有祖先節點都已經收過硬幣，才能收集該節點的硬幣。  

有兩種方式可以收集節點i的硬幣：  

- 收集所有硬幣，但只會獲得coins[i] - k分。若k大於conins[i]，則會失去abs(coins[i] = k)分  
- 收集所有硬幣，但只會獲得floor(coins[i] / 2)分。若使用此方式，則在節點i為根的子樹中的所有節點j，coins[j]值都會變成floor(coins[j] / 2)  

求收集完**所有**硬幣後的**最大分數**。  

## 解法

最多n=10^5個節點，每個coins[i]最多會被減半10^5次，看起來一定超時。  
仔細觀察coins[i]=上限是10^4，log(10^4)=13.28..，最多被減半14次就會變成0了。  
這樣看來10^5 \* 14好像還算能接受了。  

定義dp(i,div)：以i為根，且已經被減半div次的子樹中，可獲得的最大分數。  
轉移方程式：dp(i,div) = max(op1, op2)  

時間複雜度O(n \* log MX)，其中MX為max(coins)。  
空間複雜度O(n \* log MX)。  

```python
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        N=len(coins)
        g=[[] for _ in range(N)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        @cache
        def dp(i,fa,div):
            val=coins[i]>>div
            op1=(val>>div)-k
            for j in g[i]:
                if j==fa:
                    continue
                op1+=dp(j,i,div)
                
            op2=val//2
            div2=min(14,div+1)
            for j in g[i]:
                if j==fa:
                    continue
                op2+=dp(j,i,div2)
            return max(op1,op2)            
        
        return dp(0,-1,0)
```
