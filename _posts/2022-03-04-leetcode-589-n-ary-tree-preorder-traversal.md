---
layout      : single
title       : LeetCode 589. N-ary Tree Preorder Traversal
tags 		: LeetCode Easy Tree DFS
---
Study Plan - Programming Skills。  

# 題目
輸入root為一N元樹的根結點，求這棵樹的前序遍歷。

# 解法
和普通二元樹前序差不多，只是加入更多子節點。

```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        ans=[]
        
        def dfs(node):
            if not node:
                return 
            ans.append(node.val)
            for child in node.children:
                dfs(child)
        
        dfs(root)
                
        return ans
```
