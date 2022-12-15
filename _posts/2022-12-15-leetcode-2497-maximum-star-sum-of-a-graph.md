--- 
layout      : single
title       : LeetCode 2497. Maximum Star Sum of a Graph
tags        : LeetCode Medium Array Graph HashTable Sorting Heap
---
雙周賽93。終於來個難度適中的Q2，結果我還吃到WA，丟人。  

# 題目
有個無向圖由n個節點組成，節點編號分別為0\~n-1。  
輸入長度同為n的整數陣列vals，其中vals[i]代表第i個節點的值。  
另外還有一個二維陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表a<sub>i</sub>和b<sub>i</sub>之間存在一條無向的邊。  

**星型圖**指的是一個子圖，以某節點為中心，並擁有0或多個相鄰節點。換句話說，這個子圖中的所有邊都存在公共節點。  
而**星型和**指的是星型圖所有節點值的總和。  

輸入整數k，求最多擁有k個相鄰節點的星型圖的**最大星型和**。  

# 解法
講白了就是窮舉每個節點做為中心，然後找出k個最大的鄰居加起來。  

其中有兩個小細節：  
1. 節點值有可能為負數，所以ans初始化必須是最小值  
2. 題目要求**最多**k個鄰居，負數的鄰居(惡鄰居?)可以不要拿  

先建圖，但不是加入相鄰節點，而是直接加入節點值。至於壞鄰居的情況，可以在找前k大的時候處理，也可以在建圖的時候先判斷，若非正數則不加入。  
然後窮舉每個點，先找遞減排序相鄰的點，找到前k大的正數，加上當前節點值更新答案。  

時間瓶頸在於排序，如果某個點和所有的點都相連會是O(N log N)，整體時間複雜度應該為O(N+M+(N log N))。  
而N個節點共要保存M個邊，空間複雜度為O(M+N)。  

```python
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        N=len(vals)
        g=defaultdict(list)
        ans=-inf
        
        for a,b in edges:
            g[a].append(vals[b])
            g[b].append(vals[a])
            
        for i in range(N):
            adj=[x for x in sorted(g[i],reverse=True)[:k] if x>0]
            ans=max(ans,vals[i]+sum(adj))
            
        return ans
```

在建圖的時候直接忽略非正數，並使用python內建的找前k大函數。  
nlargest使用的是heap，若在n數中找的前k大的話會是O(n log k)，所以時間複雜度會比上面的方法降低一些。  

```python
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        N=len(vals)
        g=defaultdict(list)
        ans=-inf
        
        for a,b in edges:
            g[a].append(max(vals[b],0))
            g[b].append(max(vals[a],0))
            
        for i in range(N):
            ans=max(ans,vals[i]+sum(nlargest(k,g[i])))
            
        return ans
```