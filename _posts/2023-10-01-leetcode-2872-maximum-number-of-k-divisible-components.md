---
layout      : single
title       : LeetCode 2872. Maximum Number of K-Divisible Components
tags        : LeetCode Hard Array Math Graph Tree DFS BFS TopologySort
---
雙周賽114。最近真的腦子不太行，搞個麻煩的拓樸排序搞半天，最緊急改成dfs才3分鐘就寫出來，可惜提交完已經結束1分鐘了。  

## 題目

有棵無向的樹，共n個節點，編號從0到n-1。  
輸入整數n和大小為n-1的二維整數陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表a<sub>i</sub>和b<sub>i</sub>之間存在一條邊。  

另外還有長度n的整數陣列values，其中values[i]代表第i個節點的值。  
還有整數k。  

一個**有效的分割**，指的是刪除某些邊(也可以不刪)後，使得樹成為數個連通塊，且每個連通塊中的節點值總和可以被k整除。  

求任意有效的分割中，**最多**可以分割成多少連通塊。  

## 解法

題目保證sum(values)一定可被k整除。  

思路是從葉節點開始剝皮，只要總和可被k整除，就分割整個子樹；否則將總和值留給父節點使用。  
一個連通塊本是k的倍數，扣掉同為k個倍數的某個子樹，剩下的依然是k的倍數。  

維護陣列tot，其中tot[i]代表以i為根節點的子樹的值總和。  
以dfs實現上述分割子樹的方法，並更新tot[i]。  
最後能被k整除的tot[i]個數就是答案。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g=[[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        tot=[0]*n
        
        def dfs(i,fa):
            tot[i]=values[i]
            for j in g[i]:
                if j==fa:
                    continue
                dfs(j,i)
                tot[i]+=tot[j]%k
            
        dfs(0,-1)
        
        return sum(x%k==0 for x in tot)
```

拓樸排序確實可以做，但是很麻煩。  

樹是無向的，不分出入度(degree)，只要度為1就是葉節點。  
但在n=1的特殊情況時，度會是0，所以初始找葉節點的時候要涵蓋到這點，或是特殊判斷n=1回傳1。  

將葉節點用剩的值留給他的父節點，和dfs差不多，但要記錄哪些節點已經訪問過，避免values的值被誤加。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g=[[] for _ in range(n)]
        dg=[0]*n
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            dg[a]+=1
            dg[b]+=1
            
        vis=[False]*n
        q=deque()
        for i in range(n):
            if dg[i]<=1: # when n=1, dg[0] will be 0
                q.append(i)
                
        while q:
            for _ in range(len(q)):
                i=q.popleft()
                vis[i]=True
                for j in g[i]:
                    if vis[j]: # prevent repeated values
                        continue
                    values[j]+=values[i]%k
                    dg[j]-=1
                    if dg[j]==1:
                        q.append(j)
                        
        return sum(x%k==0 for x in values)
```
