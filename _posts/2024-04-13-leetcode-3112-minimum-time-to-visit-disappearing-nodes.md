---
layout      : single
title       : LeetCode 3112. Minimum Time to Visit Disappearing Nodes
tags        : LeetCode Medium Array Graph BFS Heap
---
雙周賽 128。這題也是很良心，竟然沒有讓消失時間設成 0，不然大概會有一堆人吃 WA。  

## 題目

有個 n 節點的無向圖。  
輸入二維整數陣列 edges，其中 edges[i] = [u<sub>i</sub>, v<sub>i</sub>, length<sub>i</sub>]，代表 a<sub>i</sub> 和 b<sub>i</sub> 之間存在一條邊，所需移動時間為 length<sub>i</sub>。  

另外還有整數陣列 disappear，其中 disappear[i] 代表節點 i 消失的時間點，消失後就不能再訪問了。  

注意：圖可以會被分割成不連通的樣子，而且兩點之間可能有重邊。  

回傳陣列 answer，其中 answer[i] 代表從節點 0 出發，抵達節點 i 的最短時間。若無法抵達則 answer[i] 設為 -1。  

## 解法

dijkstra 最短路變形題，只多了一個 disappear 限制到達時間。  

初始化將節點 0 加入 heap。  
每次取出抵達時間最短的節點 i，如果訪問過或是超時則不管；否則將所有相鄰的節點 j 加入 heap。  

時間複雜度 O(E log E)，其中 E = len(edges)。  
空間複雜度 O(n + E)。  

```python
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b, c in edges:
            g[a].append([b, c])
            g[b].append([a, c])
            
        ans = [-1] * n
        h = []
        heappush(h, [0, 0]) # time, node
        while h:
            time, i = heappop(h)
            if ans[i] != -1 or time >= disappear[i]:
                continue
            ans[i] = time
            
            for j, cost in g[i]:
                new_time = time + cost
                heappush(h, [new_time, j])
        
        return ans
```
