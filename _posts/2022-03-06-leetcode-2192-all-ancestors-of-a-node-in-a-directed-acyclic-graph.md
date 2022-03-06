---
layout      : single
title       : LeetCode 2192. All Ancestors of a Node in a Directed Acyclic Graph
tags 		: LeetCode Medium Graph DFS
---
雙周賽73。沒看清楚要排序，吃一個WA。

# 題目
有n個節點組成有向圖，編號0~n-1，輸入二維陣列edges，表示單向路線[fromNone,toNode]。  
求每個節點node的所有祖先，即從那些點出發可以抵達到node，並以遞增排序。

# 解法
又被python內建幫了一次。  
首先建立雜湊表parent，遍歷edges，紀錄每個節點的父節點。  
定義函數getAnc(node)代表node的所有祖先。node的所有祖先，包含node的所有父節點，以及所有父節點的祖先。  
所以祖先節點集合ancs先初始化為parent[node]，再加入所有父節點x的祖先getAnc(x)。  
最後對0~n-1全部呼叫getAnc即可。

```python
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parent = defaultdict(list)
        for a, b in edges:
            parent[b].append(a)

        @lru_cache(None)
        def getAnc(node):
            ancs = set(parent[node])
            for x in parent[node]:
                ancs.update(getAnc(x))
            return ancs

        ans = []
        for i in range(n):
            ans.append(sorted(getAnc(i)))

        return ans

```
