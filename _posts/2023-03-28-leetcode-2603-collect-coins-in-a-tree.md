--- 
layout      : single
title       : LeetCode 2603. Collect Coins in a Tree
tags        : LeetCode Hard Array Graph TopologySort
---
周賽338。網站卡了40幾分鐘，做完前面三題根本沒時間看，連題目都沒看懂就結束了。不過我倒有猜到是拓樸排序。  

# 題目
有一棵n個節點的無向樹，節點編號分別為0\~n-1，且沒有指定根節點。  
輸入整數n和長度為n-1的二維陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表a<sub>i</sub>和b<sub>i</sub>之間存在一條邊。  
另外還有長度為n，且只由1和0組成的陣列coins。1表示第i個上存在一個硬幣。  

最初，你可以選擇任意節點作為起點。然後可以執行以下操作任意次：  
- 收集所有與當前節點最多2步以內的硬幣  
- 移動到任意相鄰的節點  

求**收集所有硬幣**，然後返回出發點所需經過的**最小邊數**。  

注意：如果你通過同一條邊數次，則每次都要計入答案。   

# 解法
目標是拿全部的硬幣，所以節點上沒有硬幣就可以不管他。  
而且可以收集距離當前節點兩步以內的所有硬幣，這代表沒必要走到**葉節點**。  

從範例2來看，節點6是唯一沒有硬幣的葉節點，無視也不影響答案。依此推廣，如果節點6下面還有更多個沒有硬幣的節點，也是可以全部刪除、且不影響答案的。  
如此可知，要先進行一次拓樸排序，將所有**沒有硬幣的葉節點刪除**。  

這時剩下的所有葉節點都擁有硬幣。根據上述提過的：不需要走到葉節點，所以應該只要走到距離葉節點兩步以外的其他節點就可以。  
繼續看範例2，刪除掉無硬幣葉節點之後，只剩下[3,4,7]三個葉節點有硬幣。這時後再做兩次拓樸排序，刪掉不必走的葉節點，最後剩下[0,2]兩個節點。只要在[0,2]兩個節點上就可以收完所有硬幣。  
而題目說可以從任意位置出發，最終要返回原點，意味著不管怎樣走，每條邊都要**來回各一次**。  

而剩下remain個沒被刪掉的節點，之間共有remain-1條邊，答案就是(remain-1)\*2。  
注意特例：當刪到只剩下0或1個節點時，不存在任何邊，會計算出負值，所以要和0取max。  

時間複雜度O(N)。空間複雜度O(N)。  

```python
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        N=len(coins)
        g=[[] for _ in range(N)]
        degree=[0]*N
        remain=N
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            degree[a]+=1
            degree[b]+=1
            
        # drop no coin leaves
        q=deque()
        
        for i in range(N):
            if degree[i]==1 and coins[i]==0:
                q.append(i)

        while q:
            i=q.popleft()
            remain-=1
            for j in g[i]:
                degree[j]-=1
                if degree[j]==1 and coins[j]==0:
                    q.append(j)

        # drop leaves twice
        for i in range(N):
            if degree[i]==1 and coins[i]==1:
                q.append(i)

        for _ in range(2):
            for _ in range(len(q)):
                i=q.popleft()
                remain-=1
                for j in g[i]:
                    degree[j]-=1
                    if degree[j]==1:
                        q.append(j)
        
        return max(0,(remain-1)*2)
```
