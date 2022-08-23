--- 
layout      : single
title       : LeetCode 2385. Amount of Time for Binary Tree to Be Infected
tags        : LeetCode
---
周賽307。

# 題目
輸入一顆節點值不重複的二元樹root，和一個整數start。在第0分鐘，start節點會受到感染。  

每分鐘，若符合以下情況，節點就會被感染：  
- 該節點未受感染  
- 該節點與受感染的節點相鄰  

求整顆樹被感染需要多久。  

# 解法
雖然很清楚明瞭要從start開始bfs出去，但樹節點沒有紀錄父節點，需要自己建圖。  

維護一個圖g，在dfs函數遍歷整顆樹途中讓父子節點建立雙向連結。  
然後從start點開始bfs，直到所有點都走過一次為止。  

dfs和bfs都只會經過各節點一次，時間複雜度為O(N)。  

```python
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g=defaultdict(list)
        
        def add(p,c):
            g[p].append(c)
            g[c].append(p)
        
        def dfs(node):
            val=node.val
            if node.left:
                add(val,node.left.val)
                dfs(node.left)
            if node.right:
                add(val,node.right.val)
                dfs(node.right)
            
        dfs(root)
            
        visited=set()
        visited.add(start)
        q=deque([start])
        ans=-1
        
        while q:
            ans+=1
            for _ in range(len(q)):
                curr=q.popleft()
                for adj in g[curr]:
                    if adj not in visited:
                        q.append(adj)
                        visited.add(adj)
                        
        return ans
```

也可以只在dfs中建立父節點的映射，而不建立整個圖。  
bfs感染的時後要檢查左右節點以及父節點。  

```python
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent={}
        start_node=None
        
        def dfs(node,prev):
            nonlocal start_node
            if not node:return 
            if prev:parent[node]=prev
            if node.val==start:start_node=node
            dfs(node.left,node)
            dfs(node.right,node)
            
        dfs(root,None)
            
        visited=set()
        visited.add(start_node)
        visited.add(None)
        q=deque([start_node])
        ans=-1
        
        while q:
            ans+=1
            for _ in range(len(q)):
                node=q.popleft()
                if node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                if node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)
                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    q.append(parent[node])
                              
        return ans
```