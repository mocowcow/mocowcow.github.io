---
layout      : single
title       : LeetCode 2924. Find Champion II
tags        : LeetCode Medium Array Graph DFS
---
周賽370。剛開始想成拓樸排序，想說Q2怎麼會出這種，還真不好做。當然是有更簡單的方法。  

## 題目

有n個隊伍在比賽，編號分別為0到n-1。每個隊伍都屬於**有向無環圖**中的一個節點。  

輸入整數n，和長度為m的二維整數陣列edges，其中edges[i] = [u<sub>i</sub>, v<sub>i</sub>]，代表u<sub>i</sub>和v<sub>i</sub>之間存在一條有向邊。  

一條從a到b的有向邊代表隊伍a比隊伍b**更強**；反之，隊伍a比隊伍b**更弱**。  

如果對於隊伍a來說，不存在任意隊伍b比a更強，則a是比賽的**冠軍**。  

求這場比賽的冠軍隊伍。若不存在，則回傳-1。  

## 解法

從範例可以很清楚看到，若1比2強，且0比1強，則0也比2強。  
這種關係叫做**遞移性**(Transitive relation)。  
在此感謝我的**離散數學老師**。  

因此，冠軍一定會比其他所有的隊伍還強。  
從有向圖的角度來看，從冠軍出發，肯定能夠抵達任意一個點。  

枚舉隊伍i，試著從i開始出發，遍歷整個圖。  
若能成功抵達n個節點，則代表他就是冠軍。  

時間複雜度O(n^2)。  
空間複雜度O(n+m)。  

```python
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g=[[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)

        for i in range(n):
            vis=[False]*n
            
            def dfs(i):
                res=1
                for j in g[i]:
                    if not vis[j]:
                        vis[j]=True
                        res+=dfs(j)
                return res

            # no cycle
            # unnecessary to mark i as visited
            if dfs(i)==n:
                return i
            
        return -1
```
