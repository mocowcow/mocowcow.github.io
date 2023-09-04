---
layout      : single
title       : LeetCode 2846. Minimum Edge Weight Equilibrium Queries in a Tree
tags        : LeetCode Hard Array Tree PrefixSum BitManipulation BinaryLifting
---
周賽361。上週才考過倍增，這週馬上就考進階用法，真變態。  
雖說是進階版，但LCA倍增其實算是競賽的常見題目，網路上隨便都找得到模板可以套用。可能因此通過人數比上次還多。  

## 題目

有一個n節點的無向樹，節點編號分別為0到n-1。  
輸入二維整數陣列edges，其中edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]，代表節點u<sub>i</sub>和v<sub>i</sub>之間存在一條權重為w<sub>i</sub>邊。  

另外還輸入長度m的二維整數陣列queries，其中queries[i] = [a<sub>i</sub>, b<sub>i</sub>]。  
對於每個查詢queries[i]，要求出使得a<sub>i</sub>到b<sub>i</sub>路徑上的權重相等所需**最少操作次數**。  
每次操作，你可以將任意邊上的權重改變成任意值。  

注意：  

- 每次操作都是獨立的。意味著每次操作前，所有邊的權重都會恢復成初始值  
- a<sub>i</sub>到b<sub>i</sub>的路徑是由**不同**的節點序列所組成，從a<sub>i</sub>開始，b<sub>i</sub>結束。且序列中相鄰的節點都共享一條邊  

回傳長度m的陣列answer，其中answer[i]代表第i次查詢的答案。  

## 解法

雖然說是一棵樹，但沒指定根節點，方便起見都把節點0當作根。  

要使得路徑上的權重相等，又要操作次數最小，那就只能把所有權重都改成出現次數最多的那個。  
但是怎麼求a和b之間的路徑？先找他們的LCA(最近公共祖先)，從LCA到a的路徑加上LCA到b的路徑，就是完整的路徑。  

傳統的LCA算法是先使ab深度相等，然後兩者同時向父節點移動，直到ab相等，當前節點就是LCA。  
但是本題中節點數量高達10^4，最壞形況下是linked list，每次找LCA都要10^4次移動。查詢也是10^4量級，必須要想辦法優化LCA的算法。  

找LCA分成兩個步驟：平衡深度、同時上移。  
我們知道a和b深度的差為diff，將diff分解成數個2^j次移動，就是基本款的倍增應用。  
但是又怎麼知道要跳多少步才到LCA？這時又要導入二分思想：  

- 跳x步後，a和b相等，代表已經找到LCA或是LCA的祖先。可以保證LCA在當前節點，或是在下方  
- 若a和b不相等，則代表還沒找到LCA。可以保證LCA一定在上方  

只要找到深度最低，且不是a!=b的位置，再往上一步，就是LCA了。有點類似bisect_right或是upper_bound之後再減1的概念。  
接著剛才講的，如果x步會跳到祖先節點，那目標最多只需要x-1步。所以從最大的2^j開始往下檢查，如果跳2^j會相同，就不跳；不會相同就跳。  
最後會停在LCA的下方，再往上跳一步就大功告成。  

注意：在a或b本身就是LCA的情況下，倍增平衡完深度就可以直接回傳。  

最後處理每個查詢[a, b]：  

1. 先找到ab的lca  
2. 求a到lca，再從lca到b的路徑  
3. 找到最高的權重出現次數max_w，把總邊數tot扣掉max_w就是答案  

預處理倍增O(n log n)，每次查詢O(log n)，整體時間複雜度O( n log n + Q log n )。  
空間複雜度O(n log n)。  

```python
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        m=n.bit_length()
        g=[[] for _ in range(n)]
        for a,b,w in edges:
            g[a].append([b,w-1])
            g[b].append([a,w-1])
            
        pos=[[-1]*m for _ in range(n)]
        dep=[0]*n
        weight=[None]*n
        weight[0]=[0]*26
        
        # build depth and weights
        def dfs(i,fa,d):
            pos[i][0]=fa
            dep[i]=d
            for j,w in g[i]:
                if j==fa:
                    continue
                weight[j]=weight[i][:]
                weight[j][w]+=1
                dfs(j,i,d+1)
        
        dfs(0,-1,0)
        
        # build binary lifting
        for j in range(1,m):
            for i in range(n):
                fa=pos[i][j-1]
                if fa!=-1:
                    pos[i][j]=pos[fa][j-1]
        
        def get_lca(x,y):
            if dep[x]>dep[y]:
                x,y=y,x
                
            # make x and y same depth
            # by move diff steps from y
            diff=dep[y]-dep[x]
            for j in range(m):
                if diff&(1<<j):
                    y=pos[y][j]
                    
            # found lca
            if x==y:
                return x
            
            # find lowest non-lca
            for j in reversed(range(m)):
                if pos[x][j]!=pos[y][j]:
                    x=pos[x][j]
                    y=pos[y][j]
                    
            # now x and y are below lca 1 step
            # one more step to lca
            return pos[x][0]
        
        ans=[]
        for a,b in queries:
            lca=get_lca(a,b)
            tot=dep[a]+dep[b]-dep[lca]*2
            w_sum=[x1+x2-x3*2 for x1,x2,x3 in zip(weight[a],weight[b],weight[lca])]
            ans.append(tot-max(w_sum))
            
        return ans
```
