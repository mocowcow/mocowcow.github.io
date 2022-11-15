--- 
layout      : single
title       : LeetCode 2467. Most Profitable Path in a Tree
tags        : LeetCode Medium Array Tree Graph HashTable DFS
---
雙周賽91。題目超級長，寫起來也超級長，只要Alice和Bob出現幾乎都沒好事。  

# 題目
有一棵無向樹，n個節點編號分別為0到n-1，且節點0為根。輸入一個長度為n-1的2D整數陣列edge，其中edge[i] = [a<sub>i</sub>, b<sub>i</sub>] 表示節點 a<sub>i</sub>和b<sub>i</sub>之間的邊。  

在每個節點i都有一個門。你還會得到一個偶數陣列amount，其中amount[i]代表：  
- 若amount[i]為負數，則代表在i節點失去的分數  
- 若amount[i]為正數，則代表在i節點得到的分數  

遊戲照以下規則進行：  
- 最初Alice從節點0出發，而Bob從節點bob出發  
- 每一秒，Alice和Bob都會移動到一個相鄰的節點。Alice的目標是任一個葉節點，而Bob的目標是節點0  
- 對於路徑上的每個節點，Alice和Bob要必須付出或是得到該扇門的分數，注意：  
> 若門已經被另一人打開，則無事發生 
> 若同時抵達某節點，則他們將平分該們的收入/損失  

當Alice抵達任意葉節點就會停止移動。同理，如果Bob抵達節點0就會停止移動。注意，這些事件是相互獨立的。  
求Alice選擇最佳的葉節點，能夠擁有的**最大分數**是多少。  

# 解法
樹中不存在循環，代表bob的移動路徑只有一種。我們利用時間戳+dfs紀錄bob在前往節點0途中，抵達各節點的時間點。在dfs的途中，只有bob順利抵達0的那條路線才要標記時間戳，其他節點應保持未訪問狀態(其實也可以是-1或是null，這裏為了後續判斷方便所以使用極大值)。  

找到bob的移動路線後，接下來輪到alice了。和bob不同，alice可以有很多條路線，只要某個節點沒有繼續往其他相鄰節點移動，那麼他就是葉節點，以當前分數更新答案最大值。  
移動的過程中，要檢查當前節點bob是否也有經過，以及其抵達時間：若bob沒有經過，則alice必須接受分數變化；否則依時間決定，兩同時則只取分數變化的一半，否則不改變分數。  

注意答案初始值必須設為極小值，因為amount有可能全部為負值，否則無法處理負數。  

所有節點都會遍歷兩次，也需要大小N來表儲存節點的訪問狀態，故時空複雜度皆為O(N)。  

```python
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        N=len(amount)
        bob_time=[inf]*N
        bob_visited=[False]*N
        alice_visited=[False]*N
        ans=-inf
        g=defaultdict(list)
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(i,t):
            bob_visited[i]=True
            if i==0:
                bob_time[i]=t
                return True
            find=False
            for j in g[i]:
                if not bob_visited[j]:
                    if dfs(j,t+1):
                        find=True
                        bob_time[i]=t
            return find
        
        dfs(bob,0)
        
        def dfs2(i,t,cost):
            nonlocal ans
            alice_visited[i]=True
            if t<bob_time[i]:
                cost+=amount[i]
            elif t==bob_time[i]:
                cost+=amount[i]//2
                
            leaf=True
            for j in g[i]:
                if not alice_visited[j]:
                    leaf=False
                    dfs2(j,t+1,cost)
            if leaf:
                ans=max(ans,cost)
        
        dfs2(0,0,0)
        
        return ans
```
