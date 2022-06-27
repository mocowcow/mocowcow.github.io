--- 
layout      : single
title       : LeetCode 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
tags        : LeetCode Medium Array DFS
---
雙周賽81。最近的Q2難度真的明顯上升，這次也卡掉不少人。看到有人用並查集來做，超級殺雞用牛刀。

# 題目
有一個n節點的無向圖。輸入二維陣列edges，其中edges[i] = [ai, bi]代表連接兩節點的邊。  
求**無法連通的節點**所組成的數對有多少。  

# 解法
我覺得題目可以講得更清楚一點，例如節點0和2無法連通，但是數對[0,2]和[2,0]視為相同，只算一個數對。  

撰寫dfs函數用來計算和某點連通的所有節點數量，並將途中經過的所有點加入visited。  
遍歷所有點，若還沒訪問過，則以dfs計算連通點數量cnt，再以節點總數n扣掉visited的大小，得到剩餘未訪問節點的數量unvisited，則這cnt個點和剩下unvisited個點可以相互組成數對。  

```python
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ans=0
        visited=set()
        g=defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(i):
            visited.add(i)
            cnt=1
            for adj in g[i]:
                if adj not in visited:
                    cnt+=dfs(adj)
            return cnt
        
        for i in range(n):
            if i not in visited:
                cnt=dfs(i)
                unvisited=n-len(visited)
                ans+=cnt*unvisited
                
        return ans
```

有些數學比較好的朋友會發現，cnt乘上n-cnt所產生的數對，除2之後也是一樣的，這樣可以省去每次計算visited大小的成本，執行起來更快。

```python
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ans=0
        visited=set()
        g=defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(i):
            visited.add(i)
            cnt=1
            for adj in g[i]:
                if adj not in visited:
                    cnt+=dfs(adj)
            return cnt
        
        for i in range(n):
            if i not in visited:
                cnt=dfs(i)
                unvisited=n-cnt
                ans+=cnt*unvisited
                
        return ans//2
```