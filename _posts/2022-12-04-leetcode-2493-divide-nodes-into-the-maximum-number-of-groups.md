--- 
layout      : single
title       : LeetCode 2493. Divide Nodes Into the Maximum Number of Groups
tags        : LeetCode Hard Array Graph HashTable DFS BFS
---
周賽322。坐牢坐牢的一天，雖然知道要拆成數個連通圖來做BFS，但一直想不出如何決定從哪個節點開始。  
答案非常有趣，希望讀者朋友先自己思考看看。  

# 題目
輸入正整數n，代表一個擁有n節點的無向圖，節點編號分別為1\~n。  

還有二維整數陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表a<sub>i</sub>, b<sub>i</sub>之間存在一條雙向道路。  
注意，輸入的無向圖可能**不完全連通**。  

試將此圖分割成m個群組，使得：  
- 每個節點都屬於其中一個群組  
- 對於每對連通的節點a<sub>i</sub>, b<sub>i</sub>來說，如果a<sub>i</sub>隸屬群組x，且b<sub>i</sub>隸屬群組y，那麼abs(x-y)等於1  

求最多可以分割成多少群組。如果無法分割則回傳-1。  

# 解法
有點類似上一題的[2492. minimum score of a path between two cities]({% post_url 2022-12-04-leetcode-2492-minimum-score-of-a-path-between-two-cities %})，需將所有連通的節點分組之後再進行切割。  

先寫一個dfs函數找出連通的圖，放到group陣列中，再寫一個bfs函數對每個連通圖進行分組切割，回傳切割完的數量。  

但根據bfs起點不同，得到的層數可能會不同，例如：  
> 以範例1來說  
> 從節點5出發，分組為[5],[1],[2,4],[3,6]  
> 從節點2出發，分組為[1],[5,2,4],[3,6]  

那麼讀者朋友想到判斷最佳起點的方法了嗎？  

答案就是：**暴力法全部試一次！**  

因為節點最多只有500個，最差情況下所有節點都連通，全部走一次也只要500\*500次運算，根本綽綽有餘。  
將所有連通圖的**最大切割出數**加總起來就是本題答案。  

時間複雜度為O(N\*(N+M))，其中N為節點總數，M為邊總數。空間複雜度是O(N+M)，為節點的visited陣列和建圖的儲存成本。  

```python
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        vis=[False]*(n+1)        
        ans=0
        g=defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(i):
            nodes.add(i)
            vis[i]=True
            for j in g[i]:
                if not vis[j]:
                    dfs(j)
        
        def bfs(i):
            vis2=[False]*(n+1)
            vis2[i]=True
            curr=set([i])
            lvl=0
            while curr:
                next=set()
                lvl+=1
                for i in curr:
                    for j in g[i]:
                        if j in curr:return inf
                        if not vis2[j]:
                            vis2[j]=True
                            next.add(j)
                curr=next
            return lvl      
        
        group=[]
        nodes=set()
        for i in range(1,n+1):
            if not vis[i]:
                nodes=set()
                dfs(i)
                group.append(nodes)
    
        ans=0
        for grp in group:
            mx=0
            for i in grp:
                mx=max(mx,bfs(i))
            ans+=mx
                
        return -1 if ans==inf else ans
```
