--- 
layout      : single
title       : LeetCode 236. Lowest Common Ancestor of a Binary Tree
tags        : LeetCode
---
每日題。自己寫得很順，但卻無法順利解釋為什麼這樣寫，今天做這篇題解算是有收穫了。  

# 題目
輸入一棵二元樹，還有節點p和q，找到兩節點的最低共同祖先(LCA)。  

# 解法
我們可以先簡單的分出三種情形：
1. q在p的子樹裡面  
2. p在q的子樹裡面  
3. p和q分別在某節點的左右子樹  

撰寫一個遞迴函數dfs來遍歷這棵二元樹，並回傳p和q的LCA。  
當節點為空時，回傳null；當前節點等於p時，可以假設q在p的子樹之下，故回傳p；同理，當前節點等於q時，假設p在q的子樹之下，回傳q。  
若不符合以上條件，則對左右兩子樹dfs，找到看LCA在哪邊。如果兩邊都有回傳非空節點，代表當前節點才是**真正的LCA**，回傳當前節點；否則回傳唯一的那個LCA。

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            if node==p or node==q:
                return node
            l=dfs(node.left)
            r=dfs(node.right)
            if l and r:
                return node
            return l or r
        
        return dfs(root)
```
