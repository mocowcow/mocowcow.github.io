---
layout      : single
title       : LeetCode 104. Maximum Depth of Binary Tree
tags 		: LeetCode Easy DFS BFS BinaryTree
---
每日題。下雨好冷，聽說明天會更冷。

# 題目
輸入一個二元樹的根節點，求整棵樹最大的深度。

# 解法
題目只問深度，可以無視節點的值。維護depth變數計算最大深度，從root開始做DFS，邊往下走邊更新depth。

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth=0
        
        def dfs(node,d):
            nonlocal depth
            if not node:
                return 
            depth=max(depth,d)
            dfs(node.left,d+1)
            dfs(node.right,d+1)
        
        dfs(root,1)
        
        return depth
```

無聊看下討論區，發現更睿智的解法，果然多增廣見聞是好的。

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            return 1+max(dfs(node.left),dfs(node.right))

        return dfs(root)
```