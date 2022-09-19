--- 
layout      : single
title       : LeetCode 2415. Reverse Odd Levels of Binary Tree
tags        : LeetCode Medium BinaryTree BFS DFS TwoPointers
---
周賽311。其實這也是秒殺題，只是我在雙指針反轉的時候不小心打錯字，想說怎麼輸出錯誤，浪費10分鐘才找到原因。  

# 題目
輸入一棵prefect二元樹的根節點，反轉樹中每個奇數層的節點值。  
例如第3層的節點值為[2,1,3,4,7,11,29,18]，則應反轉為[18,29,11,7,4,3,1,2]。  
回傳反轉過後的樹根節點。  

# 解法
prefect二元樹整個節點塞滿滿，非常友好，而且反轉是整層倒過來，沒有任何意外。  
先進行一次dfs把所有節點依照深度分類，之後對所有奇數層使用雙指針將數值反轉。  

```python
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d=defaultdict(list)
        
        def dfs(node,lvl):
            if not node:
                return 
            d[lvl].append(node)
            dfs(node.left,lvl+1)
            dfs(node.right,lvl+1)
            
        dfs(root,0)
        
        for lvl,nodes in d.items():
            if lvl&1:
                lo=0
                hi=len(nodes)-1
                while lo<hi:
                    nodes[lo].val,nodes[hi].val=nodes[hi].val,nodes[lo].val
                    lo+=1
                    hi-=1
        
        return root
```

BFS版本，和上面版本大同小異。  

```python
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d=defaultdict(list)
        
        q=deque()
        q.append([root,0])
        while q:
            node,lvl=q.popleft()
            if not node:
                continue
            d[lvl].append(node)
            q.append([node.left,lvl+1])
            q.append([node.right,lvl+1])
                  
        for k in d:
            if k%2==1:
                nodes=d[k]
                l=0
                r=len(nodes)-1
                while l<r:
                    t=nodes[l].val
                    nodes[l].val=nodes[r].val
                    nodes[r].val=t
                    l+=1
                    r-=1

        return root
```