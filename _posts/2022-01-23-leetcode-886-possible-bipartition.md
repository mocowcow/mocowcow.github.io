---
layout      : single
title       : LeetCode 886. Possible Bipartition
tags 		: LeetCode Medium DFS BFS Graph
---
# 題目
有n個人，輸入dislikes陣列，表示a討厭b，不想跟對方在一起，求是否有辦法把所有人成功分為兩組。

# 解法
先建立無向圖hates，紀錄互斥的對象，再用陣列group紀錄分組狀態，-1表未分組，可分入0或是1組(XOR處理比較方便)。  
依序檢查每個人是否已經有組，否則一律編入0組，而與其互斥的對象則編入1組，以此類推。若中途分組失敗回傳false。

DFS版本 
```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1 or not dislikes:
            return True

        group = [-1]*(n+1)
        hates = defaultdict(list)
        for a, b in dislikes:
            hates[a].append(b)
            hates[b].append(a)

        def canGroup(idx, g):  # try assign group[idx] to g
            if group[idx] != -1:
                return group[idx] == g
            group[idx] = g
            for h in hates[idx]:
                if not canGroup(h, g ^ 1):
                    return False
            return True

        for i in range(1, n+1):
            if group[i] == -1 and not canGroup(i, 0):
                return False

        return True

```

BFS版本
```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1 or not dislikes:
            return True

        group = [-1]*(n+1)
        hates = defaultdict(list)
        for a, b in dislikes:
            hates[a].append(b)
            hates[b].append(a)

        for i in range(1, n+1):
            if group[i] != -1:  # visited
                continue
            group[i] = 0
            q = deque([i])
            while q:
                curr = q.popleft()
                for h in hates[curr]:
                    if group[h] == -1:
                        group[h] = group[curr] ^ 1
                        q.append(h)
                    elif group[curr] == group[h]:
                        return False

        return True
```
