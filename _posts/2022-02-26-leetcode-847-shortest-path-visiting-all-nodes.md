---
layout      : single
title       : LeetCode 847. Shortest Path Visiting All Nodes
tags 		: LeetCode Hard Graph BitManipulation BFS
---
每日題。吃了一個MLE，心服口服。 

# 題目
輸入一個無向圖graph，裡面有N個節點，分別為0~N-1編號。graph[i]代表節點0所鄰接的其他節點。  
你可以從任意點出發，每次移動一步，最少需要移動幾次才能走完所有的點。

# 解法 
看到graph要找最短路徑一定先想到BFS，這題測資寫了N<=12，那剛好可以使用bit mask來表示走過的點。  
首先確定節點數N，並以(1<<i)表示到過的點，走過則設為1，全部走完應為sum(1<<i FOR ALL 0<=i<N)。  
維護一個queue，初始化每一個節點為起點(起點,已訪問過的點,步數)加入queue中，開始做BFS。
每次取出一組數對，先將訪問過的點visited加上curr，步數+1，並檢查是否全部走完，若是則回步數；否則檢查curr的鄰接點，加入queue中。  

但是這樣給我噴一個記憶體超量，有沒有什麼方法可以減少queue的內容量？另外維護一個雜湊表seen，保存出現過的(curr,visited)數對，過濾掉已經走過的路線。
例：  
> graph = [[1,2,3],[0],[0],[0]]   
> curr=1, visited=0010, step=0  
> curr=0, visited=0011, step=1  (此時本有可能0,1,0,1無限循環，但(1,0011)在seen中所以忽略這條路線)  
> curr=2, visited=0111, step=2  
> curr=0, visited=0111, step=3  
> curr=3, visited=1111, step=4  

```python
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        end = 0
        q = deque()
        seen = set()
        for i in range(N):
            end |= 1 << i
            q.append((i, 0, -1))  # curr,visited,step

        while q:
            curr, visited, step = q.popleft()
            visited |= 1 << curr
            step += 1
            if visited == end:
                return step
            for adj in graph[curr]:
                if (adj, visited, step) not in seen:
                    seen.add((adj, visited, step))
                    q.append((adj, visited, step))

```
