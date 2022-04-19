---
layout      : single
title       : LeetCode 99. Recover Binary Search Tree
tags 		: LeetCode Medium BinarySearchTree DFS
---
每日題。又是二分搜尋樹，follow up還要求O(1)空間解法，結果人有爆氣說沒必要反芻五十年前的垃圾演算法，有夠好笑。

# 題目
輸入一個**錯誤**的二元搜尋樹，其中有正好2個節點互相被換了位置。在不改變樹的結構下，將節點值恢復到正確的位置。

# 解法
先遍歷一次樹，取出所有節點值後排序。以中序遍歷再走一次樹，把節點值依序放回正確的位置上即可。

```python
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        nodes=[]
        
        def get(node):
            if not node:
                return 
            get(node.left)
            nodes.append(node.val)
            get(node.right)
        
        get(root)
        nodes.sort(reverse=1)
        
        def put(node):
            if not node:
                return 
            put(node.left)
            node.val=nodes.pop()
            put(node.right)
            
        put(root)
```

