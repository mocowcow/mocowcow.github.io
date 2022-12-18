--- 
layout      : single
title       : LeetCode 2508. Add Edges to Make Degrees of All Nodes Even
tags        : LeetCode Hard Array Graph HashTable
---
周賽324。又是麻煩的分類討論，最近常常栽在這種類型上，今天大部分的時間都浪費在這題。  

# 題目
輸入一個n節點的無向圖，節點編號從1\~n。另外還有二維陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表a<sub>i</sub>, b<sub>i</sub>之中存在一條邊。整個圖有可能是非連通的。  

你最多可以在圖中**加入2條邊(也可以不加)**，但不能有重複的邊，或是同個節點自己連接自己。  

若能使得每個節點存在的邊為**偶數**條，則回傳true，否則回傳false。  

# 解法
首先建圖，紀錄每個節點和其他那些節點有連接。然後過濾出邊數為奇數的節點，稱為**非法節點**。  
我們最多只能新增**兩條**邊，一條邊可以使得兩個奇數節點變成偶數，也就是說最多只能容忍4個非法節點。換個角度來看，每次加入一條邊，一定需要兩個節點，所以**奇數個非法節點**也不可能達成要求。而0個非法節點直接就是合法的，不需要新增。  

但是範例3也是4個非法節點，卻沒辦法全部變成偶數，然後我就卡了半小時完全沒頭緒。  
後來想通，假設有ABCD四個節點，一定要有兩顆之間不連通，而另外兩顆也不連通，才能達成需求。      
也就是(A,B)+(C,D), (A,C)+(B,D), (A,D)+(B,C)這三種情況之一。  

然後2個非法節點也很囉唆，這兩個點有可能本身就連通，這時就要找到與這兩節點互不連通的**第三個節點**。  

時空間複雜度O(n+m)，其中n為節點數量，m為邊數量。  

```python
class Solution: 
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        g=defaultdict(set)
        for a,b in edges:
            g[a].add(b)
            g[b].add(a)
        
        cand=[]
        for i in range(1,n+1):
            if len(g[i])%2==1:cand.append(i)

        odd=len(cand)
        if odd==2:
            for i in range(1,n+1):
                if cand[0] not in g[i] and cand[1] not in g[i]:return True
        if odd==4:
            if (cand[0] not in g[cand[1]]) and (cand[2] not in g[cand[3]]):return True
            if (cand[0] not in g[cand[2]]) and (cand[1] not in g[cand[3]]):return True
            if (cand[0] not in g[cand[3]]) and (cand[1] not in g[cand[2]]):return True
            
        return odd==0
```
