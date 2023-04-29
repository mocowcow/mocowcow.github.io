--- 
layout      : single
title       : LeetCode 1697. Checking Existence of Edge Length Limited Paths
tags        : LeetCode Hard Array Graph UnionFind Sorting TwoPointers
---
每日題。感覺我好像有抓到並查集的精隨。  
以前並查集都是去貼封裝好的模板，現在反而是直接手刻，比複製貼上還順手。  

# 題目
有個n節點的無向圖，由edgeList表示所有的邊，其中edgeList[i] = [u<sub>i</sub>, v<sub>i</sub>, dis<sub>i</sub>]，代表u<sub>i</sub>和v<sub>i</sub>之間有條距離為dis<sub>i</sub>的邊。  
注意：兩節點間可能有多條邊。  

輸入陣列queries，其中queries[j] = [p<sub>j</sub>, q<sub>j</sub>, limit<sub>j</sub>]，你必須檢查p<sub>j</sub>和q<sub>j</sub>中間是否存在一條路徑，且路徑上的每條邊都**嚴格小於**limit<sub>j</sub>。  

回傳和queries等長的布林陣列answer，其中answer[j]代表queries[j]的結果。  

# 解法
相似題[2421. number of good paths]({% post_url 2022-09-25-leetcode-2421-number-of-good-paths %})。  

查詢問的是能否**只走小於limit的邊**從p抵達q。因此我們只要加入所有小於limit的邊，再來確認p和q是否連通。  
說到連通圖，當然就是並查集。並查集可在O(1)時間找出根節點，只要p, q兩點的根相同，則為連通。  

剛才說到要依照邊的距離，由小到大逐步加入，所以先將每個邊按照其距離分組。  
但是查詢中的limit是隨機的，時大時小。同理，我們也可以依照limit將查詢分組。  

最後只要從小到大窮舉limit，先**處理所有查詢qeuries[j]**，並在answer[j]填上是否連通。然後才將所有距離為limit的邊edgeList[i]連上。  
注意：因為查詢是要嚴格小於limit，**一定要先查詢**！加完邊才查就錯了。  

時間複雜度O(n + E + Q + MX)，其中Q為查詢次數，E為邊的個數，MX為所有limit<sub>j</sub>和dis<sub>i</sub>中的最大值。  
空間複雜度O(n + E + MX)。  

```python
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        fa=list(range(n))
        
        def find(i):
            if fa[i]!=i:
                fa[i]=find(fa[i])
            return fa[i]
        
        def union(i,j):
            fa1=find(i)
            fa2=find(j)
            if fa1!=fa2:
                fa[fa1]=fa2

        qs=[[] for _ in range(100005)] # qeury indexes, grouped by limit
        for j,q in enumerate(queries):
            qs[q[2]].append(j)
            
        es=[[] for _ in range(100005)] # edge indexes, grouped by distance
        for i,e in enumerate(edgeList):
            es[e[2]].append(i)
   
        ans=[False]*len(queries)
        for limit in range(100005):
            # update query answers
            for j in qs[limit]:
                a,b,_=queries[j]
                if find(a)==find(b):
                    ans[j]=True
                    
            # add edges
            for i in es[limit]:
                a,b,_=edgeList[i]
                union(a,b)

        return ans
```

如果limit的範圍很大，沒辦法直接開陣列去分組，那只好帶著原本的索引位置將edges和queries排序。  
使用雙指針或是隊列來維護當前處理到的位置。如果還有dis小於當前limit的邊，就全部加入，然後判斷p, q兩點是否連通。  

```python
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        fa=list(range(n))
        
        def find(i):
            if fa[i]!=i:
                fa[i]=find(fa[i])
            return fa[i]
        
        def union(i,j):
            fa1=find(i)
            fa2=find(j)
            if fa1!=fa2:
                fa[fa1]=fa2
        
        es=[[i,u,v,dis] for i,(u,v,dis) in enumerate(edgeList)]
        qs=[[j,p,q,limit] for j,(p,q,limit) in enumerate(queries)]
        es.sort(key=itemgetter(3))
        qs.sort(key=itemgetter(3))
        ans=[False]*len(queries)
        
        i=j=0
        while j<len(qs):
            idx,p,q,limit=qs[j]
            while i<len(es) and es[i][3]<limit:
                union(es[i][1],es[i][2])
                i+=1
            ans[idx]=find(p)==find(q)
            j+=1
            
        return ans
```