--- 
layout      : single
title       : LeetCode 1202. Smallest String With Swaps
tags        : LeetCode Medium Array String DFS UnionFind
---
每日題。好久沒有在每日題出現併查集，我也好一段時間沒寫過相關題，且這篇是我第一篇寫的並查集題解！  
雖然說是併查集題，但我今天是先用dfs把它解決的。我認為一個好的題目不會被侷限於單一一種解法，可能因為大多數人都如此覺得，這題的讚數才會破兩千。 

# 題目
輸入字串s以及二維陣列pairs，pairs[i]由[a,b]兩個數組成，代表s中某字元的索引位置。  
你可以對pairs中任意一組索引位置的字元交換**任意次**，求s經過交換後可以得到的**最小字典順序**。

# 解法
這種說交換任意次的通常就是排序的意思，真的去一個個交換肯定會死得很慘。  
可以先將s的每個位置當成節點，pairs想成節點間連線，能連通的節點之間都可以互相交換。  
概念釐清之後開始實作，需要一個雜湊表g紀錄每個節點的相鄰節點，雜湊表group紀錄可以連通的節點，陣列used表示該點是否已經處理過。  

透過dfs將所有能連通的點i標記加入組別id，並將used[i]改為true，避免重複處理。  
分組完，把每組的字元和索引分別排序，填入相對應位置中。

```python
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N=len(s)
        g=defaultdict(list)
        group=defaultdict(list)
        used=[False]*N
        ans=['']*N
        for a,b in pairs:
            g[a].append(b)
            g[b].append(a)

        # mark position i with group id
        def dfs(i,id):
            group[id].append(i)
            used[i]=True
            for j in g[i]:
                if not used[j]:
                    dfs(j,id)
                    
        # group postitions   
        for i in range(N):
            if not used[i]:
                dfs(i,i)
                
        # sort by group
        for gp in group:
            idx=sorted(group[gp])
            cs=[]
            for i in idx:
                cs.append(s[i])
            cs.sort()
            for i,c in zip(idx,cs):
                ans[i]=c
            
        return ''.join(ans)
```

既然都說是併查集，就再來寫一次。思維和上面一樣，只是使用不同的資料結構來記錄連通。  
差別在於上面方法是將依照分組將答案填入，下面改用成對某索引位置i找到對應的組別，才取出字元。

```python
class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [0]*n
        for i in range(n):
            self.parent[i] = i

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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N=len(s)
        uf=UnionFind(N)
        group=defaultdict(list)
        ans=[]
        for a,b in pairs:
            uf.union(a,b)
            
        for i in range(N):
            group[uf.find(i)].append(s[i])
            
        for k in group:
            group[k].sort(reverse=True)
            
        for i in range(N):
            ans.append(group[uf.find(i)].pop())
            
        return ''.join(ans)
```