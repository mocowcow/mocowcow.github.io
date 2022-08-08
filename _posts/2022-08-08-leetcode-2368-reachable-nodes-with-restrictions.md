--- 
layout      : single
title       : LeetCode 2368. Reachable Nodes With Restrictions
tags        : LeetCode
---
周賽305。看來我的思路和大部分人不同：我在建圖的時候直接忽略禁止的點，而大多數人都選擇在遍歷的時候才過濾，怪哉。  

# 題目
有一棵無向樹，其n個節點編號從0到n-1，共有n-1條邊。  
輸入長度為n-1的二維陣列egdes，其中edges[i] = [ai, bi]，表示節點ai和bi之間有一條邊。另外還有整數陣列restricted，代表禁止前往的節點編號。

求從節點0出發，在不前往禁止節點前提下，最多能夠訪問多少個節點。  
注意，節點0永遠不會被禁止。  

# 解法
被禁止的節點不能進入，也不會從上面出發，那乾脆一開始就無視他。  

先把restricted裝入集合re中，遍歷edges中的所有邊a,b，若至少其中一個點被禁止，則略過不管。  
另外維護集合seen代表訪問過的節點，從節點0開始dfs，結束時seen的大小正好是所有訪問過的節點數量，直接回傳seen的大小。  

```python
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g=defaultdict(list)
        re=set(restricted)
        seen=set()
        
        for a,b in edges:
            if a in re or b in re:continue
            g[a].append(b)
            g[b].append(a)
                
        
        def dfs(i):
            if i in seen:return 
            seen.add(i)
            for j in g[i]:
                dfs(j)
            
        dfs(0)
        
        return len(seen)
```

正常建立有向圖，改在遍歷樹的過程中檢查節點是否被禁止。

```python
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g=defaultdict(list)
        re=set(restricted)
        seen=set()
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
                
        
        def dfs(i):
            if i in seen:return 
            seen.add(i)
            for j in g[i]:  
                if j not in re:
                    dfs(j)
            
        dfs(0)
        
        return len(seen)
```