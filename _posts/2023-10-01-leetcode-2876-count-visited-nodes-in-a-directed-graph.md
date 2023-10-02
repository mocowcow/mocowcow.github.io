---
layout      : single
title       : LeetCode 2876. Count Visited Nodes in a Directed Graph
tags        : LeetCode Hard Array Graph TopologySort DFS BFS
---
周賽365。圖論在最近Q4佔比很重，超過一半。  

## 題目

有個n節點的**有向圖**，有n條邊。節點編號由0到n-1。  

輸入陣列edges，其中edges[i]代表從節點i指向節點edges[i]的有向邊。  

你會在圖上執行以下流程：  

- 從節點x出發，不斷訪問下一個節點，直到抵達訪問過的節點為止  

回傳陣列answer，其中answer[i]代表從節點i出發，可以訪問到的**不同節點**個數。  

## 解法

n節點，每個節點都有一條邊，肯定會出現循環。  
題目保證edges[i]不會指向i自己，看起來不重要，但其實還滿重要的。  

這些點最後都會進到某個循環上。假設環上有5個點，則環上的這些點對應的ans[i]都是5。  
若某些點不在環上，而是移動x步後才進入環，則ans[i]就是進入環的步數，再加上環的大小。  

我們可以先找出所有位於環上的節點，填上答案，然後再處理其他非環節點。  
首先透過拓樸排序，把所有入度為0的節點逐一丟掉，最後剩下一堆入度不為0的節點，肯定位於環上。  
來一次dfs，找到環上的所有點，並填上答案，標記已訪問。重複直到處理過所有環。  
再來填上不位於環上的點，再寫另一個dfs求進入環的步數。  

如果有edges[i]指向自己，那麼他入度至少是1，沒辦法作為葉節點被刪掉。這題不需要處理此情形，還算是佛心。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        N=len(edges)
        ind=[0]*N
        
        for i,x in enumerate(edges):
            ind[x]+=1
            
        q=deque()
        for i in range(N):
            if ind[i]==0:
                q.append(i)
                
        while q:
            i=q.popleft()
            j=edges[i]
            ind[j]-=1
            if ind[j]==0:
                q.append(j)
                
        vis=[False]*N
        ans=[0]*N
        
        def dfs(i,cnt):
            if vis[i]:
                ans[i]=cnt
                return 
            vis[i]=True
            j=edges[i]
            dfs(j,cnt+1)
            ans[i]=ans[j]

        for i in range(N):
            if ind[i]==1 and not vis[i]:
                dfs(i,0)
                
        def dfs2(i):
            if vis[i]:
                return 
            vis[i]=True
            j=edges[i]
            dfs2(j)
            ans[i]=ans[j]+1
        
        for i in range(N):
            if ans[i]==0:
                dfs2(i)
                
        return ans
```

看了別人的解法，發現一些可以改進的地方。  

首先是計算環上節點數量的部分，為避免重複計算而維護的vis陣列，其實可以把入度的ind設成-1就好。  

求非環上節點答案，則可以建立反向的路徑，從環上開始dfs/bfs回去。  

```python
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        N=len(edges)
        ind=[0]*N
        rev=[[] for _ in range(N)]
        
        for i,x in enumerate(edges):
            ind[x]+=1
            rev[x].append(i)
            
        q=deque()
        for i in range(N):
            if ind[i]==0:
                q.append(i)
                
        while q:
            i=q.popleft()
            j=edges[i]
            ind[j]-=1
            if ind[j]==0:
                q.append(j)
                
        ans=[0]*N
        for i in range(N):
            if ind[i]<=0: # 0:not on ring, -1:visited
                continue
            
            q=deque()
            curr=i
            while True:
                ring.append(curr)
                ind[curr]=-1 # mark as visited
                curr=edges[curr]
                if curr==i:
                    break
                    
            q=deque([[x,len(ring)] for x in ring])
            while q:
                for _ in range(len(q)):
                    curr,cnt=q.popleft()
                    ans[curr]=cnt
                    for nxt in rev[curr]:
                        if ind[nxt]==0:
                            q.append([nxt,cnt+1])
        
        return ans
```
