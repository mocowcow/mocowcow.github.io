--- 
layout      : single
title       : LeetCode 2646. Minimize the Total Price of the Trips
tags        : LeetCode Hard Array Graph BFS DP
---
周賽341。相似題[337. house robber iii]({% post_url 2022-05-09-leetcode-337-house-robber-iii %})。  

# 題目
有個n節點且沒有根的樹，節點編號分別為0\~n-1。  
輸入整數n和長度為n-1的二維陣列edges，其中edges[i] = [ai, bi]代表ai和bi之間存在一條邊。  

每個節點都有相應的價格。輸入整數陣列price，其中price[i]代表第i個節點的價格。  

**總價**指的是一條路徑上所有節點價格的總和。  

接下來還有二維矩陣trips，其中trips[i] = [starti, endi]代表你必須從starti出發，抵達endi，路徑不限。  

在開始旅行前，你可以將數個**互不相鄰**的節點價格減半。  

回傳每趟旅行的**最低總價**。  

# 解法
題目給的是一棵樹，也就是沒有循環，代表兩節點之間一定**只有一條最短路徑**。  
雖然說不限定路徑，但在所有節點權重不為負時，回頭走是沒有意義的，因此肯定選擇最短路徑。  
在這些前提下，想要知道兩點之間的最短路徑，只要從某一點開始做bfs就可以找到，每次時空間複雜度O(n)。  

而後面需要查詢q次trips，全部都是共用同種價格減半的方案。那麼我們可以先算出全部的旅行總共**經過那些點各多少次**，再來考慮哪哪種減半方案最佳。到目前為止，時間複雜度O(q\*n)，空間複雜度O(n)。  

現在我們知道每一個節點共出現幾次，乘上該節點的價格，得到節點的**總價格**。  
例如一顆直線的樹：  
> (0) - (1) - (2)  
> 價格分別為3,4,5  
> trips[0]要從0到1，路徑是[0,1]  
> trips[1]要從0到2，路徑是[0,1,2]  
> 所以節點0會經過2次，總價格為3\*3=6  
> 節點1會經過2次，總價格為4\*2=8  
> 節點2會經過1次，總價格為5\*1=5  
> 將節點的價格以總價表示為 (6) - (8) - (5)  

接下來問題轉化成單純的樹狀DP，以任意節點為根，每個子樹有**減半或不減**兩種選擇，時空間複雜度O(n)。  
定義dp(i,fa,ok)：在節點i父節點為fa的子樹時，子樹的**最小總價格**。ok為true代表節點i可以減半。  
轉移方程式：j為i的子節點，若ok為true，可選擇**i減半**加上所有dp(j,i,false)的總和，以及**i不減半**加上所有dp(j,i,true)的較小者；若ok為false，代表父節點已經減半過，i只能不變，加上所有dp(j,i,true)的總和。  

整體時間複雜度O(q\*n)，其中q查詢次數，n為節點數。空間複雜度O(n)。  

```python
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g=[[] for _ in range(n)]
        tot=[0]*n
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            
        # count total sum for each node
        for start,end in trips:
            # bfs to find path
            q=deque()
            q.append([start,-1,[start]]) # i, fa, path
            
            while q:
                i,fa,path=q.popleft()
                if i==end: # merge path value sum
                    for x in path:
                        tot[x]+=price[x]

                    break
                for j in g[i]:
                    if j==fa:continue
                    q.append([j,i,path+[j]])
                    
        # dp on tree, half total price or not
        @cache
        def dp(i,fa,ok):
            half=tot[i]//2
            nohalf=tot[i]
            for j in g[i]:
                if j==fa:continue
                half+=dp(j,i,False)
                nohalf+=dp(j,i,True)
            
            if ok:
                return min(half,nohalf)
            return nohalf
        
        return dp(0,-1,True)
```
