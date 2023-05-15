--- 
layout      : single
title       : LeetCode 2685. Count the Number of Complete Components
tags        : LeetCode Medium Array Graph DFS
---
周賽345。又是沒有hard的周賽，真的每次碰到這種排名都會很慘。  

# 題目
輸入整數n，代表有個n節點的無向圖，編號分別從0\~n-1。  
輸入二維整數陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表a<sub>i</sub>和b<sub>i</sub>之間存在一條邊。 

求有多少**完全連通塊**。  

若一個子圖中任意兩點之間都存在路徑，且不與子圖外的節點共享邊，則稱為**連通塊**。  
若一個連通塊之間任意兩點都存在邊，則稱為**完全連通塊**。  

# 解法
一個完全連通塊若有v個節點，則每個節點都必須連接其於v-1個節點，共有v\*(v-1)條邊。但邊是無向的，[a,b]和[b,a]視為同一條，所以實際上是v\*(v-1)/2條邊。  

首先建圖，維護每個節點i的鄰接點，同時可以知道有幾條邊。  
撰寫一個dfs(i)函數，計算一個連通塊中的節點和邊數。  

遍歷每個節點，若還沒訪問過，則代表是一個全新的連通塊，則進行dfs求出節點數v以及邊數e。  
如果去重後的邊數正好為上面提到的v\*(v-1)/2，代表是**完全連通塊**，答案加1。  

時間複雜度O(n + M)，其中M為edges大小。  
空間複雜度O(n + M)。  

```python
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g=[[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            
        vis=[False]*n
        
        def dfs(i):
            nonlocal e,v
            vis[i]=True
            v+=1
            e+=len(g[i])
            for j in g[i]:
                if not vis[j]:
                    dfs(j)
        
        ans=0
        for i in range(n):
            if not vis[i]:
                e=v=0
                dfs(i)
                if e==v*(v-1): # e//2 == v*(v-1)//2
                    ans+=1
            
        return ans
```
