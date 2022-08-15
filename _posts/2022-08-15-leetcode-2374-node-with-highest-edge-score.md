--- 
layout      : single
title       : LeetCode 2374. Node With Highest Edge Score
tags        : LeetCode Medium Array
---
周賽306。其實這題放到Q1也可以吧，說是graph只是幌子，但是好像不少人被騙到。  

# 題目
有一個有向圖，有n個節點，編號從0到n-1，每個節點正好有一個出邊。  
輸入長度為n的陣列edges，代表節點i的出邊指向edge[i]。  

**邊際分數**指的是指向該節點的來源節點編號總和。  
回傳**邊際分數**最高的節點。若有多個相同分數的節點，則回傳索引最小者。  

# 解法
其實根本不用建圖，只要遍歷所有邊，以來源節點的編號作為分數，加到目標節點上。  
最後找到分數最大的節點即可。  

```python
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        N=len(edges)
        scores=[0]*N
        
        for i,to in enumerate(edges):
            scores[to]+=i
            
        ans=-1
        mx=-inf
        
        for i,sc in enumerate(scores):
            if sc>mx:
                mx=sc
                ans=i
                
        return ans
```
