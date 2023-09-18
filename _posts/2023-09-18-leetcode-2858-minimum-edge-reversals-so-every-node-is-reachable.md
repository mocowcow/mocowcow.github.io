---
layout      : single
title       : LeetCode 2858. Minimum Edge Reversals So Every Node Is Reachable
tags        : LeetCode Hard Array Tree Graph DFS DP
---
雙周賽113。比較簡單的換根dp基本款，甚至寫起來比Q2還快。  

## 題目

一個n節點的**簡單有向圖**，編號由0到n-1。若此圖無向，則形成一棵**樹**。  

輸入整數n，以及二維整數陣列edges，其中edges[i] = [u<sub>i</sub>, v<sub>i</sub>]，代表一條有向邊從u<sub>i</sub>指向v<sub>i</sub>。  

一次**反轉**可以改變邊的方向，也就是將u<sub>i</sub>往v<sub>i</sub>，改成v<sub>i</sub>往u<sub>i</sub>。  

對於每個節點i，分別計算使i能夠前往其餘任意節點的**最少反轉次數**。  

回傳整數陣列answer其中answer[i]代表以節點i為起點，使得其餘所有節點可到達的**最少反轉次數**。  

## 解法

一棵樹，代表任意兩節點之間只存在唯一一條路徑。  

若從節點i出發前往j，則路徑上的所有反向邊都需要**反轉**。答案求的就是以i為根節點的樹中，所存在的**反向邊**數量。  

首先建圖，對於每條邊加入一個參數，用1代表正向，-1代表反向。  
先以0為根做一次dfs，求出以0為根節點的樹中總共有多少反向邊。  

維護陣列neg，其中neg[i]代表以i為根時的反向邊數量，再來第二次dfs。  
對於i的子節點j來說，樹中的邊大致上都是相同的，只有(i, j)這條邊的方向受到改變。  
若(i, j)是正向，則neg[j]會比neg[j]多一條反向；反之，若(i, j)是反向，則neg[j]會比neg[i]少一條反向。  

時間複雜度O(n)。  
空間複雜度O(n)。  

```python
class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g=[[] for _ in range(n)]
        for a,b in edges:
            g[a].append([b,1]) # pos
            g[b].append([a,-1]) # neg
            
        def dfs(i,fa):
            cnt=0
            for j,dir in g[i]:
                if j==fa:
                    continue
                if dir==-1:
                    cnt+=1
                cnt+=dfs(j,i)
            return cnt
        
        neg=[0]*n
        neg[0]=dfs(0,-1)

        def dfs2(i,fa):
            for j,dir in g[i]:
                if j==fa:
                    continue
                neg[j]=neg[i]
                if dir==1:
                    neg[j]+=1
                else:
                    neg[j]-=1
                dfs2(j,i)
        
        dfs2(0,-1)
        
        return neg
```
