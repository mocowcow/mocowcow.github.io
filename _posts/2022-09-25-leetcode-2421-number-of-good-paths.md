--- 
layout      : single
title       : LeetCode 2421. Number of Good Paths
tags        : LeetCode Hard Array UnionFind Graph Tree HashTable
---
周賽312。真的是吐血了，寫一半有人打電話來，寫出一坨狗屎code，分心狀況下根本沒辦法debug。後來才發現我把for寫成if，整題就毀了，好慘。  

# 題目
有一棵樹(無向無環)由n個節點組成，編號從0到n-1，且正好有n-1條邊。  
輸入長度n的整數陣列vals，其中vals[i]表示第i個節點的值。還有一個二維整數陣列edges，其中edges[i] = [ai, bi]，表示連接節點ai和bi的無向邊。  

一條**好的路徑**必須條滿足以下條件：  
- 起始節點和結束節點具有相同的值  
- 起始節點和結束節點之間的所有節點的值都小於等於起始節點的值(即起始節點的值應該是路徑中的最大值)  

求有多少條**好的路徑**。  
注意，路徑及其反向被視為同一路徑。例如[1,2]和[2,1]是相同的。單個節點也被算是有效路徑。  

# 解法
總共有3\*10^4個節點，如果用普通的bfs一定會超時，要想想別的方法。  
而且另一個困難點在於**不知道什麼時候會碰到更大的節點值**，這樣非常沒有效率。  

那如果先從值較小的節點開始連通，是不是就可以保證能走到的節點一定小於等於本身？  
這時候需要快速查找節點是否相連的資料結構：併查集。  

為了使相鄰節點連通，先把edges改成存成graph，方便查詢。再依照節點值將各節點分組裝入雜湊表d。  
之後依照節點值由小到大，加入值為k的節點。然後找出有幾個連通區域、各區域內有多少節點，計算出有效路徑並加入答案。  
因為單一節點也算是有效路徑，最後記得將答案加上節點數量。  

併查集時間複雜度O(N)，但有可能各節點的值完全不重複，排序需要O(N log N)。空間需要保存各節所屬的root，並對edges建圖，複雜度O(N+M)。  

```python
class UnionFind:
    def __init__(self):
        self.parent={}

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        g=defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            
        N=len(vals)
        uf=UnionFind()
        d=defaultdict(list)
        ans=0
        
        for i,v in enumerate(vals):
            d[v].append(i)
            
        for k in sorted(d.keys()):
            for i in d[k]:
                uf.parent[i]=i
            for i in d[k]:
                for x in g[i]:
                    if x in uf.parent:
                        uf.union(x,i)

            grp=Counter()
            for i in d[k]:
                grp[uf.find(i)]+=1
            for v in grp.values():
                ans+=v*(v-1)//2

        return ans+len(vals)
```
