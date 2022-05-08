--- 
layout      : single
title       : LeetCode 2265. Count Nodes Equal to Average of Subtree
tags        : LeetCode Medium BinaryTree DFS
---
周賽292。好像很少在Q2看到二元樹，但也不算難。

# 題目
輸入一棵二元樹的根節點root，求樹中有幾個節點，其節點值等於**子樹節點平均值**。  
- n個節點的子樹，其平均值=(n個節點值加總)/n 向下取整  
- root的子樹由root和他的所有後代組成  

# 解法
以root為根的子樹，其總和值為root值+左子樹總和+右子樹總和，而節點樹為1+左子樹節點數+右子樹節點數。這樣遞迴關係式就出來了。  
定義dfs(node)函數，每次回傳長度為2的陣列，第一個位置為node子樹的總節點數，第二個位置為node子樹的總和。  
以post order的方式往左右子樹dfs，求出正確值後再來判斷平均值是否等於此節點node的值。

```python
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return [0, 0]
            l = dfs(node.left)
            r = dfs(node.right)
            cntNodes = 1+l[0]+r[0]
            sumVal = node.val+l[1]+r[1]
            if sumVal//cntNodes==node.val:
                ans += 1
            return [cntNodes, sumVal]

        dfs(root)

        return ans
```
