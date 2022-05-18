--- 
layout      : single
title       : LeetCode 1192. Critical Connections in a Network
tags        : LeetCode Hard Graph DFS
---
每日題。好久沒有出現沒做過的題，

# 題目
有n個伺服器，編號從0到n-1，透過好幾條無向的connections形成網絡，其中connections[i]=[a, b]表示伺服器a, b有連線。所有伺服器都可以透過網路，直接或是間接和其他伺服器溝通。  
**關鍵連線**指的是某些連線若刪除掉，會使某些伺服器失去連線。
以任意順序回傳網絡中的所有**關鍵連線**。

# 解法
想一段時間沒頭緒，就去找[題解](https://leetcode.cn/problems/critical-connections-in-a-network/solution/dfsfan-yi-liao-xia-ying-wen-ban-zui-jia-da-an-by-k/)看了。  
主要思想是給每個節點curr一個id，分別向鄰接點dfs找其最小的id值rootId，如果rootId小於等於當前id，代表形成了環，除了當前連線還有別條路能夠回來，所以當前連線並非必要，可以刪除。最後回傳整個curr連線中出現過的最小id，即minId，供其他dfs使用。  

題目傳入的connections並不保證節點出現順序，所以一律將較小的節點放在前方，轉成tuple後，才能成功放入set中。

```python
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g=defaultdict(list)
        critical =set()
        id=[-1]*n
        convert=lambda a,b:tuple(sorted([a,b]))
        for a,b in connections:
            g[a].append(b)
            g[b].append(a)
            critical.add(convert(a,b))
            
        def dfs(curr,i,prev):
            if id[curr]!=-1:
                return id[curr]
            id[curr]=i
            minId=i
            for adj in g[curr]:
                if adj==prev:
                    continue
                rootId=dfs(adj,i+1,curr)
                if rootId<=i:
                    critical.remove(convert(curr,adj))
                    minId=rootId
            return minId
        
        dfs(0,0,-1)
        
        return critical
```


```python
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g=defaultdict(list)
        critical=[]
        id=[-1]*n
        for a,b in connections:
            g[a].append(b)
            g[b].append(a)

            
        def dfs(curr,currId,prev):
            if id[curr]!=-1:
                return id[curr]
            id[curr]=currId
            minId=currId
            for adj in g[curr]:
                if adj==prev:
                    continue
                rootId=dfs(adj,currId+1,curr)
                if currId+1==rootId:
                    critical.append([curr,adj])
                minId=min(minId,rootId)
            return minId
        
        dfs(0,0,-1)
        
        return critical
```

也可以改成加入關鍵連線的方式。  
當某個鄰接點adj的最小id=當前id+1時，代表這兩點有直接連線。  
需要注意的是，id相差超過1，代表adj已經透過其他點建立連線，所以curr和adj的連線並非必要，所以不能以currId<rootId作為判斷條件。

```python
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g=defaultdict(list)
        critical=[]
        id=[-1]*n
        for a,b in connections:
            g[a].append(b)
            g[b].append(a)
            
        def dfs(curr,currId,prev):
            if id[curr]!=-1:
                return id[curr]
            id[curr]=currId
            minId=currId
            for adj in g[curr]:
                if adj==prev:
                    continue
                rootId=dfs(adj,currId+1,curr)
                if currId+1==rootId:
                    critical.append([curr,adj])
                minId=min(minId,rootId)
            return minId
        
        dfs(0,0,-1)
        
        return critical
```