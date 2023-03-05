--- 
layout      : single
title       : LeetCode 2581. Count Number of Possible Root Nodes
tags        : LeetCode Hard Array Graph Tree HashTable DP
---
雙周賽99。不小心開了10^5\*10^5的陣列，結果不噴MLE而是TLE。我想了半天不理解為什麼O(N)解不會過，後來才發現是被陣列初始化時間卡死，太智障了。  

# 題目
Alice有一顆n節點的無向樹，節點編號分別為0\~n-1。二維整數陣列edges代表了n-1個邊，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]代表存在於a<sub>i</sub>和b<sub>i</sub>中間的邊。  

Alice要求Bob找到此樹的根節點，並允許他**猜測**樹的構造。每次猜測，Bob會：  
- 選擇兩個**不相等**的選擇兩個不重複的整數u和v，且u和v中必定存在一條邊  
- Bob會猜測u是v的**父節點**  

Bob的猜測由二維整數陣列guesses表示，其中guesses[j] = [u<sub>j</sub>, v<sub>j</sub>]代表Bob猜u<sub>j</sub>是v<sub>j</sub>的父節點。  

但是Alice很懶，只願意回答這些猜測中**至少** 猜對幾個。  

輸入二維整數陣列edges和edges，還有整數k，求有**多少節點**有可能作為根節點。若無則回傳0。  

# 解法
相似題[834. sum of distances in tree]({% post_url 2022-05-07-leetcode-834-sum-of-distances-in-tree %})。  

根據選取的根節點不同，某些節點的父子關係會改變。例如：  
> 0--1--2  
> 0為根節點時：0 -> 1 -> 2  
> 1為根節點時：0 <- 1 -> 2  
> 2為根節點時：0 <- 1 <- 2  

發現只有在子節點**代替**父節點成為根的時候，雙方的上下關係才會改變。  
假設只有兩個節點，Bob只猜了[0,1]，且至少猜對一次時：  
> 0為根節點時：0 -> 1  
> [0,1]猜對了，共猜對一次  
> 接下來以1代替0作為根：0 <- 1  
> 本來猜對的[0,1]沒了，但Bob沒猜[1,0]，所以猜對的剩下零個  
> 只有0可以做為根節點  

所以當將根節點i傳給子節點j時，j為根總次數=i為根總次數-損失的猜對數+新增的猜對數。  

維護陣列cnt，其中cnt[i]代表以i為根時的猜對次數。  
任選一個節點作為根先做一次dfs求出cnt[i]。方便起見選擇0。  
這時只有cnt[0]的值是正確的，我們必須透過cnt[0]的值去推算出其他cnt[i]。  

再次從0開始做第二次dfs，將根節點i的所有子節點j交換，帶入剛才推算出的公式，更新正確的cnt[i]。如果猜隊至少k個，則答案加一。  

時間複雜度O(N+M)，其中N為節點數和邊數(edges長度+1)，M為guesses長度。空間複雜度O(N+M)。  

```python
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        N=len(edges)+1
        g=defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        ok=[Counter() for _ in range(N)]
        for u,v in guesses:
            ok[u][v]=1
        
        ans=0
        cnt=[0]*N

        def dfs(i,fa):
            for j in g[i]:
                if j==fa:continue
                cnt[i]+=dfs(j,i)+ok[i][j]
            return cnt[i]
            
        dfs(0,-1)
    
        def dfs2(i,fa):
            nonlocal ans
            if fa!=-1:
                cnt[i]=cnt[fa]-ok[fa][i]+ok[i][fa]
            if cnt[i]>=k:
                ans+=1
            for j in g[i]:
                if j==fa:continue
                dfs2(j,i)
        
        dfs2(0,-1)
                        
        return ans
```
