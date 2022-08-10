--- 
layout      : single
title       : LeetCode 947. Most Stones Removed with Same Row or Column
tags        : LeetCode Medium Array UnionFind Graph DFS
---
LC75學習計畫。需要一點考察力的併查集題目，不過出題者應該只是想考簡單的DFS而已。  

# 題目
在一個2D平面上，將n塊石頭放在某些整數坐標點，每個坐標點最多放一塊石頭。  
如果某塊石頭與同行或同列上還有其他石頭，則可以被移除。  

輸入長度為n的陣列stones，其中stones[i] = [xi, yi]表示第i個石頭的座標，回傳最多可以移除幾顆石頭。  

# 解法
若有5顆石頭都在同一行，那麼我們從邊緣開始移除，最多可以移除4顆；若有9顆石頭排成正方形，一樣從邊角外圍開始移除，最多可以移除8顆。只要從最外圍開始移除石頭，那麼X顆形成的連線最多可以移除掉X-1顆。  

如此一來，只要找出有多少個獨立的群組，以石頭總數N扣掉群組數量就是可移除的石頭數。  
使用併查集紀錄每個座標[r,c]所屬的群組。兩兩列舉所有石頭，若同行或是同列，則將兩石頭聯集。每一次聯集代表多出一顆可以移除的石頭，故cnt+1。  
最後回傳cnt就是答案。列舉石頭的時間複雜度為O(N^2)，加上聯集時間其實效率很差，如果測資兇狠一點或許就沒辦法通過。  

```python
class UnionFind:
    def __init__(self):
        self.parent={}
        self.cnt=0

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.cnt+=1
            self.parent[px] = py

    def find(self, x):
        if x not in self.parent:
            self.parent[x]=x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N=len(stones)
        uf=UnionFind()
        for i in range(N):
            for j in range(i+1,N):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    uf.union(tuple(stones[i]),tuple(stones[j]))
        
        return uf.cnt
```

上面方法有點多此一舉，既然都要O(N^2)，不如直接普通的DFS，找出石頭群組總數。  

```python
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N=len(stones)
        group=0
        visited=set()
        
        def dfs(i):
            visited.add(i)
            for j in range(N):
                if j in visited:continue
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    dfs(j)
        
        for i in range(N):
            if i not in visited:
                dfs(i)
                group+=1
                
        return N-group
```

最後是併查集的最佳解法，複雜度只要O(N)。  

因為x和y軸座標最大只會到10^4，所以我們只要對y軸加上大於10^4的偏移值，就可以避免行列衝突，問題簡化成將2*10^4個群組相互聯集。  
列舉每個石頭，把所屬的行列[r,c]聯集就好，但是行數c要記得加上偏移值。  
全部聯集完後，檢查總共剩下多少個不同的群組，以石頭總數N扣掉群組數即為答案。  

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
        if x not in self.parent:
            self.parent[x]=x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N=len(stones)
        uf=UnionFind()
        for r,c in stones:
            uf.union(r,c+10005)
        
        group=set(uf.find(x) for x in uf.parent)
        return N-len(group)
```