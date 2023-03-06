--- 
layout      : single
title       : LeetCode 2583. Kth Largest Sum in a Binary Tree
tags        : LeetCode Medium BinaryTree DFS Sorting
---
周賽335。

# 題目
輸入一棵二元樹的根節點root以及正整數k。  

**層總和**指的是**同一層**中所有節點的值的總和。  

求此樹中**第k大**的層總和。若不足k層則回傳-1。  

# 解法
直接dfs算出每層的總和。  
如果不足k層則回傳-1；否則將各層總和排序，回傳第k大者。  

時間複雜度O(H log H)，其中H為樹的高度。空間複雜度O(H)。  

```python
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        d=Counter()
        
        def dfs(o,lvl):
            if not o:return 
            d[lvl]+=o.val
            dfs(o.left,lvl+1)
            dfs(o.right,lvl+1)
            
        dfs(root,0)
        
        if len(d)<k:
            return -1
        
        return sorted(d.values())[-k]
```
