---
layout      : single
title       : LeetCode 1557. Minimum Number of Vertices to Reach All Nodes
tags 		: LeetCode Easy Graph
---
臭狗昨天拔牙，住院一晚，今天中午回家了。拔了二十幾顆，每個牙根都黑黑爛爛，牙周病真可怕。  
大家都要好好刷牙，定期回診，健康最重要。

# 題目
一個有向無環圖，edges為路線，求最少要從哪幾個點出發才可以走完全部的點。

# 解法
以前做過，那時候還不知道何謂"入度"的概念。當時是使用set來排除可以抵達的點，概念其實相同。  
入度(indegree)指的是有多少個來源可以直接抵達目前的點，在topology sort的題型扮演著非常重要的角色。  
若某點有入口，則只需要從其上一個來源出發。我們只要找出沒有入口的所有點就是答案。  
處理每一個edge，來源方向不重要，只需要關注目的地，將其入度+1。最後入度為0的點就是答案。

```python
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0]*n
        for _, b in edges:
            indegree[b] += 1

        return [i for i in range(n) if indegree[i] == 0]

```
