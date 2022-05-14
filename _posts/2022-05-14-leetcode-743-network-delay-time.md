--- 
layout      : single
title       : LeetCode 743. Network Delay Time
tags        : LeetCode Medium Graph Heap BFS
---
每日題。

# 題目
輸入整數n，代表n個節點，編號由1到n。另外陣列times代表有向邊，times[i]=(u,v,w)，節點u前往節點v的時間為w。  
我們將從k點發送信號，返回所有點接收到訊號的最短時間。若無法使全部點都收到訊號則回傳-1。  

# 解法
從k點發訊，找出每個點收到訊號的時間，完全就是dijkstra最短路徑演算法。  

因為節點是從1開始編號，我們手動把所有節點編號-1，變成以0開始計，比較方便處理。  
建立長度為n的陣列dis，代表從k前往各點的最低成本，初始值為inf。以k點出發做dijkstra，求出每個點的最低成本之後，遍歷一次dis，若中途出現值為inf，代表此點無法收到訊號，直接回傳-1；否則dis陣列中的最大值就是答案。

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g=defaultdict(list)
        for a,b,cost in times:
            g[a-1].append((b-1,cost))
            
        ans=0
        dis=[math.inf]*n
        h=[(0,k-1)]
        while h:
            time,curr=heappop(h)
            if time>=dis[curr]:
                continue
            dis[curr]=time
            for adj,cost in g[curr]:
                heappush(h,(time+cost,adj))
                
        for x in dis:
            if x==math.inf:
                return -1
            ans=max(ans,x)
            
        return ans
```

假設節點j是最後一個收到訊號的，題目只要求抵達j節點的時間，而不管先前其他點收訊時間。  
且heap永遠是取出最小的路徑成本，我們可以改用一個set紀錄那些節點已經訪問過，在dijkstra的途中，若n個節點全訪問過，則直接回傳當前時間；可用路徑處理完，還沒有回傳出去的話，代表有某些點收不到訊號，最後才回傳-1。

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g=defaultdict(list)
        for a,b,cost in times:
            g[a-1].append((b-1,cost))
            
        visited=set()
        h=[(0,k-1)]
        while h:
            time,curr=heappop(h)
            if curr in visited:
                continue
            visited.add(curr)
            if len(visited)==n:
                return time
            for adj,cost in g[curr]:
                heappush(h,(time+cost,adj))

        return -1
```