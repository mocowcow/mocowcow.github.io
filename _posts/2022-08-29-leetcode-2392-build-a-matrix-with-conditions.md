--- 
layout      : single
title       : LeetCode 2392. Build a Matrix With Conditions
tags        : LeetCode Hard Array Matrix HashTable Graph TopologySort
---
周賽308。其實算是很簡單的Q4，但我沒看出來是拓樸排序，在那邊貪心半天。賽後看到知道是拓樸排序就馬上寫出來了，好冤。  

# 題目
輸入正整數k，以及兩個由1\~k組成的二元陣列：  
- 大小為n的二維整數陣列rowConditions，其中rowConditions[i] = [abovei, belowi]  
- 大小為m的二維整數陣列colConditions，其中colConditions[i] = [lefti, righti]  

你必須構建一個k\*k矩陣，其中包含1\~k的每個數字正好一次。其餘格子的值應為0。  

該矩陣需滿足以下條件：  
- 對於0\~n-1中的每個i，abovei的所在列必須嚴格在於belowi所在列的上方  
- 對於0\~m-1中的每個i，lefti的所在行必須嚴格在於righti所在行的左方  

回傳任何滿足條件的矩陣。如果沒有答案，則回傳空矩陣。  

# 解法
行列的限制條件是獨立的，不會交互影響，所以可以分開處理。  
仔細想想，right必須出現在left的右方，就像是選修B課程前必須先修完A課程，這就是**拓樸排序**的暗示吧。  

拓樸排序可以在**有向無環圖**中找到合法的訪問順序。  
首先需要遍歷所有的邊，建立有向圖g，並維護**入度**陣列indegree。當某個點入度為0時，代表先決條件已經符合，接下來可以訪問。  

建完圖g後，我們找出所有入度0的點，加入佇列中進行bfs。每訪問節點i，先將i點加到輸出順序out中，再將其所有相鄰節點j入度減少一，若入度成為0則加入佇列。bfs結束後回傳out，即為各節點的訪問順序。  

如果圖中某些點存在**循環**，則那些點不會被訪問到，自然不會出現在out中。  
所以我們分別對行、列的限制做拓樸排序後，先檢查的到的順序是不是都為k。若否，則代表條件不合法， 直接回傳空矩陣。  
最後只要建立各數字和出現索引的映射，填入矩陣中即可。  

拓樸排序的時間複雜度是O(V+E)，V是頂點數量，也就是k，而E是邊的數量。E的上限是10^4，而k是400。  
主要成本是在於產生矩陣，要建立k\*k的矩陣，所以整體複雜度應該是O(k^2)。  

```python
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topology_sort(cond):
            indegree=[0]*(k+1)
            g=defaultdict(list)
            q=deque()
            out=[]
            
            for a,b in cond:
                g[a].append(b)
                indegree[b]+=1
            
            for i in range(1,k+1):
                if indegree[i]==0:q.append(i)   
        
            while q:
                i=q.popleft()
                out.append(i)
                for j in g[i]:
                    indegree[j]-=1
                    if indegree[j]==0:q.append(j)
            return out
        
        rows=topology_sort(rowConditions)
        cols=topology_sort(colConditions)
        
        if not len(rows)==len(cols)==k:
            return []
        
        row_mp={n:i for i,n in enumerate(rows)}
        col_mp={n:i for i,n in enumerate(cols)}
        mat=[[0]*k for _ in range(k)]
        
        for i in range(1,k+1):
            r=row_mp[i]
            c=col_mp[i]
            mat[r][c]=i
        
        return mat
```
