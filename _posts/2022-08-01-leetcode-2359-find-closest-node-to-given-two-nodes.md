--- 
layout      : single
title       : LeetCode 2359. Find Closest Node to Given Two Nodes
tags        : LeetCode
---
周賽304。不知道為什麼無法理解題目描述，還以為要node1盡可能多走，node2盡可能少走。等了一小時才開竅，真想打死我自己。  
真心希望這種較大較小的關係可以用公式來表達，不然至少句子短一點。  

# 題目
輸入一個n節點的有向圖，節點編號從0到n-1，每個節點最多有一條出邊。
另有長度為n的整數陣列edges，其中edges[i]代表節點i的到edges[i]存在一條有向出邊。若沒有出邊則edges[i]為-1。  

另外還有兩個整數node1和node2。  
找到某個節點，同時可以從node1和node2出發而抵達，且**node1和該節點的距離**與**node2和該節點的距離**的較大值**最小化**。若有多個符合的節點，則選擇索引較小者。若不存在則回傳-1。    

請注意，圖中可能包含循環。  

# 解法
理解題意之後其實很簡單，分別從node1和node2出發，算出抵達各點的距離為多少。  
之後遍歷每個節點，若從兩節點出發皆可抵達，則以兩距離取較大者mmx，再拿去和當前最大值mx比較，若小於mx則更新答案。  

```python
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N=len(edges)
        
        def f(i):
            dist=[-1]*N
            step=0
            curr=i
            while curr!=-1 and dist[curr]==-1:
                dist[curr]=step
                step+=1
                curr=edges[curr]
            return dist
        
        dist1=f(node1)
        dist2=f(node2)
        ans=-1
        mx=inf
        
        for i,(a,b) in enumerate(zip(dist1,dist2)):
            if a==-1 or b==-1:continue
            mmx=max(a,b)
            if mmx<mx:
                ans=i
                mx=mmx
            
        return ans
        
```
