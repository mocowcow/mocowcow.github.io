---
layout      : single
title       : LeetCode 2976. Minimum Cost to Convert String I
tags        : LeetCode Medium Array String Graph DP
---
周賽377。

## 題目

輸入兩個長度n，只由小寫字母組成的字串source和target。  
另外還有兩個字元陣列original, changed和整數陣列cost。其中cost[i]代表將original[i]改成changed[i]的成本。  

最初你擁有字串source。  
每次操作，如果滿足original[j]=x, changed[j]=y, cost[j]=z，你可以從字串中的**任一**個字元x改成y，並支付成本z。  

求將source變成target的**最小成本**；若不可能，則回傳-1。  

注意：可能存在兩個索引i, j，其中original[j] == original[i]且changed[j] == changed[i]。也就是兩種修改方向相同，但成本不一定相同。

## 解法

總共只有26種字母，但不限制修改次數。  
當你要把a改成b，可以直接a -> b，也可以是a -> x -> b。  

把字母當成端點，可以視作一個有向圖，修改成本就是路徑成本。  
先求出最短路徑各字母之間的最短路徑，再來遍歷source/target，計算總成本。  

我們需要所有端點之間的最短路，而且端點只有26個，故選擇floyd-warshall。  
先遍歷所有的有向邊，只保留最短者。然後枚舉中繼點、更新最短路。  

最後把每個需要修改的字母成本加總即可。  

時間複雜度O(n^3 + E)。其中n=26個字母，E=len(cost)。  
空間複雜度O(n^2)。  

```python
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n=26
        dp=[[inf]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=0
            
        for a,b,c in zip(original,changed,cost):
            a=ord(a)-97
            b=ord(b)-97
            if c<dp[a][b]:
                dp[a][b]=c
                
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    new_dist=dp[i][k]+dp[k][j]
                    if new_dist<dp[i][j]:
                        dp[i][j]=new_dist
                        
        ans=0
        for s,t in zip(source,target):
            s=ord(s)-97
            t=ord(t)-97
            ans+=dp[s][t]
            
        if ans==inf:
            return -1
        
        return ans
```
